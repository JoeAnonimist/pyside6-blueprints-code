from PySide6.QtCore import QObject, Signal, Slot

# 1. Create the worker_obj class

class Worker(QObject):
    
    finished = Signal()
    error = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    # This method to be executed
        
    @Slot()
    def process(self):
        print('Hello World')
        self.finished.emit()