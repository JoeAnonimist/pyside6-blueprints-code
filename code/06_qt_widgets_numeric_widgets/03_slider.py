# QSlider provides a vertical or horizontal slider.

import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication,
    QWidget,  QVBoxLayout, QSlider, QLabel)


class Window(QWidget):
    
    # # A class-level constant for the stylesheet template
    LABEL_STYLE = "background-color: rgba(0, 128, 0, {});"
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create a slider and set its properties
        
        self.slider = QSlider()
        self.slider.setRange(0, 255)
        self.slider.setValue(255)
        self.slider.setPageStep(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(32)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        
        # 3. Connect signal
        
        self.slider.valueChanged.connect(self.change_opacity)
        
        self.label = QLabel('QSlider demo')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(Window.LABEL_STYLE.format(255))
        
        layout.addWidget(self.slider)
        layout.addWidget(self.label)
    
    # 2. Slot that receives the new opacity value.
    
    @Slot(int)
    def change_opacity(self, value):
        self.label.setStyleSheet(Window.LABEL_STYLE.format(value))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
