#  The QStatusBar class provides a horizontal bar 
# suitable for presenting status information. 

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QMainWindow, QTextEdit, QLabel)

class Editor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Editor')
        self.resize(500, 300)
        self.text_edit = QTextEdit()        
        self.setCentralWidget(self.text_edit)
        self.position_label = QLabel()
        self.charcount_label = QLabel()
        self.statusBar().addWidget(self.position_label)
        self.statusBar().addPermanentWidget(self.charcount_label)
        
        self.text_edit.textChanged.connect(self.update_stats)
        self.text_edit.selectionChanged.connect(
            self.show_selection_size)
    
    @Slot()
    def update_stats(self):
        cursor = self.text_edit.textCursor()
        size = self.text_edit.document().characterCount()
        x = str(cursor.blockNumber() + 1)
        y = str(cursor.columnNumber() + 1)
        self.position_label.setText(f'Ln: {x}, Col: {y}')
        self.charcount_label.setText(f'Chars: {size}')        
    
    @Slot()
    def show_selection_size(self):
        cursor = self.text_edit.textCursor()
        count = len(cursor.selectedText())
        msg = f'{count} characters selected'
        self.statusBar().showMessage(msg, 2000)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())
