import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        self.resize(300, 120)
        
        # 1. Create a layout and
        #    set it as the window's layout.
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 2. Create a QLabel instance
        #    and add it to the window layout.
        
        label = QLabel('Hello, World!')
        layout.addWidget(label)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
