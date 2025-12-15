import sys
from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QLabel, QSpinBox, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # 1. Set the countdown variable with an initial value.
        #    Add a spinbox to let the user adjust it.
        #    Add a button for starting the countdown.
        #    Create a timer.
        
        self.counter = 5
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(10)
        self.spinbox.setValue(self.counter)
        self.spinbox.setSingleStep(1)
        self.spinbox.valueChanged.connect(self.on_value_changed)
        layout.addWidget(self.spinbox)
        
        self.start_button = QPushButton('Start countdown')
        self.start_button.clicked.connect(self.start_countdown)
        layout.addWidget(self.start_button)

        self.label = QLabel(str(self.counter))
        layout.addWidget(self.label)
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.on_timeout)
    
    # 2. On the Start button click:
    #    Set the counter value.
    #    Disable the Start button.
    #    Disable the spinbox.
    #    Start the timer.
    
    @Slot()
    def start_countdown(self):
        self.counter = self.spinbox.value()
        self.label.setText(str(self.spinbox.value()))
        self.start_button.setDisabled(True)
        self.spinbox.setDisabled(True)
        self.timer.start()
    
    # 3. On timeout:
    #    Decrement the counter
    #    Set the label text
    #    If the counter reaches zero, stop the timer
    
    @Slot()
    def on_timeout(self):
        self.counter -= 1
        self.label.setText(str(self.counter))
        if self.counter == 0:
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.spinbox.setEnabled(True)
        
    @Slot(int)
    def on_value_changed(self, value):
        self.counter = value
        self.label.setText(str(self.counter))
      

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
