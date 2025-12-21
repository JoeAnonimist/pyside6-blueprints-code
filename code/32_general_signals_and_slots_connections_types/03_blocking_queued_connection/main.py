import sys
from PySide6.QtCore import QThread, Slot, Qt
from PySide6.QtWidgets import (QApplication,
    QPushButton, QWidget, QVBoxLayout)
from sender import Sender
from receiver import Receiver


class Window(QWidget):

    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Start the task')
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)
        
        self.sender_thread = QThread()
        self.receiver_thread = QThread()
        
        self.sender_obj = Sender()
        self.receiver_obj = Receiver()
        
        self.sender_obj.moveToThread(self.sender_thread)
        self.receiver_obj.moveToThread(self.receiver_thread)
        
        self.sender_thread.finished.connect(
            self.sender_obj.deleteLater)
        self.receiver_thread.finished.connect(
            self.receiver_obj.deleteLater)
        
        self.sender_obj.operate.connect(self.receiver_obj.do_work)

        self.receiver_obj.result_ready.connect(
            self.sender_obj.handle_results,
            Qt.ConnectionType.BlockingQueuedConnection)
        '''
        self.receiver_obj.result_ready.connect(
            self.sender_obj.handle_results)
        '''

        self.sender_thread.start()
        self.receiver_thread.start()
    
    @Slot()
    def on_button_clicked(self):
        self.sender_obj.operate.emit()
    
    def closeEvent(self, event):
        try:
            self.sender_thread.quit()
            self.receiver_thread.quit()
            self.sender_thread.wait()
            self.receiver_thread.wait()
        except Exception as e:
            print(e) 
        event.accept()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
