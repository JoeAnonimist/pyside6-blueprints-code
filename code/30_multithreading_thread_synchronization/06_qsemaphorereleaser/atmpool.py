from random import randint
from PySide6.QtCore import (QObject, QSemaphore,
    QSemaphoreReleaser, QThread, Slot)

class AtmPool(QObject):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.atm_count = 5
        self.semaphore = QSemaphore(self.atm_count)

    @Slot()
    def use_atm(self):
        self.semaphore.acquire()
        releaser = QSemaphoreReleaser(self.semaphore)
        print(QThread.currentThread().objectName() +
            ' is using an ATM' +
            ' (available: ' +
            str(self.semaphore.available()) + ')')
        QThread.msleep(randint(10, 200))
        print(QThread.currentThread().objectName() +
            ' done ' +
            '(available before release: ' +
            str(self.semaphore.available()) + ')')
        #del releaser