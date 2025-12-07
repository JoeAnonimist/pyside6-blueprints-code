import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLineEdit, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.show_button = QPushButton('Show widgets')
        self.show_button.clicked.connect(self.show_widgets)
        layout.addWidget(self.show_button)
        
        self.switch_button = QPushButton('Switch QLineEdit parent')
        self.switch_button.clicked.connect(self.switch_parent)
        self.switch_button.setDisabled(True)
        layout.addWidget(self.switch_button)
        
        # 1. Create two top-level windows
        
        self.widget1 = QWidget()
        self.widget1.setObjectName('Widget 1')
        self.widget1.setLayout(QVBoxLayout())
        self.widget1.setWindowTitle('Widget 1')
        self.widget1.resize(200, 80)
        
        self.widget2 = QWidget()
        self.widget2.setObjectName('Widget 2')
        self.widget2.setLayout(QVBoxLayout())
        self.widget2.setWindowTitle('Widget 2')
        self.widget2.resize(200, 80)
        
        # 2. Create the child widget
        
        self.edit = QLineEdit()
        self.widget1.layout().addWidget(self.edit)

    def show_widgets(self):
        self.show_button.setDisabled(True)
        self.switch_button.setEnabled(True)
        self.widget1.show()
        self.widget2.show()
    
    # 3. Switch child widget parent on button click.
    
    def switch_parent(self):

        self.edit.parent().layout().removeWidget(self.edit)
        if self.edit.parent() == self.widget1:
            self.edit.setParent(self.widget2)
        else:
            self.edit.setParent(self.widget1)
        
        self.edit.parent().layout().addWidget(self.edit)
        self.edit.setText(f' Parent: {self.edit.parent().objectName()}')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
