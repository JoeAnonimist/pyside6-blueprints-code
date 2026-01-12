import sys
from PySide6.QtCore import Signal, QThread
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout, QLabel)
from bankaccount import BankAccount
from worker import Worker


class Window(QWidget):
    
    requestBalance = Signal()
    
    def __init__(self):

        super().__init__()
        
        self.thread_count = 5
        self.amount = 100
        
        self.label = QLabel('Click to start')
        self.button = QPushButton('Withdraw money')
        self.button.clicked.connect(self.start_threads)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.workers = []

    def start_threads(self):

        self.button.setEnabled(False)

        self.bank_account = BankAccount(self.thread_count * self.amount)
        self.bank_account_thread = QThread()
        self.bank_account_thread.setObjectName('Bank account thread')
        self.bank_account.moveToThread(self.bank_account_thread)
        self.requestBalance.connect(self.bank_account.send_balance)
        self.bank_account.balanceSent.connect(self.on_balance_sent)
        self.bank_account_thread.start()

        self.completed = 0

        self.workers.clear()

        for i in range(self.thread_count):
            background_thread = QThread(self)
            background_thread.setObjectName(f'Thread {i}')

            worker_obj = Worker(self.bank_account, self.amount)
            self.workers.append(worker_obj)
            worker_obj.moveToThread(background_thread)
            
            worker_obj.transactionProcessed.connect(self.on_worker_done)
    
            background_thread.started.connect(worker_obj.process)
            worker_obj.transactionProcessed.connect(background_thread.quit)
            worker_obj.transactionProcessed.connect(worker_obj.deleteLater)
            background_thread.finished.connect(background_thread.deleteLater)
            
            background_thread.start()
            
    def on_worker_done(self):
        self.completed += 1
        if self.completed == self.thread_count:
            self.requestBalance.emit()

            
    def on_balance_sent(self, balance):

        self.bank_account_thread.quit()
        self.bank_account_thread.wait()
        print('Expected: 0, Got:', balance)
        self.label.setText(f'Final balance: {balance}')
        self.button.setEnabled(True)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
