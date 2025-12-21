import sys
from PySide6.QtCore import Slot, Qt, SIGNAL
from PySide6.QtWidgets import (QApplication, QWidget, 
    QVBoxLayout, QLabel, QPushButton)


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Click Me')        
        self.connect_btn = QPushButton('Connect signals')
        self.label = QLabel('Button: 0 receivers')
        
        layout.addWidget(self.button)
        layout.addWidget(self.connect_btn)
        layout.addWidget(self.label)
        
        self.connect_btn.clicked.connect(
            self.on_connect_btn_clicked)

    def on_connect_btn_clicked(self):
        self.button.clicked.connect(self.on_clicked, 
            Qt.ConnectionType.SingleShotConnection)        
        self.update_label()
        
    @Slot(bool)
    def on_clicked(self, checked):
        print('Button clicked')
        self.update_label()
        
    def update_label(self):
        count = self.button.receivers(SIGNAL('clicked(bool)'))
        self.label.setText(f'Button: {count} receivers')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())