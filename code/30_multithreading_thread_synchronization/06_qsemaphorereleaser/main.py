import sys
from PySide6.QtCore import QThread
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout, QLabel)
from atmpool import AtmPool
from worker import Worker


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.thread_count = 15

        self.label = QLabel("Click to start", self)
        self.button = QPushButton("Start Threads", self)
        self.button.clicked.connect(self.start_threads)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.workers = []

    def start_threads(self):

        self.button.setEnabled(False)

        self.atm_pool = AtmPool()
        self.atm_pool_thread = QThread()
        self.atm_pool_thread.setObjectName('Atm Pool thread')
        self.atm_pool.moveToThread(self.atm_pool_thread)
        self.atm_pool_thread.start()
        
        self.completed = 0

        self.workers.clear()

        for i in range(self.thread_count):
            background_thread = QThread(self)
            background_thread.setObjectName(f'Thread {i}')

            worker_obj = Worker(self.atm_pool)
            self.workers.append(worker_obj)
            worker_obj.moveToThread(background_thread)
            
            worker_obj.finished.connect(self.on_worker_done)
    
            background_thread.started.connect(worker_obj.process)
            worker_obj.finished.connect(background_thread.quit)
            worker_obj.finished.connect(worker_obj.deleteLater)
            background_thread.finished.connect(
                background_thread.deleteLater)
            
            background_thread.start()
            
    def on_worker_done(self):
        
        self.completed += 1

        if self.completed == self.thread_count:
            self.atm_pool_thread.quit()
            self.atm_pool_thread.wait()
            self.button.setEnabled(True)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
