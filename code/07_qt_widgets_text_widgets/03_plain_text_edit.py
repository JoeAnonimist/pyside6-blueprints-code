# The QPlainTextEdit class provides a widget 
# that is used to edit and display plain text.

import sys
from PySide6.QtCore import Slot
from PySide6.QtGui import QFontDatabase, QTextCursor
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QPlainTextEdit, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the plain text edit widget
        #     and set its font and wrap mode.
        
        self.editor = QPlainTextEdit()
        self.editor.setLineWrapMode(
            QPlainTextEdit.LineWrapMode.NoWrap)
        mono = QFontDatabase.systemFont(
            QFontDatabase.SystemFont.FixedFont)
        mono.setPointSize(9)
        self.editor.setFont(mono)
        
        # Labels displaying document stats.
        
        self.charcount_label = QLabel()
        self.position_label = QLabel()
        
        layout.addWidget(self.editor)
        layout.addWidget(self.charcount_label)
        layout.addWidget(self.position_label)
        
        # 3. Connect the signals to the slots
        self.editor.textChanged.connect(self.update_char_count)
        self.editor.cursorPositionChanged.connect(self.update_position)
        
        self.editor.setPlainText(
            'MAX_POSITION = 5000\n'
            'MAX_ORDER_SIZE = 1000\n'
            'BLOCK_AFTER = 15:30\n')
        self.editor.moveCursor(QTextCursor.MoveOperation.End)
    
    # 2. Get the underlying QTextDocument properties
    #    Character count is directly available.
    #    Cursor position needs to be calculated.
    
    @Slot()        
    def update_char_count(self):
        char_count = self.editor.document().characterCount()
        self.charcount_label.setText(f'Char count: {char_count}')
    
    @Slot()
    def update_position(self):
        
        cursor = self.editor.textCursor()
        x = str(cursor.block().blockNumber() + 1)
        y = str(cursor.positionInBlock() + 1)
        
        self.position_label.setText(f'Line: {x} Column: {y}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
