import sys
import psutil
from PySide6.QtCore import Qt, QEvent, QTimer, QObject
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)

# 1. Create a custom event class.

class CpuUsageEvent(QEvent):
    
    event_type = QEvent.Type(QEvent.registerEventType())
    
    def __init__(self, cpu_percent):
        super().__init__(CpuUsageEvent.event_type)
        self.cpu_percent = cpu_percent

class CpuUsageEventFilter(QObject):
        
    def eventFilter(self, watched, event):
        if event.type() == CpuUsageEvent.event_type:
            print('In eventFilter(): ', event.cpu_percent)
            watched.setText(f'{event.cpu_percent} % CPU used')
        return super().eventFilter(watched, event)

class Window(QWidget):
    
    THRESHOLD = 10 # CPU percent
    
    def __init__(self):

        super().__init__()
        self.resize(300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        
        self.filter = CpuUsageEventFilter()
        self.label.installEventFilter(self.filter)
        layout.addWidget(self.label)
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start()
        
    def on_timeout(self):
        cpu_percent = psutil.cpu_percent(interval=None)
        if cpu_percent > self.THRESHOLD:
            # 3. Create an event object and post it.
            QApplication.postEvent(self.label, CpuUsageEvent(cpu_percent))        
            QApplication.postEvent(self, CpuUsageEvent(cpu_percent))
        else:
            self.label.clear()

    def event(self, event):
        if event.type() == CpuUsageEvent.event_type:
            print('In event(): ', event.cpu_percent)
        return super().event(event)
    
    def customEvent(self, event):
        if event.type() == CpuUsageEvent.event_type:
            print('In customEvent(): ', event.cpu_percent)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
