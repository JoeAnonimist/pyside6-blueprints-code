import sys
from PySide6.QtWidgets import (QApplication, QWidget,
    QGroupBox, QVBoxLayout, QPushButton, QLineEdit)


class MainWindow(QWidget):
    
    def __init__(self):
        
        super().__init__()

        layout = QVBoxLayout(self)

        self.group1 = QGroupBox('Group 1')
        self.group1.setObjectName('Groupbox 1')
        self.group1.setLayout(QVBoxLayout())
        self.line_edit1 = QLineEdit()
        self.group1.layout().addWidget(self.line_edit1)
        layout.addWidget(self.group1)
        
        self.clear_button = QPushButton('Clear text')
        self.clear_button.clicked.connect(self.line_edit1.clear)
        self.group1.layout().addWidget(self.clear_button)

        self.group2 = QGroupBox('Group 2')
        self.group2.setObjectName('Groupbox 2')
        self.group2.setLayout(QVBoxLayout())
        self.line_edit2 = QLineEdit()
        self.line_edit2.setDisabled(True)
        self.group2.layout().addWidget(self.line_edit2)
        layout.addWidget(self.group2)

        self.move_button = QPushButton('Move Clear Button')
        layout.addWidget(self.move_button)
        self.move_button.clicked.connect(self.move_widget)

    def move_widget(self):
        
        # 1. Adjust any state/side-effects
        
        old_parent = self.clear_button.parent()
        
        if old_parent == self.group1:
            self.line_edit1.setDisabled(True)
            self.line_edit2.setEnabled(True)
            self.clear_button.clicked.disconnect(self.line_edit1.clear)
            self.clear_button.clicked.connect(self.line_edit2.clear)
            new_parent = self.group2
        else:
            self.line_edit2.setDisabled(True)
            self.line_edit1.setEnabled(True)
            self.clear_button.clicked.disconnect(self.line_edit2.clear)
            self.clear_button.clicked.connect(self.line_edit1.clear)
            new_parent = self.group1
            
        # 2. Transfer ownership

        new_parent.layout().addWidget(self.clear_button)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
