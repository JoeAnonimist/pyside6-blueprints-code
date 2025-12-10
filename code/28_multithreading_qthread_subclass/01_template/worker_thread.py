from PySide6.QtCore import QThread, Signal, Slot

# 1. Create a QThread subclass
#    and override its run() method.
#    Add signals as needed.

class WorkerThread(QThread):
    
    result_ready = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        print('Init in', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())
        
    def run(self):
        
        print('Running in', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())

        result = 'Hello World'
        print(result)
        self.result_ready.emit(result)

