import sys
from PySide6.QtCore import QObject, QEvent, Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QGroupBox, QVBoxLayout, QLineEdit, QLabel, QCheckBox)


# 1. Create the event filter class.

class EventFilter(QObject):
    
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print('Log: mouse pressed in ', watched.objectName())
        if event.type() == QEvent.Type.KeyPress:
            print('Log: key pressed in ', watched.objectName())
        return super().eventFilter(watched, event)

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName('MainWindow')

        layout = QVBoxLayout(self)

        self.outer_groupbox = QGroupBox('Outer GroupBox')
        self.outer_groupbox.setObjectName('outer_groupbox')
        self.outer_groupbox.setLayout(QVBoxLayout())

        self.inner_groupbox = QGroupBox('Inner GroupBox')
        self.inner_groupbox.setObjectName('inner_groupbox')
        self.inner_groupbox.setLayout(QVBoxLayout())
        self.outer_groupbox.layout().addWidget(self.inner_groupbox)
        
        # 3. Create the user registration form.

        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText('User name')
        self.username_edit.setObjectName('line_edit')
        self.username_edit.textChanged.connect(self.update_email)
        self.inner_groupbox.layout().addWidget(self.username_edit)
        
        self.email_label = QLabel()
        self.email_label.setObjectName('label')
        self.email_label.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.email_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByKeyboard |
            Qt.TextInteractionFlag.TextSelectableByMouse)
        self.inner_groupbox.layout().addWidget(self.email_label)
        
        self.email_checkbox = QCheckBox('Enable email notifications')
        self.email_checkbox.setObjectName('checkbox')
        self.inner_groupbox.layout().addWidget(self.email_checkbox)

        layout.addWidget(self.outer_groupbox)
        layout.addStretch()
        
    def update_email(self, text):
        if text:
            self.email_label.setText(f'{text}@domain.com')
        else:
            self.email_label.clear()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    # 2. Instantiate and install the filter.
    
    event_filter = EventFilter(app)
    app.installEventFilter(event_filter)
    
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
