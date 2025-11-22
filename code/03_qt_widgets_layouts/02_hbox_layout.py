# QHBoxLayout is the horizontal box layout
# It lines out widgets horizontally

import sys

from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QLabel, QHBoxLayout)
from PySide6.QtCore import QTime




class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # The steps are the same as for the vertical box layout:
        # 1 - Create the layout and set it as the window layout
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # 2 - Create some widgets
        #     I add a button and a label for variety purposes
        
        button = QPushButton("What's the time?")
        self.label = QLabel('')
        self.label.setMinimumWidth(60)
        
        # I need to access the label from the 
        # slot method (ie. on_button_clicked)
        # so I make it a Window instance variable.
        # I also set the label minimum width
        
        
        # 3 - Add widgets to the layout
        
        layout.addWidget(button)
        layout.addWidget(self.label)
        
        # connect button.clicked to a slot
        # to check if everything works
        
        button.clicked.connect(self.on_button_clicked)
        

    def on_button_clicked(self):
        
        # You can use the QtCore.QTime class
        # to get the current time
        
        self.label.setText(QTime.currentTime().toString('hh:mm:ss'))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())