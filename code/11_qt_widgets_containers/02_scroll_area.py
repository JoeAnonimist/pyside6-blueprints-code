# The QScrollArea class provides a 
# scrolling view onto another widget

import sys

from PySide6.QtGui import QTextOption
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QScrollArea, QPlainTextEdit)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the scroll area
        
        scroll_area = QScrollArea()
        
        # 2 - Create the widget that needs to be scrolled
        
        text_edit = QPlainTextEdit()
        text_edit.setWordWrapMode(QTextOption.WrapMode.NoWrap)

        # 3 - Add the widget to the scroll area

        scroll_area.setWidget(text_edit)
        
        # Use this if you want the inner widget to 
        # get resized together with the scroll area.
        
        scroll_area.setWidgetResizable(True)
        
        layout.addWidget(scroll_area)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
