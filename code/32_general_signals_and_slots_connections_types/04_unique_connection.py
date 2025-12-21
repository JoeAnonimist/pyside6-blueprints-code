import sys
from PySide6.QtCore import Slot, Qt, SIGNAL
from PySide6.QtWidgets import (QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, QLabel, QPushButton)


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Click Me')        
        self.label = QLabel('Button: 0 receivers')
        
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        h_layout = QHBoxLayout()
        self.connect_btn = QPushButton('Connect signals')
        self.disconnect_btn = QPushButton('Disconnect signals')
        
        self.connect_btn.clicked.connect(
            self.on_connect_btn_clicked)
        self.disconnect_btn.clicked.connect(
            self.on_disconnect_btn_clicked)
        
        h_layout.addWidget(self.connect_btn)
        h_layout.addWidget(self.disconnect_btn)
        layout.addLayout(h_layout)

    def on_connect_btn_clicked(self):
        conn = self.button.clicked.connect(self.on_clicked,
            Qt.ConnectionType.UniqueConnection)
        if conn:
            print('Connection is valid')
        else:
            print('Connection is invalid')
        self.update_label()

    def on_disconnect_btn_clicked(self):
        self.button.clicked.disconnect(self.on_clicked)
        self.update_label()
        
    @Slot(bool)
    def on_clicked(self, checked):
        print('Button clicked')
        
    def update_label(self):
        count = self.button.receivers(SIGNAL('clicked(bool)'))
        self.label.setText(f'Button: {count} receivers')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())