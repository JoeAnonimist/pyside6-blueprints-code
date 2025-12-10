import os
from PySide6.QtCore import (QObject, QMutex, 
    QMutexLocker, Signal, Slot)

# 1. Create the worker_obj class

class Worker(QObject):
    
    result_ready = Signal()
    progress = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interruption_requested = False
        self.mutex = QMutex()
        
    @Slot()
    def do_work(self):
        
        self.interruption_requested = False
        
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            with QMutexLocker(self.mutex):
                if self.interruption_requested:
                    self.progress.emit('Canceled')
                    self.result_ready.emit()
                    return
            self.progress.emit(os.path.basename(root))
        self.result_ready.emit()
        
    @Slot()
    def stop(self):
        with QMutexLocker(self.mutex):
            self.interruption_requested = True
        
    @Slot()
    def reset(self):
        with QMutexLocker(self.mutex):
            self.interruption_requested = False
