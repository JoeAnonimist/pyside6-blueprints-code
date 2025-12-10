# https://doc.qt.io/qt-6/qthread.html

import sys

from PySide6.QtCore import QThread, Slot, Signal, Qt
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)
from worker import Worker


class Controller(QWidget):
    
    operate = Signal()
    
    def __init__(self):

        super().__init__()
        
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
        
        # 2. Create the thread
        
        self.worker_thread = QThread()
        
        # 3. Create the worker_obj and move it to the thread
        
        self.worker_obj = Worker()
        self.worker_obj.moveToThread(self.worker_thread)
        
        # 4. Connect the signals with the slots
        
        self.worker_thread.finished.connect(self.worker_obj.deleteLater)
        self.operate.connect(self.worker_obj.do_work)
        self.worker_obj.result_ready.connect(self.handle_results)
        
        self.worker_obj.progress.connect(self.label.setText)
        
        # 5. Start the thread

        self.worker_thread.start()
    
    # 6. On the start button click emit the operate signal
    
    @Slot()
    def on_start_button_clicked(self):
        
        self.start_button.setDisabled(True)
        self.cancel_button.setEnabled(True)
        
        self.worker_obj.reset()
        self.operate.emit()
    
    # 7. On the cancel button click stop the worker_obj
    
    @Slot()
    def on_cancel_button_clicked(self):
        
        self.start_button.setEnabled(True)
        self.cancel_button.setDisabled(True)
        self.worker_obj.stop()

    @Slot()
    def handle_results(self):
        self.label.setText('Worker finished')
    
    # 8. Quit the thread when the main window is closed
    
    def closeEvent(self, event):        
        try:
            self.worker_obj.stop()
            self.worker_thread.quit()
            self.worker_thread.wait()
        except Exception as e:
            print(e) 
        event.accept()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Controller()
    main_window.show()

    sys.exit(app.exec())

