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
        
        self.start_button = QPushButton('Start background thread')
        self.start_button.clicked.connect(self.on_start_button_clicked)
        
        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.clicked.connect(self.on_cancel_button_clicked)
        self.cancel_button.setDisabled(True)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(self.start_button)
        layout.addWidget(self.cancel_button)
        layout.addWidget(self.label)
    
    @Slot()
    def on_start_button_clicked(self):
        
        print('Main thread loop level', 
            QThread.currentThread().loopLevel())
        
        # 2. Create the WorkerThread object

        self.worker_thread = WorkerThread()
        self.worker_thread.setObjectName('Worker thread')

        # 3. Connect the signals with the slots

        self.worker_thread.progress.connect(self.on_progress)
        self.worker_thread.finished.connect(
            self.worker_thread.deleteLater)
        
        self.start_button.setDisabled(True)
        self.cancel_button.setEnabled(True)
        
        # 5. Start the worker thread
        
        self.worker_thread.start()
    
    # 4. Handle the signals
    
    @Slot()
    def on_cancel_button_clicked(self):
        
        self.start_button.setEnabled(True)
        self.cancel_button.setDisabled(True)
        
        if hasattr(self, 'worker_thread'):
            self.worker_thread.requestInterruption()
            self.worker_thread.wait()
        
    @Slot()
    def on_progress(self, msg):
        self.label.setText(msg)
        
    # Make sure the thread is destroyed
    # when the main window is closed.
    
    def closeEvent(self, event):        
        try:
            self.worker_thread.requestInterruption()
            self.worker_thread.wait()
        except Exception as e:
            print(e) 


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
