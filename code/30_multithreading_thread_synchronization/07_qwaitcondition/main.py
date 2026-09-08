import sys
from PySide6.QtCore import QThread
from PySide6.QtWidgets import (QApplication,
    QWidget, QPushButton, QVBoxLayout, QLabel)
from bankaccount import BankAccount
from worker import Worker

class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()

        self.thread_count = 5
        self.amount = 100

        self.label = QLabel()
        self.start_button = QPushButton('Start Withdrawals')
        self.deposit_button = QPushButton('Deposit Funds')

        self.start_button.clicked.connect(self.start_threads)
        self.deposit_button.clicked.connect(self.deposit_money)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.deposit_button)

        self.threads = []
        self.workers = []

        self.bank_account = BankAccount()
        self.completed = 0

    def start_threads(self):
        
        self.start_button.setEnabled(False)
        self.completed = 0
        
        self.threads.clear()
        self.workers.clear()

        for i in range(self.thread_count):
            thread = QThread(self)
            thread.setObjectName(f'Thread {i}')
            worker = Worker(self.bank_account, self.amount)
            worker.moveToThread(thread)

            thread.started.connect(worker.process)
            worker.finished.connect(self.on_worker_done)
            worker.finished.connect(thread.quit)
            worker.finished.connect(worker.deleteLater)
            thread.finished.connect(thread.deleteLater)

            self.threads.append(thread)
            self.workers.append(worker)
            
            thread.start()

    def deposit_money(self):
        
        deposit = self.amount * self.thread_count
        print(f'[Main] Depositing {deposit}')
        self.bank_account.deposit(deposit)
        self.label.setText(
            f'Remaining balance: '
            f'{self.bank_account.balance}')

    def on_worker_done(self):

        self.completed += 1
        if self.completed == self.thread_count:
            print(f'Remaining balance: '
                  f'{self.bank_account.balance}')
            self.label.setText(
                f'Remaining balance: '
                f'{self.bank_account.balance}')

            self.start_button.setEnabled(True)

    def closeEvent(self, event):

        for thread in list(self.threads):
            thread.requestInterruption()
    
        self.bank_account.wake_threads()

        for thread in list(self.threads):
            thread.quit()
            thread.wait()

        self.threads.clear()
        self.workers.clear()
    
        super().closeEvent(event)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
