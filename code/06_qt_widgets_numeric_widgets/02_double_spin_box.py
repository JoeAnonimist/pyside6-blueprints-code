# QDoubleSpinBox provides a
# spin box widget that takes doubles.

import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QDoubleSpinBox, QLabel)


class Window(QWidget):
    
    PRINCIPAL = 10000
    
    LABEL_STYLE = '''
        font-size: 18px;
        font-weight: bold;
    '''
    
    def __init__(self):

        super().__init__()
        self.resize(400, 250)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the spinbox and set its properties
        
        self.spinbox = QDoubleSpinBox()
        self.spinbox.setRange(0, 15)
        self.spinbox.setDecimals(2)
        self.spinbox.setSingleStep(0.05)
        self.spinbox.setSuffix(' %')
        self.spinbox.setValue(4.50)

        # 3. Connect the valueChanged signal with the slot

        self.spinbox.valueChanged.connect(self.calculate_earnings)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(Window.LABEL_STYLE)
        
        layout.addWidget(self.spinbox)
        layout.addWidget(self.label)
        
        self.calculate_earnings(self.spinbox.value())
    
    # 2. Create a slot to handle its valueChanged signals.
    
    @Slot(float)
    def calculate_earnings(self, value):
        earnings = Window.PRINCIPAL * (value / 100)
        self.label.setText(
            f'First year earnings on ${Window.PRINCIPAL:,.2f}:\n'
            f' ${earnings:,.2f}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
