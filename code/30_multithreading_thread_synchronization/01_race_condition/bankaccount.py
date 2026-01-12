from PySide6.QtCore import QObject, QThread, Slot

# 1. Create the BankAccount class

class BankAccount(QObject):
    
    def __init__(self, balance, parent=None):
        super().__init__(parent)
        self.balance = balance
    
    @Slot(result=int)
    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        print('---withdraw start---',
            QThread.currentThread().objectName())
        balance = self.balance
        QThread.msleep(1)
        #print(end='')
        #loop = QEventLoop()
        #QTimer.singleShot(1000, loop.quit)
        if balance >= amount:
            balance -= amount
            self.balance = balance
        print('---withdraw end---',
            QThread.currentThread().objectName(), self.balance)