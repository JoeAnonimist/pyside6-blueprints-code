import sys
from PySide6.QtWidgets import QApplication, QWidget

# 1 - Create a class inherited from QWidget

class Window(QWidget):

    def __init__(self):

        # If you don't init the superclass 
        # you get a run-time error
        super().__init__()
        self.resize(300, 120)
    

if __name__ == '__main__':
    
    # 2 - Create an instance of the QApplication class

    app = QApplication(sys.argv)

    # 3 - Create an instance of the Window class
    #     and show() it
    
    main_window = Window()
    main_window.show()
    
    # 4 - Start receiving events
    
    sys.exit(app.exec())
