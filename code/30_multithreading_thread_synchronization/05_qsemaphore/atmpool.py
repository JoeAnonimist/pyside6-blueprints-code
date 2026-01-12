from random import randint
from PySide6.QtCore import QObject, QSemaphore, QThread, Slot

class AtmPool(QObject):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.atm_count = 5        
        self.semaphore = QSemaphore(self.atm_count)
    
    @Slot()
    def use_atm(self):
        self.semaphore.acquire()
        try:
            print(QThread.currentThread().objectName() +
                ' is using an ATM ' +
                '(available: ' +
                str(self.semaphore.available()) + ')')
            QThread.msleep(randint(10, 200))
        finally:
            print(QThread.currentThread().objectName() +
                ' done. (available before release: ' +
                str(self.semaphore.available()))
            self.semaphore.release()
