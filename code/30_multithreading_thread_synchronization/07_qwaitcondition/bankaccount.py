from PySide6.QtCore import (QObject, QMutex, 
    QMutexLocker,QThread, QWaitCondition)


class BankAccount(QObject):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self.balance = 0
        self.mutex = QMutex()
        self.condition = QWaitCondition()

    def deposit(self, amount):
        
        locker = QMutexLocker(self.mutex)
        self.balance += amount
        print(f'[Deposit] Balance updated: {self.balance}')
        self.condition.wakeAll()

    def withdraw(self, amount):

        locker = QMutexLocker(self.mutex)

        thread_name = QThread.currentThread().objectName()
        while self.balance < amount:
            if QThread.currentThread().isInterruptionRequested():
                return
            print('[Withdraw] No money. Waiting... '
                  f'| Thread: {thread_name}')
            self.condition.wait(self.mutex)

        self.balance -= amount
        print('[Withdraw] Done. Remaining: '
            f'{self.balance} | Thread: {thread_name}')

    def wake_threads(self):
        locker = QMutexLocker(self.mutex)
        self.condition.wakeAll()
