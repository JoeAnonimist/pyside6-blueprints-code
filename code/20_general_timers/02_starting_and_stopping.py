import sys
from PySide6.QtCore import QTimer, Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QPushButton, QLabel, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.counter = 0
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the start and stop buttons.
        
        self.start_button = QPushButton('Start timer')
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton('Stop timer')
        self.stop_button.clicked.connect(self.stop_timer)
        self.stop_button.setEnabled(False)
        layout.addWidget(self.stop_button)
        
        self.label = QLabel('0')
        layout.addWidget(self.label)
        
        # 2. Create the timer and set its interval
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.on_timeout)
    
    # 3. Start/stop the timer on buttons click
    
    @Slot()
    def start_timer(self):
        self.start_button.setDisabled(True)
        self.stop_button.setEnabled(True)
        self.timer.start()
        
    @Slot()
    def stop_timer(self):
        self.start_button.setEnabled(True)
        self.stop_button.setDisabled(True)
        self.timer.stop()
    
    # 4. Update the display on timer timeout.
    
    @Slot()
    def on_timeout(self):
        self.counter += 1
        self.label.setText(str(self.counter))
      

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
