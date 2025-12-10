# https://doc.qt.io/qt-6/qthread.html

import sys

from PySide6.QtCore import QThread, Slot, Qt
from PySide6.QtWidgets import (QApplication, QPushButton,
    QLabel, QWidget, QVBoxLayout)
from worker import Worker


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        QThread.currentThread().setObjectName('Main thread')
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button_auto = QPushButton('Auto connection')
        self.button_direct = QPushButton('Direct connection')
        self.button_queued = QPushButton('Queued connection')
        self.button_blocking = QPushButton('Blocking Queued connection')

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.emitting_thread = QThread()
        self.emitting_thread.setObjectName('Emitting Thread')
        
        self.emitter = Worker()
        self.emitter.moveToThread(self.emitting_thread)
        
        self.receiving_thread = QThread()
        self.receiving_thread.setObjectName('Receiving Thread')
        
        self.receiver = Worker()
        self.receiver.moveToThread(self.receiving_thread)
        
        self.emitter.auto_signal.connect(self.receiver.auto_slot, Qt.ConnectionType.AutoConnection)
        self.emitter.direct_signal.connect(self.receiver.direct_slot, Qt.ConnectionType.DirectConnection)
        self.emitter.queued_signal.connect(self.receiver.queued_slot, Qt.ConnectionType.QueuedConnection)
        self.emitter.blocking_signal.connect(self.receiver.blocking_slot, Qt.ConnectionType.BlockingQueuedConnection)
        
        self.button_auto.clicked.connect(self.emitter.auto_signal)
        self.button_direct.clicked.connect(self.emitter.direct_signal)
        self.button_queued.clicked.connect(self.emitter.queued_signal)
        self.button_blocking.clicked.connect(self.emitter.blocking_signal)
        
        self.emitting_thread.start()
        self.receiving_thread.start()
        
        layout.addWidget(self.button_auto)
        layout.addWidget(self.button_direct)
        layout.addWidget(self.button_queued)
        layout.addWidget(self.button_blocking)
        layout.addWidget(self.label)
    
    @Slot()
    def on_result_ready(self, result):
        self.label.setText(result)
        
    def closeEvent(self, event):        
        try:
            self.emitting_thread.quit()
            self.emitting_thread.wait()
            self.receiving_thread.quit()
            self.receiving_thread.wait()
        except Exception as e:
            print(e) 
        event.accept()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

