import os
from PySide6.QtCore import QThread, Signal

# 1. Create a QThread subclass
#    and subclass its run() method.
#    Add signals as needed.

class WorkerThread(QThread):
    
    progress = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        print('Init it', QThread.currentThread().objectName())
        
    def run(self):
        
        print('Running in: ',
            QThread.currentThread().objectName())
        print('event loop level: ',
            QThread.currentThread().loopLevel())

        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            if QThread.currentThread().isInterruptionRequested():
                return
            self.progress.emit(os.path.basename(root))
