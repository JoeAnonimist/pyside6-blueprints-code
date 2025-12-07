import sys
from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QGroupBox, QCheckBox, QLineEdit, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.groupbox = QGroupBox()
        gb_layout = QVBoxLayout()
        self.groupbox.setLayout(gb_layout)
        layout.addWidget(self.groupbox)
        
        # 1. Create the checkboxes
        
        self.checkbox1 = QCheckBox('checkbox1')
        self.checkbox1.setObjectName('checkbox1')
        gb_layout.addWidget(self.checkbox1)
        
        self.checkbox2 = QCheckBox('checkbox2')
        self.checkbox2.setObjectName('checkbox2')
        gb_layout.addWidget(self.checkbox2)
        
        self.checkbox3 = QCheckBox('checkbox3')
        self.checkbox3.setObjectName('checkbox3')
        gb_layout.addWidget(self.checkbox3)
        
        self.find_button = QPushButton('Find child')
        self.find_button.clicked.connect(self.find_widget)
        layout.addWidget(self.find_button)
        
        self.edit = QLineEdit()
        layout.addWidget(self.edit)
        
    def find_widget(self):
        
        # 2. Find the checkboxes.
        
        pattern = self.edit.text()
        regexp = QRegularExpression(pattern)
        children = self.groupbox.findChildren(QCheckBox, regexp)
        
        # 3. Set the checkboxes state to checked
        
        if len(children) > 0:
            for child in children:
                child.setCheckState(Qt.CheckState.Checked)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
