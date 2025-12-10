import os
from PySide6.QtCore import (QObject, QThread,
    QRunnable, Signal, Slot)


class Signals(QObject):
    progress = Signal(str)
    error = Signal(str)

# 1. Create a QRunnable subclass
#    and implement its run() method

class Runnable(QRunnable):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.signals = Signals()
        self.do_work = True
    
    # Enumerate fs objects while self.do_work flag is True
    
    def run(self):
        path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
        for root, _, _ in os.walk(path):
            if not self.do_work:
                return
            self.signals.progress.emit(os.path.basename(root))
            print(QThread.currentThread())
    
    @Slot()
    def on_cancel_emitted(self):
        self.do_work = False
