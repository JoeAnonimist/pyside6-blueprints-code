
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit


# 1. Create a QMainWindow subclass.

class Editor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle('Financial Memo Editor')
        self.resize(500, 300)
        
        # 2. Create a central widget.
        
        text_edit = QTextEdit()
        
        # 3. Set the main window central widget.
        
        self.setCentralWidget(text_edit)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())
