from PySide6.QtCore import QObject, Signal

class Worker(QObject):
    
    transactionProcessed = Signal()
    requestUpdate = Signal(int)

    def __init__(self, bank_account, amount, parent=None):
        super().__init__(parent)
        self.bank_account = bank_account
        self.amount = amount
        self.requestUpdate.connect(self.bank_account.withdraw)

    def process(self):
        self.requestUpdate.emit(self.amount)
        self.transactionProcessed.emit()