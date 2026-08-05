# The QScrollArea class provides a 
# scrolling view onto another widget

import sys

from PySide6.QtGui import QTextOption
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QScrollArea, QPlainTextEdit)


MEMO_TEXT = (
    'Monthly retainer payment for ongoing bookkeeping services.\n'
    'Same terms as the original engagement letter.\n'
    'Continue at this amount until further notice.\n'
    'No action needed unless the invoice changes '
    'or the vendor updates their banking details.\n'
    'Reach out to accounts payable if a payment is ever skipped.')


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the scroll area.
        
        scroll_area = QScrollArea()
        
        # 2. Create the widget that needs to be scrolled.
        
        memo_field = QPlainTextEdit()
        memo_field.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        memo_field.setPlainText(MEMO_TEXT)

        # 3. Add the widget to the scroll area.

        scroll_area.setWidget(memo_field)
        scroll_area.setWidgetResizable(True)
        
        layout.addWidget(scroll_area)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
