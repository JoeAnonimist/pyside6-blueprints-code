# The QSpinBox class provides a spin box widget.
# Access the current value using its value property

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QSpinBox, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the spinbox and set its properties
        
        self.spinbox = QSpinBox()
        self.spinbox.setSuffix(' GB')    # visual unit
        self.spinbox.setValue(32)        # initial value
        
        # Set valid RAM sizes: from 16 GB
        # to 256 GB in steps of 2 GB.
        
        self.spinbox.setRange(16, 256)
        self.spinbox.setSingleStep(2)
        layout.addWidget(self.spinbox)

        self.label = QLabel()
        self.label.setText('RAM: 32 GB')
        layout.addWidget(self.label)
        
        # 3. Connect the valueChanged signal with the slot
        
        self.spinbox.valueChanged.connect(self.set_ram)
    
    # 2. Create the slot. The value passed
    #    from the signal is an integer. 
    
    @Slot(int)    
    def set_ram(self, value):
        self.label.setText(f'RAM: {value} GB')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
