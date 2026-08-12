import sys
from PySide6.QtCore import QTimer, QTime, Slot, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QWidget,
    QPushButton, QLabel, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # 1. Add a variable to track elapsed time.
        
        self.elapsed_time = QTime(0, 0, 0, 0)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 2. Add the start, pause and reset buttons
        
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_stopwatch)
        layout.addWidget(self.start_button)
        
        self.pause_button = QPushButton('Pause')
        self.pause_button.setDisabled(True)
        self.pause_button.clicked.connect(self.pause_stopwatch)
        layout.addWidget(self.pause_button)
        
        self.reset_button = QPushButton('Reset')
        self.reset_button.clicked.connect(self.reset_stopwatch)
        layout.addWidget(self.reset_button)

        self.label = QLabel(self.elapsed_time.toString('mm:ss.z'))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Monospace", 18))
        layout.addWidget(self.label)
        
        # 3. Create the timer.
        
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.on_timeout)
    
    @Slot()
    def start_stopwatch(self):
        self.start_button.setDisabled(True)
        self.pause_button.setEnabled(True)
        self.timer.start()
        
    @Slot()
    def pause_stopwatch(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.pause_button.setDisabled(True)
    
    @Slot()
    def reset_stopwatch(self):
        self.timer.stop()
        self.elapsed_time = QTime(0, 0, 0, 0)
        self.label.setText(self.elapsed_time.toString('mm:ss.z'))
        self.start_button.setEnabled(True)
        self.pause_button.setDisabled(True)
    
    # 4. Update the time.
    
    @Slot()
    def on_timeout(self):
        self.elapsed_time = self.elapsed_time.addMSecs(100)
        self.label.setText(self.elapsed_time.toString('mm:ss.z'))
      

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
