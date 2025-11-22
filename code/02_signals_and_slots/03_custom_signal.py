import sys

# 1. Import the Signal class

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)

# 2. Declare the signal

class CounterButton(QPushButton):
    
    counterChanged = Signal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.counter = 0        
        self.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.counter += 1
        self.counterChanged.emit(self.counter)


class Window(QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = CounterButton('Click me!')
        
        # 3. Use the signal
        
        self.button.clicked.connect(self.on_button_clicked)
        self.button.counterChanged.connect(self.on_counter_changed)
        
        layout.addWidget(self.button)
        
    @Slot()
    def on_button_clicked(self):
        print('Button clicked')
    
    @Slot()
    def on_counter_changed(self, counter):
        print('Counter: ', counter)
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
