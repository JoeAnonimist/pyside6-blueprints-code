# A script that just displays
# an empty Qt6 window

import sys
from PySide6.QtWidgets import QApplication, QWidget


# 1 - Create a class inherited from QWidget

class Window(QWidget):

    def __init__(self):

        # If you don't init the superclass 
        # you get a run-time error
        super().__init__()
    

if __name__ == '__main__':
    
    # 2 - Create an instance of the QApplication class
    #     Make sure there isn't one already running.
    
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    # 3 - Create an instance of the Window class
    #     and show() it
    
    main_window = Window()
    main_window.show()
    
    # 4 - Start receiving events
    
    sys.exit(app.exec())
