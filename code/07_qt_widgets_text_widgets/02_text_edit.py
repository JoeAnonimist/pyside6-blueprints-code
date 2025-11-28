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
        
        self.src = QTextEdit()
        self.src.textChanged.connect(self.update_preview)

        mono = QFontDatabase.systemFont(
            QFontDatabase.SystemFont.FixedFont)
        mono.setPointSize(11)
        self.src.setFont(mono)
        
        # 2. Create the preview textedit instance
        
        self.preview = QTextEdit()
        self.preview.setReadOnly(True)
        self.preview.setStyleSheet('background-color: #f0f0f0;')
        
        layout.addWidget(self.src)
        layout.addWidget(self.preview)

        self.src.setText('### Enter Markdown Text\n\n')

    # 3. Implement the slot to preview the entered text

    @Slot()
    def update_preview(self):
        markdown_text = self.src.toPlainText()
        self.preview.setMarkdown(markdown_text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
