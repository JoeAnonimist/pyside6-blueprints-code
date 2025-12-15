import sys
from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import (QApplication, QWidget,
    QLabel, QSpinBox, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.counter = 0
        self.pending_interval = None
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the spinbox and timer objects
        
        self.spinbox = QSpinBox()
        self.spinbox.setRange(200, 2000)
        self.spinbox.setValue(1000)
        self.spinbox.setSingleStep(100)
        self.spinbox.valueChanged.connect(self.adjust_interval)
        layout.addWidget(self.spinbox)
        
        self.label = QLabel(str(self.counter))
        layout.addWidget(self.label)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        
        self.timer.start(self.spinbox.value())
    
    # 3. On timeout, check if the user changed the spinbox value
    #    and adjust the timer interval to sync them.
    #    Also, perform timed tasks.
    
    @Slot()
    def on_timeout(self):
        
        if self.pending_interval is not None:
            self.timer.setInterval(self.pending_interval)
            self.pending_interval = None

        self.counter += 1
        self.label.setText(str(self.counter))
    
    # 2. When the spinbox value changes store it in a
    #    member variable.
    
    @Slot(int)
    def adjust_interval(self, value):
        self.pending_interval = value
      

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
