import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QLabel, QVBoxLayout, QGridLayout)


KEYS = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('*', 3, 0), ('0', 3, 1), ('#', 3, 2)
]


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.display_label = QLabel()
        font = self.display_label.font()
        font.setPointSize(16)
        font.setBold(True)
        self.display_label.setFont(font)
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.display_label)
        
        # 1. Create a QGridLayout`.
        
        keypad_layout = QGridLayout()
        
        for key, row, col in KEYS:
            
            # 2. Create the buttons.
            
            button = QPushButton(key)
            button.setFixedSize(60, 40)
            
            button.clicked.connect(
                lambda checked, key=key: 
                    self.update_display(key))
            
            # 3. Add each button to the grid.
            
            keypad_layout.addWidget(button, row, col)
            
        layout.addLayout(keypad_layout)
        
    def update_display(self, key):
        if key == '*':
            self.display_label.clear()
        elif key == '#':
            self.display_label.setText('DONE')
        else:
            text = self.display_label.text()
            if text == 'DONE':
                text = ''
            self.display_label.setText(text + key)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
