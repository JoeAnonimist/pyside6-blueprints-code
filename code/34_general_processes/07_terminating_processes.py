import sys
import platform
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout, QTextBrowser)

class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        if platform.system() == 'Windows':
            self.executable = 'ping'
            self.arguments = ['-t', '127.0.0.1']
        else:
            self.executable = 'ping'
            self.arguments = ['127.0.0.1']

        self.log_widget = QTextBrowser()
        self.start_button = QPushButton('Start process')
        self.start_button.clicked.connect(self.start_process)
        
        self.stop_button = QPushButton('Stop process')
        self.stop_button.clicked.connect(self.stop_process)
        self.stop_button.setEnabled(False)

        layout = QVBoxLayout(self)
        layout.addWidget(self.log_widget)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.log_stdout)
        self.process.readyReadStandardError.connect(self.log_stderr)
        self.process.errorOccurred.connect(self.log_error)
        self.process.stateChanged.connect(self.log_state_change)
        self.process.finished.connect(self.log_finished)
    
    # 1. Start the process and track its state.
    
    def start_process(self):
        self.start_button.setDisabled(True)
        self.log_widget.clear()
        self.log_widget.append(f'Running process: {self.executable}')
        self.log_widget.append(f'Argument(s): {self.arguments}')
        self.process.start(self.executable, self.arguments)
        self.stop_button.setEnabled(True)
        
    def stop_process(self):
        self.stop_button.setEnabled(False)
        self.log_widget.append('Stopping the process')
        
        # 2. Try to terminate the process gracefully.
        
        self.process.terminate()
        
        # 3. If necessary, kill the process.
        
        if not self.process.waitForFinished(2000):
            self.process.kill()
            self.process.waitForFinished()
        self.start_button.setEnabled(True)

    def log_stdout(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.log_widget.append(f'stdout: {output.strip()}')
        
    def log_stderr(self):
        output = self.process.readAllStandardError().data().decode()
        self.log_widget.append(f'stderr: {output}')
        
    def log_error(self):
        self.log_widget.append(f'Error: {self.process.errorString()}')
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        
    def log_state_change(self, newState):
        self.log_widget.append(f'State changed: {str(newState)}')
        
    def log_finished(self):
        self.log_widget.append('Process finished!')
        self.start_button.setEnabled(True)
    
    # 4. Handle process termination on window close.
    
    def closeEvent(self, event):
        if self.process.state() == QProcess.ProcessState.Running:
            self.stop_process()
        super().closeEvent(event)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
