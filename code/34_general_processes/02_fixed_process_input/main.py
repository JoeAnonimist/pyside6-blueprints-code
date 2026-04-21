import sys
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout, QTextEdit)


with open('create_project.py', 'r') as file:
    script_text = file.read()

input_args = [b'my_app\n', b'Joe\n', b'12\n']


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.button = QPushButton('Run Command')
        self.button.clicked.connect(self.run_command)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        
        # 1. Create a QProcess and connect its signals.
        
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_stdout)
        self.process.readyReadStandardError.connect(self.on_stderr)
        self.process.errorOccurred.connect(self.on_error_occurred)
        self.process.stateChanged.connect(self.on_state_changed)
        self.process.finished.connect(self.on_finished)
    
    # 2. Start the process.
    
    def run_command(self):
        self.button.setDisabled(True)
        self.text_edit.clear()
        self.process.start(sys.executable, ['-u', '-c', script_text])

    def on_stdout(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.text_edit.append(output.rstrip())
        
    def on_stderr(self):
        output = self.process.readAllStandardError().data().decode()
        self.text_edit.append(output.rstrip())
        
    def on_error_occurred(self):
        self.text_edit.append(self.process.errorString())
        self.button.setEnabled(True)
    
    # 3. Write the predefined input values.
    
    def on_state_changed(self, state):
        if state == QProcess.ProcessState.Running:
            for arg in input_args:
                bytes_written = self.process.write(arg)
                if bytes_written == -1:
                    print(self.process.errorString())
            self.process.closeWriteChannel()
        
    def on_finished(self):
        self.button.setEnabled(True)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
