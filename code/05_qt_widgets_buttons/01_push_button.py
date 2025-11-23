# QPushButton generates 'clicked' signals when you click it duh

from random import randint
import sys

from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the button and add it to the window layout
        
        button = QPushButton('Generate random integer')
        
        # 3 - Connect the button clicked event with the slot
        
        button.clicked.connect(self.on_button_clicked)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(button)
        layout.addWidget(self.label)
    
    # 2 - Create the method/function to use as the slot
    
    @Slot()
    def on_button_clicked(self):
        self.label.setNum(randint(0, 100))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
