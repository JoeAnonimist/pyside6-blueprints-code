import os
import sys
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QVBoxLayout, QTextEdit)


with open('subprocess_script.py', 'r') as file:
    subprocess_script = file.read()

class Window(QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.buffer = ''

        self.text_edit = QTextEdit(readOnly=True)
        self.text_edit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)

        self.run_button_naive = QPushButton('Run - Naive Chunk Handling')
        self.run_button_naive.clicked.connect(self.run_process_naive)

        self.run_button_buffered = QPushButton('Run with Buffering')
        self.run_button_buffered.clicked.connect(self.run_process_buffered)

        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.run_button_naive)
        layout.addWidget(self.run_button_buffered)

        self.process = None
        
    def set_buttons_enabled(self, enabled):
        self.run_button_naive.setEnabled(enabled)
        self.run_button_buffered.setEnabled(enabled)

    def run_process_naive(self):
        
        self.text_edit.clear()
        self.text_edit.append('Naive Chunk Handling\n\n')
        self.set_buttons_enabled(False)

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(
            self.handle_stdout_naive)
        self.process.finished.connect(self.finished_naive)
        self.process.start(sys.executable, ['-c', subprocess_script])

    def handle_stdout_naive(self):
        data = self.process.readAllStandardOutput()
        chunk = bytes(data).decode('utf-8', errors='replace')
        self.text_edit.append(chunk)
        
    def finished_naive(self):
        self.text_edit.append('\nProcess Finished')
        self.set_buttons_enabled(True)

    def run_process_buffered(self):
        
        self.text_edit.clear()
        self.text_edit.append('Buffered Chunk Handling\n\n')
        self.set_buttons_enabled(False)        
        # 1. Create a QProcess, connect the signals
        #    and run the child process.
        
        self.buffer = ''
        
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(
            self.handle_stdout_buffered)
        self.process.finished.connect(self.finished_buffered)
        self.process.start(sys.executable, ['-c', subprocess_script])
            
    def handle_stdout_buffered(self):
        
        # 2. Read the child process stdout data,
        #    decode it, and append it to the buffer
        
        data = self.process.readAllStandardOutput()
        chunk = bytes(data).decode('utf-8', errors='replace')
        self.buffer += chunk
        
        # 3. Check whether the buffer contains
        #    any complete lines and display them.
        
        lines = self.buffer.split(os.linesep)
        for line in lines[:-1]:
            self.text_edit.append(line)
        self.buffer = lines[-1]
    
    # 4. Flush any remaining content from the buffer.
    
    def finished_buffered(self):
        if self.buffer:
            self.text_edit.append(self.buffer)
        self.text_edit.append('Process Finished')
        self.set_buttons_enabled(True)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
