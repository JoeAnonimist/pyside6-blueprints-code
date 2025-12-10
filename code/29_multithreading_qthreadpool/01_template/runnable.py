from PySide6.QtCore import QObject, QRunnable, Signal


class Signals(QObject):
    progress = Signal(str)
    error = Signal(str)

# 1. Create a QRunnable subclass
#    and implement its run() method.

class Runnable(QRunnable):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.signals = Signals()
    
    # The run method will be executed
    # in the worker thread.
    
    def run(self):
        self.signals.progress.emit('Progress emitted')
        print('Hello World')
        self.signals.deleteLater()

