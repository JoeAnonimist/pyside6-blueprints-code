import sys
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout)
from customwidgets import SignupWidget

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.signup_widget = SignupWidget()
        self.signup_widget.usernameChanged.connect(
            self.log_username_changes)
        layout.addWidget(self.signup_widget)
        
        # self.signup_widget.email = "This won't work."
        # self.signup_widget.username = "This won't either."
        
    def log_username_changes(self):
        print(f'First Name: {self.signup_widget.firstname}')
        print(f'Last Name: {self.signup_widget.lastname}')
        print(f'Username: {self.signup_widget.username}')
        print(f'Email: {self.signup_widget.email}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
