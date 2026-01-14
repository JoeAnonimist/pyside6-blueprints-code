import sys
from PySide6.QtWidgets import (QApplication,
    QMainWindow, QTextEdit)

class Editor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Editor')
        self.resize(500, 300)
        text_edit = QTextEdit()        
        self.setCentralWidget(text_edit)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())
