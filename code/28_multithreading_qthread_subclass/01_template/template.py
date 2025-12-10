# https://doc.qt.io/qt-6/qthread.html

import sys

from PySide6.QtCore import QThread, Slot, Qt
from PySide6.QtWidgets import (QApplication, QPushButton,
    QLabel, QWidget, QVBoxLayout)
from worker_thread import WorkerThread


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        QThread.currentThread().setObjectName('Main thread')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button = QPushButton('Start background thread')
        button.clicked.connect(self.start_work_in_a_thread)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(button)
        layout.addWidget(self.label)
    
    @Slot()
    def start_work_in_a_thread(self):
        
        print('Button click in', QThread.currentThread().objectName(),
            ', Loop level', QThread.currentThread().loopLevel())
        
        # 2. Create the WorkerThread object
        
        self.worker_thread = WorkerThread()
        self.worker_thread.setObjectName('Worker thread')
        
        # 3. Connect the signals with the slots
        
        self.worker_thread.result_ready.connect(self.on_result_ready)
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        
        # 5. Start the worker thread
        
        self.worker_thread.start()
    
    # 4. Handle the worker thread signals
    
    @Slot()
    def on_result_ready(self, result):
        self.label.setText(result)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

