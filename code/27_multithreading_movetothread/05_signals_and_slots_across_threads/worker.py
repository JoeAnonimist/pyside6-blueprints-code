from PySide6.QtCore import QObject, QThread, Signal, Slot

class Worker(QObject):
    
    auto_signal = Signal()
    direct_signal = Signal()
    queued_signal = Signal()
    blocking_signal = Signal()
    
    @Slot()
    def auto_slot(self):
        print('Auto connection')
        print('In', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())

    @Slot()
    def direct_slot(self):
        print('Direct connection')
        print('In', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())
    @Slot()
    def queued_slot(self):
        print('Queued connection')
        print('In', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())
        
    @Slot()
    def blocking_slot(self):
        print('Blocking Queued connection')
        print('In', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())
        QThread.sleep(10)