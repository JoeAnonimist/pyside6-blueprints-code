import os
from PySide6.QtCore import QObject, QThread, Signal, Slot

# 1. Create the worker_obj class

class Worker(QObject):
    
    finished = Signal()
    progress = Signal(str)
    error = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
    
    # This is the method we want to execute.
    # We are in a tight loop.

    @Slot()
    def process(self):
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            if QThread.currentThread().isInterruptionRequested():
                return
            self.progress.emit(os.path.basename(root))
        self.finished.emit()
