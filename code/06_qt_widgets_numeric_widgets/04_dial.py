# The QDial class provides a rounded range control

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QDial, QProgressBar)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the dial
        
        self.dial = QDial()
        self.dial.setRange(0, 100)
        self.dial.setValue(50)
        self.dial.setNotchesVisible(True)
        
        self.volume_bar = QProgressBar()
        self.volume_bar.setFormat('%v%')
        self.volume_bar.setValue(self.dial.value())
        
        layout.addWidget(self.dial)
        layout.addWidget(self.volume_bar)
        
        # 3. Connect the signal the slot
        
        self.dial.valueChanged.connect(self.set_volume)
    
    # 2.Create the slot. 
    
    @Slot(int)    
    def set_volume(self, value):
        self.volume_bar.setValue(value)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
