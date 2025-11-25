import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create QLabel objects and set their text
        
        plain_text_label = QLabel('Plain text label')
        markdown_label = QLabel('**Markdown** label')
        rich_text_label = QLabel('<b>Rich text</b> label')
        
        # 2. Optionally, set their text format

        markdown_label.setTextFormat(Qt.TextFormat.MarkdownText)
        rich_text_label.setTextFormat(Qt.TextFormat.RichText)
        
        # 3. Add the objects to the layout

        layout.addWidget(plain_text_label)
        layout.addWidget(markdown_label)
        layout.addWidget(rich_text_label)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
