# The QDial class provides a rounded range control

import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication, QLabel,
    QWidget, QVBoxLayout, QDial, QProgressBar)


class Window(QWidget):
    
    PRINCIPAL = 10000
    YEARS = 20
    LABEL_STYLE = '''
        font-size: 18px;
        font-weight: bold;
    '''
    
    def __init__(self):

        super().__init__()
        self.resize(400, 250)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the dial
        
        self.dial = QDial()
        self.dial.setRange(-5, 15)
        self.dial.setValue(7)
        self.dial.setNotchesVisible(True)
        self.dial.setFixedSize(150, 150)
        
        self.progress = QProgressBar()
        self.progress.setRange(0, 165000)
        self.progress.setTextVisible(False)
        
        self.label = QLabel()
        self.label.setStyleSheet(Window.LABEL_STYLE)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        layout.addWidget(self.dial,
            alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.progress)
        layout.addWidget(self.label)
        
        # 3. Connect the signal the slot
        
        self.dial.valueChanged.connect(self.update_projection)
        self.update_projection(self.dial.value())
    
    # 2.Create the slot. 
    
    @Slot(int)    
    def update_projection(self, value):
        
        growth_factor = 1 + value / 100
        balance = Window.PRINCIPAL * (growth_factor ** Window.YEARS)
        
        self.progress.setValue(int(balance))
        self.label.setText(
            f'Annual Rate: {value}%\n\n'
            f'Initial Investment: ${Window.PRINCIPAL:,.2f}\n'
            f'After {Window.YEARS} years:\n'
            f'${balance:,.2f}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
