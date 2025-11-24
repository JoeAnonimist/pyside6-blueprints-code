# Signals are event notifications.
# Slots are Python methods/functions.
# A QPushButton is a button that you can push.

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the signal sender, ie. the QPushButton.
        #     When you click it the button emits a signal.
        
        button = QPushButton('Click me!')
        
        # 3 - Connect the signal and the slot.
        #     Notice there's no parentheses after self.on_button_clicked
        #     This means you pass a Python function object
        #     to the connect() method
        
        button.clicked.connect(self.on_button_clicked)
        
        layout.addWidget(button)
        
    # 2 - Create the slot. It's a simple method
    #     that belongs to our Window class.
    #     What ever code you put here is
    #     executed when the button is clicked.
    
    @Slot(bool)
    def on_button_clicked(self, checked):
        print('Button clicked,', 'checked:', checked)
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
