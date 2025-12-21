from PySide6.QtCore import QObject, Signal, Slot, QThread

class Sender(QObject):
    
    operate = Signal()
            
    @Slot()
    def handle_results(self):
        print('Sender: handle_results started')
        QThread.sleep(5)
        print('Sender: handle_results finished after delay')
