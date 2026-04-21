import sys
import platform
from PySide6.QtCore import QProcess, Slot
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout, QTextBrowser)


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.executable = 'ping'
        if platform.system() == 'Windows':
            self.arguments = ['google.com']
        else:
            self.arguments = ['google.com', '-c', '4']

        self.log_widget = QTextBrowser()
        self.button = QPushButton('Run Command')
        self.button.clicked.connect(self.run_process)

        layout = QVBoxLayout(self)
        layout.addWidget(self.log_widget)
        layout.addWidget(self.button)
        
        # 1. Create a QProcess and connect its signals.
        
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.log_stdout)
        self.process.readyReadStandardError.connect(self.log_stderr)
        self.process.errorOccurred.connect(self.log_error)
        self.process.stateChanged.connect(self.log_state_change)
        self.process.finished.connect(self.log_finished)
    
    # 2. Start the external process.
    
    def run_process(self):
        self.button.setDisabled(True)
        self.log_widget.clear()
        self.log_widget.append(f'Running process: {self.executable}')
        self.log_widget.append(f'Argument(s): {self.arguments}')
        self.process.start(self.executable, self.arguments)
    
    # 3. Handle signals.
    
    @Slot()
    def log_stdout(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.log_widget.append(f'stdout: {output}')
    
    @Slot()
    def log_stderr(self):
        output = self.process.readAllStandardError().data().decode()
        self.log_widget.append(f'stderr: {output}')
    
    @Slot(QProcess.ProcessError)
    def log_error(self, error):
        self.log_widget.append(f'Error Code: {str(error)}')
        self.log_widget.append(f'Error: {self.process.errorString()}')
        self.button.setEnabled(True)
    
    @Slot(QProcess.ProcessState)
    def log_state_change(self, newState):
        self.log_widget.append(f'State changed: {str(newState)}')
    
    @Slot(int, QProcess.ExitStatus)
    def log_finished(self, exitCode, exitStatus):
        self.log_widget.append('Process finished!')
        self.log_widget.append(f'Exit code: {exitCode}')
        self.log_widget.append(f'Exit status: {str(exitStatus)}')
        self.button.setEnabled(True)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
