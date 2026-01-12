from PySide6.QtCore import QObject, Signal

class Worker(QObject):
    
    finished = Signal()

    def __init__(self, bank_account, amount, parent=None):
        super().__init__(parent)
        self.bank_account = bank_account
        self.amount = amount

    def process(self):
        self.bank_account.withdraw(self.amount)
        self.finished.emit()
