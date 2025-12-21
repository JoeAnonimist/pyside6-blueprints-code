import sys
from PySide6.QtCore import Signal, Slot, QEvent, Qt
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    custom_signal = Signal()
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Click me!')
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.on_button_clicked)
        
        # 1. Force the queued connection
        
        self.custom_signal.connect(self.on_custom_signal_1,
            Qt.ConnectionType.QueuedConnection)
        self.custom_signal.connect(self.on_custom_signal_2,
            Qt.ConnectionType.QueuedConnection)
        self.custom_signal.connect(self.on_custom_signal_3,
            Qt.ConnectionType.QueuedConnection)
    
    @Slot()
    def on_button_clicked(self):
        print('on_button_clicked: Emitting custom signal')
        self.custom_signal.emit()
        print('on_button_clicked: Returning\n')
    
    @Slot()
    def on_custom_signal_1(self):
        print('First custom slot executed\n')
    
    @Slot()
    def on_custom_signal_2(self):
        print('Second custom slot executed\n')
    
    @Slot()
    def on_custom_signal_3(self):
        print('Third custom slot executed\n')
    
    # 2. Intercept MetaCall events
    
    def event(self, event):
        if event.type() == QEvent.Type.MetaCall:
            print(f"Queued signal (MetaCall event) intercepted")
        return QWidget.event(self, event)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())

