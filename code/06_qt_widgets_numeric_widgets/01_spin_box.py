# The QSpinBox class provides a spin box widget.
# Access the current value using its value property

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QSpinBox, QLabel)


class Window(QWidget):
    
    LABEL_STYLE = '''
        font-size: 18px;
        font-weight: bold;
    '''
    
    def __init__(self):

        super().__init__()
        self.resize(400, 250)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 1 - Create the spinbox and set its properties
        
        self.spinbox = QSpinBox()

        # Set valid limit sizes: from $0
        # to $100,000 in steps of $1,000.
        
        self.spinbox.setRange(0, 100000)
        self.spinbox.setSingleStep(1000)
        self.spinbox.setValue(1000)     # initial value
        self.spinbox.setPrefix('$ ')    # visual unit
        
        layout.addWidget(self.spinbox)

        self.label = QLabel()
        self.label.setText(f'Monthly budget limit: $1,000')
        self.label.setStyleSheet(Window.LABEL_STYLE)
        layout.addWidget(self.label)
        
        # 3. Connect the valueChanged signal with the slot
        
        self.spinbox.valueChanged.connect(self.set_limit)
    
    # 2. Create the slot. The value passed
    #    from the signal is an integer. 
    
    @Slot(int)    
    def set_limit(self, value):
        self.label.setText(f'Monthly budget limit: ${value:,}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
