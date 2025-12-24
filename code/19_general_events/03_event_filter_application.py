import sys

from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import (QApplication, QWidget, 
    QPushButton, QVBoxLayout)


# 1. Create the event filter class.

class MousePressFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print('Filter mouse press for: ', watched.objectName())
            if isinstance(watched, QPushButton):
                if not watched.isEnabled():
                    watched.clicked.emit()
                    return True
        return super().eventFilter(watched, event)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setObjectName('Main Window')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button1 = QPushButton('Button 1')
        button1.setObjectName('button1')
        button1.clicked.connect(self.on_button_clicked)
        
        button2 = QPushButton('Button 2')
        button2.setObjectName('button2')
        button2.clicked.connect(self.on_button_clicked)
        button2.setDisabled(True)
        
        button3 = QPushButton('Button 3')
        button3.setObjectName('button3')
        button3.clicked.connect(self.on_button_clicked)
        
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addStretch()
        
    def on_button_clicked(self):
        print('Button clicked: ', self.sender().objectName())
      

if __name__ == '__main__':

    app = QApplication(sys.argv)
    
    # 2. Instantiate the event filter object.
    
    filter_obj = MousePressFilter(app)
    
    # 3. Install the event filter on the application.
    
    app.installEventFilter(filter_obj)

    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
