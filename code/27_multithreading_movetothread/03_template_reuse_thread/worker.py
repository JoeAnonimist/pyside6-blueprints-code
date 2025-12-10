from PySide6.QtCore import QObject, Signal, Slot

# 1. Create the worker_obj class

class Worker(QObject):
    
    result_ready = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    @Slot()
    def do_work(self, parameter):
        print(parameter)
        self.result_ready.emit(parameter)