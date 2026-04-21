import sys
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout, QTextEdit)


CMD = 'git'
ARGS = ['--version']

class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.button = QPushButton('Check Git')
        self.button.clicked.connect(self.run_command)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_stdout)
        self.process.readyReadStandardError.connect(self.on_stderr)
        self.process.errorOccurred.connect(self.on_error_occurred)
        self.process.finished.connect(self.on_finished)

    def run_command(self):

        self.button.setDisabled(True)
        self.text_edit.clear()
        
        # 1. Start the process and wait for it to start.
        
        self.process.start(CMD, ARGS)
        ret_val = self.process.waitForStarted()
        if ret_val:
            self.text_edit.append('Git found, checking version...')
            
            # 2. Wait for the process to finish.
            
            self.process.waitForFinished()
            self.text_edit.append('Proceeding with Git operations.')
        else:
            self.text_edit.append('Git not found.')
            self.button.setEnabled(True)

    def on_stdout(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.text_edit.setText(output.strip())
        
    def on_stderr(self):
        output = self.process.readAllStandardError().data().decode()
        self.text_edit.setText(output.strip())
        
    def on_error_occurred(self):
        self.text_edit.setText(f'Error: {self.process.errorString()}')
        self.button.setEnabled(True)

    def on_finished(self):
        self.button.setEnabled(True)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
