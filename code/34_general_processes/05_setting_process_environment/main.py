import sys
from PySide6.QtCore import QProcess, QProcessEnvironment
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout, QCheckBox, QTextEdit)

class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        # 1. Get the system environment.
        
        self.env = QProcessEnvironment.systemEnvironment()

        self.executable = sys.executable
        self.arguments = 'testapp.py'
        
        self.style_checkbox = QCheckBox('Override style (Windows)')
        self.scale_checkbox = QCheckBox('Change scale factor (1.5x)')
        self.button = QPushButton('Run Test App')
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        
        self.style_checkbox.checkStateChanged.connect(
            self.update_environment)
        self.scale_checkbox.checkStateChanged.connect(
            self.update_environment)        
        self.button.clicked.connect(self.run_process)

        layout = QVBoxLayout(self)
        layout.addWidget(self.style_checkbox)
        layout.addWidget(self.scale_checkbox)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

        self.process = QProcess(self)

        self.process.readyReadStandardOutput.connect(self.log_output)
        self.process.readyReadStandardError.connect(self.log_output)
        self.process.errorOccurred.connect(
            lambda: print(f'Error: {self.process.errorString()}'))
        self.process.finished.connect(
            lambda: self.button.setEnabled(True))
    
    # 2. Update environment variables.
    
    def update_environment(self):

        if self.style_checkbox.isChecked():
            self.env.insert('QT_STYLE_OVERRIDE', 'windows')
        else:
            self.env.remove('QT_STYLE_OVERRIDE')
        if self.scale_checkbox.isChecked():
            self.env.insert('QT_SCALE_FACTOR', '1.5')
        else:
            self.env.remove('QT_SCALE_FACTOR')
        
        # 3. Apply the environment to the process.    
        
        self.process.setProcessEnvironment(self.env)
    
    def run_process(self):
        self.button.setDisabled(True)
        self.output.clear()
        self.output.append(f'Running process: {self.executable}\n')
        self.process.start(self.executable, [self.arguments])

    def log_output(self):
        stdout = self.process.readAllStandardOutput().data().decode()
        stderr = self.process.readAllStandardError().data().decode()
        if stdout:
            self.output.append(f'stdout: {stdout}\n')
        if stderr:
            self.output.append(f'stderr: {stderr}\n')


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
