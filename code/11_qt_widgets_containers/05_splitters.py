# The QSplitter class implements a splitter widget.
# A splitter lets the user control the size of 
# child widgets by dragging the boundary between them. 
# Any number of widgets may be controlled by a single splitter. 

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QSplitter, QGroupBox, QRadioButton)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create a splitter
        
        self.splitter = QSplitter()
        
        # 2 - Create widgets
        #     In this case it's three groupboxes
        
        groupbox_1 = QGroupBox('Orientation')
        groupbox_1.setLayout(QVBoxLayout())
        
        # The radio buttons are just to demonstrate
        # splitter orientation. I don't think changing
        # splitter orientation at run time is that common.
        
        self.button_horizontal = QRadioButton('Horizontal')
        self.button_horizontal.setChecked(True)
        self.button_vertical = QRadioButton('Vertical')
        
        self.button_horizontal.toggled.connect(self.on_toggled)
        self.button_vertical.toggled.connect(self.on_toggled)
        
        groupbox_1.layout().addWidget(self.button_horizontal)
        groupbox_1.layout().addWidget(self.button_vertical)
        
        groupbox_2 = QGroupBox('group box 2')
        groupbox_3 = QGroupBox('group box 3')
        
        # 3 - Add widgets to the splitter
        
        self.splitter.addWidget(groupbox_1)
        self.splitter.addWidget(groupbox_2)
        self.splitter.addWidget(groupbox_3)
        
        layout.addWidget(self.splitter)
        
    def on_toggled(self):
        
        if self.button_horizontal.isChecked():
            self.splitter.setOrientation(
                Qt.Orientation.Horizontal)
        else:
            self.splitter.setOrientation(
                Qt.Orientation.Vertical)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
