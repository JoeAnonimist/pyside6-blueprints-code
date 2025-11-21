# Displays a Hello, World! message in QLabel

# Import QLabel and QVBoxLayout

import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)

# 1 - Create a class that inherits from QWidget

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # 2 - Set window layout
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 3 - Create a QLabel instance
        #     and add it to the window layout
        
        label = QLabel('Hello, World!')
        layout.addWidget(label)

# The boilerplate code is similar to that from helloworld.py        

if __name__ == '__main__':

    # The qApp variable points to the application
    # if it was already created so this is equivalent
    # to checking for QApplication.instance()
    app = qApp or QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
