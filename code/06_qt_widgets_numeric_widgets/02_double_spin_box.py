# QDoubleSpinBox provides a
# spin box widget that takes doubles.

import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QDoubleSpinBox, QLabel, QGraphicsOpacityEffect)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the spinbox and set its properties
        
        self.spinbox = QDoubleSpinBox()
        self.spinbox.setRange(0, 1)
        self.spinbox.setDecimals(2)
        self.spinbox.setSingleStep(0.05)
        self.spinbox.setValue(1)

        # 3. Connect the valueChanged signal with the slot

        self.spinbox.valueChanged.connect(self.change_opacity)

        self.label = QLabel('QDoubleSpinBox demo')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet('background-color: #008000;')
        
        layout.addWidget(self.spinbox)
        layout.addWidget(self.label)
        
        self.effect = QGraphicsOpacityEffect()
        self.effect.setOpacity(1)
        self.label.setGraphicsEffect(self.effect)
    
    # 2. Create a slot to handle its valueChanged signals.
    
    @Slot(float)
    def change_opacity(self, value):
        self.effect.setOpacity(value)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
