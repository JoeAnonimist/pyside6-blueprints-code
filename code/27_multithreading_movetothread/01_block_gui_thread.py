import os
import sys
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QLabel, QVBoxLayout)


class Task(QObject):
    
    progress = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    # 1. Create a long running task
    #    We search for a file using os.walk()
    #    using a tight (blocking) for loop.
    #    The loop blocks the Qt event loop
    #    so no signals are send or events
    #    processed until the loop exits.
    #    This effectively freezes the Gui.
    
    @Slot()
    def do_work(self):
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        name = 'bogus'
        for root, _, files in os.walk(path):
            self.progress.emit(root)
            if name in files:
                print(os.path.join(root, name))


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 2. Create a push button
        
        self.button = QPushButton('Start working')
        self.label = QLabel()
        
        self.button.clicked.connect(self.do_work)
        
        layout.addWidget(self.button)
        layout.addWidget(self.label)
    
    # 3. Execute the long running task.
    
    def do_work(self):
        self.task = Task()
        self.task.progress.connect(self.label.setText)
        self.task.do_work()
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())

