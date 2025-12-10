# https://mayaposch.wordpress.com/2011/11/01/how-to-really-truly-use-qthreads-the-full-explanation/

import sys
from PySide6.QtCore import QThread, Slot, Qt
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)
from worker import Worker


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button = QPushButton('Start background thread')
        button.clicked.connect(self.on_button_clicked)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(button)
        layout.addWidget(self.label)
    
    @Slot()
    def on_button_clicked(self):
        
        # 2. Create the thread object
        
        self.background_thread = QThread()
        
        # 3. Create the worker_obj and move it to the thread
        
        self.worker_obj = Worker()
        self.worker_obj.moveToThread(self.background_thread)
        
        self.worker_obj.finished.connect(self.on_finished)
        
        # 4. Connect the signals and the slots 
        
        self.worker_obj.error.connect(self.on_error)
        self.background_thread.started.connect(self.worker_obj.process)
        self.worker_obj.finished.connect(self.background_thread.quit)
        self.worker_obj.finished.connect(self.worker_obj.deleteLater)
        self.background_thread.finished.connect(self.background_thread.deleteLater)
        
        # 5. Start the thread
        
        self.background_thread.start()
    
    @Slot()
    def on_finished(self):
        self.label.setText('Worker finished')
    
    @Slot()
    def on_error(self, message):
        print(message)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
