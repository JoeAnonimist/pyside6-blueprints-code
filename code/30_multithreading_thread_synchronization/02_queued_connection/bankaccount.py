from PySide6.QtCore import QObject, QThread, Signal, Slot

class BankAccount(QObject):
    
    balanceSent = Signal(int)
    
    def __init__(self, balance, parent=None):
        super().__init__(parent)
        self.balance = balance
    
    @Slot(int)
    def withdraw(self, amount):
        print('---withdraw start---',
            QThread.currentThread().objectName())
        balance = self.balance
        if balance >= amount:
            balance -= amount
            QThread.msleep(1)
            self.balance = balance
        print('---withdraw end---',
            QThread.currentThread().objectName())
        
    @Slot()
    def send_balance(self):
        self.balanceSent.emit(self.balance)