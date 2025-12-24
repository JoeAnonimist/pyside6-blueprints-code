import sys

from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)

# 1. Create a class and implement its eventFilter() method.

class MousePressFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            print('Filter mouse press for: ', watched.objectName())
            if watched.objectName() == 'button2':
                return True
        return super().eventFilter(watched, event)


class Window(QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button1 = QPushButton('Button 1')
        button1.setObjectName('button1')
        button2 = QPushButton('Button 2')
        button2.setObjectName('button2')
        button3 = QPushButton('Button 3')
        button3.setObjectName('button3')
        
        # 2. Create the event filter object.
        
        event_filter = MousePressFilter(self)
        
        # 3. Install the event filter for the target objects.
        
        button1.installEventFilter(event_filter)
        button2.installEventFilter(event_filter)
        button3.installEventFilter(event_filter)
        
        button1.clicked.connect(self.on_button_clicked)
        button2.clicked.connect(self.on_button_clicked)
        button3.clicked.connect(self.on_button_clicked)
        
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addStretch()
        
    def on_button_clicked(self):
        print('Button clicked: ', self.sender().objectName())
      

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
