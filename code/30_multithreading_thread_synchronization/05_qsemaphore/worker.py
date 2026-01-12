from PySide6.QtCore import QObject, Signal

class Worker(QObject):
    
    finished = Signal()

    def __init__(self, atm_pool, parent=None):
        super().__init__(parent)
        self.atm_pool = atm_pool

    def process(self):
        self.atm_pool.use_atm()
        self.finished.emit()
