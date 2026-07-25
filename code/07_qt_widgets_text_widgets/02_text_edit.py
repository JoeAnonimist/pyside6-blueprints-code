# The QTextEdit class provides a widget that is used 
# to edit and display both plain and rich text.

import sys
from PySide6.QtCore import Slot
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import (QApplication,
    QWidget, QHBoxLayout, QTextEdit)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the source textedit instance
        
        self.src_edit = QTextEdit()
        self.src_edit.textChanged.connect(self.update_preview)

        mono = QFontDatabase.systemFont(
            QFontDatabase.SystemFont.FixedFont)
        mono.setPointSize(9)
        self.src_edit.setFont(mono)
        
        # 2. Create the preview textedit instance
        
        self.preview_edit = QTextEdit()
        self.preview_edit.setReadOnly(True)
        self.preview_edit.setStyleSheet('background-color: #f0f0f0;')
        
        layout.addWidget(self.src_edit)
        layout.addWidget(self.preview_edit)

        self.src_edit.setText('### Monthly Budget Report Notes\n\n')

    # 3. Implement the slot to preview the entered text

    @Slot()
    def update_preview(self):
        markdown_text = self.src_edit.toPlainText()
        self.preview_edit.setMarkdown(markdown_text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
