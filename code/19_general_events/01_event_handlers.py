import sys
from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.label = QLabel('Hello, events!')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
    
    # Centralized event handler
    
    def event(self, event):
        if event.type() == QEvent.Type.KeyPress:
            print(f'Intercepted key pressed: {event.text()}')
            #return True
        if event.type() == QEvent.Type.Show:
            print('Intercepted show event')
            #return True
        return super().event(event)
    
    # Specialized event handlers
    
    # 1. Extend the keyPressEvent() method
    
    def keyPressEvent(self, event):
        if event.text() == 'q':
            print(f'isAccepted: {event.isAccepted()}')
            self.label.setText('q pressed')
        else:
            self.label.clear()
            super().keyPressEvent(event)
    
    # 2. Extend the showEvent() method
    
    def showEvent(self, event):
        self.label.setText('Added to visible windows list')
        super().showEvent(event)
    
    # 3. Extend the hideEvent() method.
    
    def hideEvent(self, event):
        self.label.clear()
        print('Removed from visible windows list')
        super().hideEvent(event)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())