# Radio buttons typically present the user 
# with a "one of many" choice. In a group of radio buttons, 
# only one radio button at a time can be checked

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QRadioButton, QLabel)
import sys


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the radio buttons and add them to the layout
        
        self.blue_radiobutton = QRadioButton('Change bg to blue')
        self.green_radiobutton = QRadioButton('Change bg to green')
        self.red_radiobutton = QRadioButton('Change bg to red')
        
        self.label = QLabel('Colored label')
        
        layout.addWidget(self.blue_radiobutton)
        layout.addWidget(self.green_radiobutton)
        layout.addWidget(self.red_radiobutton)
        layout.addWidget(self.label)
        
        # 3. Connect the radio buttons' toggled signal
        #    to the slot
        
        self.blue_radiobutton.toggled.connect(
            lambda: self.on_button_toggled('blue'))
        self.green_radiobutton.toggled.connect(
            lambda: self.on_button_toggled('green'))
        self.red_radiobutton.toggled.connect(
            lambda: self.on_button_toggled('red'))
        
        self.blue_radiobutton.setChecked(True)
    
    # 2 - Create the slot to handle radio button toggled() signal
    
    @Slot(str)    
    def on_button_toggled(self, color):
        
        self.label.setStyleSheet(
            f'background-color:{color}; color: white;')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())