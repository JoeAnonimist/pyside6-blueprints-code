import sys
import re
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit)


class Window(QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.pattern = \
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        layout.addWidget(QLabel('Email:'))
        
        # 1. Add the widget to be styled.
        
        self.email_edit = QLineEdit()
        self.email_edit.textChanged.connect(self.validate_email)
        layout.addWidget(self.email_edit)

        self.status_label = QLabel()
        layout.addWidget(self.status_label)
        
        # 2. Set the style sheet.
        
        self.setStyleSheet('''
            QLineEdit { }
            QLineEdit[isValid="true"] { border: 2px solid green; }
            QLineEdit[isValid="false"] { border: 2px solid red; }
        ''')
        
    @Slot(str)
    def validate_email(self, text):
        
        print(f'isValid exists: {self.email_edit.property("isValid")}')
        
        # 3. Set a dynamic property to trigger conditional widget styling.
        
        if not text:
            self.status_label.clear()
            self.email_edit.setProperty('isValid', None)
        else:
            if re.fullmatch(self.pattern, text):
                valid = True
                self.status_label.setText('Valid!')
            else:
                valid = False
                self.status_label.setText('Invalid email.')
    
            self.email_edit.setProperty('isValid', valid)

        self.email_edit.style().unpolish(self.email_edit)
        self.email_edit.style().polish(self.email_edit)
        self.email_edit.update()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
