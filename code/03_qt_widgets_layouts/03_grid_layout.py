# QGridLayout lays out widgets, well, in a grid

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QLabel, QGridLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # 1 - Create the layout:
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        # 2 - Create widgets and add them to the grid
        # We create sixteen buttons in a 4x4 grid
        # (0, 0) is the top left cell
        # The first integer is the row number
        # The second integer is the column number
        
        for r in range(4):
            for c in range(4):
                
                button = QPushButton(f'Button {r}, {c}')
                button.clicked.connect(self.on_button_clicked)
                self.layout().addWidget(button, r, c)

        # The label is put in row 4, column 0
        # and spans one row and four columns. 

        self.label = QLabel()
       
        layout.addWidget(self.label, 4, 0, 1, 4)
        
    # The slot method

    @Slot()    
    def on_button_clicked(self):
        
        # Get a reference to the clicked button
        # and its position in the grid view

        clicked_button = self.sender()

        index = self.layout().indexOf(clicked_button)
        position = self.layout().getItemPosition(index)
        r, c, _, _ = position
        self.label.setText(f'Row: {r}, Column: {c}')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())