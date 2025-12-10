import sys
from PySide6.QtCore import QThread, Slot, Qt
from PySide6.QtWidgets import (QApplication, QPushButton,
    QLabel, QWidget, QVBoxLayout)
from worker import Worker

class Window(QWidget):
    
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
    
    @Slot()
    def on_start_button_clicked(self):
        
        self.start_button.setDisabled(True)
        self.cancel_button.setEnabled(True)
        
        # 2. Create the thread
        
        self.background_thread = QThread()
        
        # 3. Create the worker_obj and move it to the thread
        
        self.worker_obj = Worker()
        self.worker_obj.moveToThread(self.background_thread)
        
        self.worker_obj.finished.connect(self.on_finished)
        
        # 4. Connect the appropriate signals to ensure
        #    both the worker_obj and the thread are destroyed.
        
        self.worker_obj.error.connect(self.on_error)
        self.background_thread.started.connect(self.worker_obj.process)
        self.worker_obj.finished.connect(self.background_thread.quit)
        self.worker_obj.finished.connect(self.worker_obj.deleteLater)
        self.background_thread.finished.connect(self.background_thread.deleteLater)
        
        self.worker_obj.progress.connect(self.label.setText)
        
        # 5. Start the thread.
        
        self.background_thread.start()
    
    # Stop the work by requesting interruption
        
    @Slot()
    def on_cancel_button_clicked(self):
        
        self.start_button.setEnabled(True)
        self.cancel_button.setDisabled(True)
        
        if hasattr(self, 'background_thread'):
            self.background_thread.requestInterruption()
            self.background_thread.quit()
            self.background_thread.wait()
    
    @Slot()
    def on_finished(self):
        self.label.setText('Worker finished')
    
    @Slot()
    def on_error(self, message):
        print(message)
    
    # Make sure the thread is destroyed
    # when the main window is closed.
    
    def closeEvent(self, event):        
        try:
            self.background_thread.requestInterruption()
            self.background_thread.quit()
            self.background_thread.wait()
        except Exception as e:
            print(e) 


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
