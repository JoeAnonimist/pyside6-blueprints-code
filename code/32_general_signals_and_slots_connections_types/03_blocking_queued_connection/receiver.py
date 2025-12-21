from PySide6.QtCore import QObject, Signal, Slot

class Receiver(QObject):

    result_ready = Signal()
        
    @Slot()
    def do_work(self):
        print('Receiver: Starting do_work')
        print('Receiver: Emitting result_ready')
        self.result_ready.emit()
        print('Receiver: After emit (this should delay if blocking)')
