import sys
from html import escape
from PySide6.QtWidgets import (QApplication, QVBoxLayout,
    QWidget, QLineEdit, QTextBrowser)
from PySide6.QtCore import QProcess


class Window(QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self.output_browser = QTextBrowser()
        layout.addWidget(self.output_browser)

        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText(
            'Enter Python code and press Enter to execute it:')
        self.input_line.returnPressed.connect(self.send_input)
        self.input_line.setEnabled(False)
        layout.addWidget(self.input_line)
        
        self.stdout_buffer = ''
        self.stderr_buffer = ''
        
        # 1. Create the process,
        #    connect the signals, and start it.
        
        self.process = QProcess(self)
        self.process.started.connect(self.on_started)
        self.process.errorOccurred.connect(self.on_error_occurred)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)

        self.process.start(sys.executable, ['-u', '-i', '-q'])

    def on_started(self):
        
        self.output_browser.append(
            'Embedded Python repl ready.\n'
            'Type Python code and press Enter.\n')
        self.input_line.setEnabled(True)
        self.input_line.setFocus()
    
    def on_error_occurred(self):
        self.output_browser.append(
            '<font color="red">Failed to start Python</font>')
    
    # 2. Send user input to the process.
    
    def send_input(self):
        
        if self.process.state() != QProcess.ProcessState.Running:
            return

        command = self.input_line.text()
        self.output_browser.append(f'>>> {command}')
        self.process.write((command + '\n').encode())
        self.input_line.clear()
    
    # 3. Handle the process output.
    
    def handle_stdout(self):
        
        data = self.process.readAllStandardOutput().data()
        text = data.decode('utf-8', errors='replace')
        self.stdout_buffer += text
        while '\n' in self.stdout_buffer:
            line, remainder = self.stdout_buffer.split('\n', 1)
            self.stdout_buffer = remainder
            self.output_browser.append(line.rstrip('\r'))

    def handle_stderr(self):

        data = self.process.readAllStandardError().data()
        text = data.decode('utf-8', errors='replace')
        self.stderr_buffer += text
        while '\n' in self.stderr_buffer:
            line, remainder = self.stderr_buffer.split('\n', 1)
            self.stderr_buffer = remainder
            stripped_line = line.rstrip('\r')
            self.output_browser.append(
                f'<font color="red">{stripped_line}</font>')
    
    # 4. Terminate the process
    
    def closeEvent(self, event):

        if self.process.state() == QProcess.ProcessState.Running:
            self.process.write(b'exit()\n')
            self.process.waitForFinished(100)
            if self.process.state() == QProcess.ProcessState.Running:
                self.process.kill()
                self.process.waitForFinished()
        super().closeEvent(event)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
