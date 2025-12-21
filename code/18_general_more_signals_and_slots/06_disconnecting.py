import sys
from PySide6.QtCore import Slot, QObject, SIGNAL
from PySide6.QtWidgets import (QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, QLabel, QPushButton)


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.connections = []
        
        self.button = QPushButton('Click Me') 
        self.button.setCheckable(True)       
        self.label = QLabel('Button: 0 receivers')
        
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        h_layout = QHBoxLayout()
        self.connect_btn = QPushButton('Connect signals')
        self.connect_btn.clicked.connect(self.on_connect_btn_clicked)
        
        self.disconnect_1 = QPushButton('Disconnect 1')
        self.disconnect_1.clicked.connect(self.on_disconnect_1)
        
        self.disconnect_2 = QPushButton('Disconnect 2')
        self.disconnect_2.clicked.connect(self.on_disconnect_2)
        
        self.disconnect_3 = QPushButton('Disconnect 3')
        self.disconnect_3.clicked.connect(self.on_disconnect_3)
        
        self.disconnect_4 = QPushButton('Disconnect 4')
        self.disconnect_4.clicked.connect(self.on_disconnect_4)
        
        h_layout.addWidget(self.connect_btn)
        
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.disconnect_1)
        v_layout.addWidget(self.disconnect_2)
        v_layout.addWidget(self.disconnect_3)
        v_layout.addWidget(self.disconnect_4)
        h_layout.addLayout(v_layout)
        layout.addLayout(h_layout)

    def on_connect_btn_clicked(self):
        c1 = self.button.clicked.connect(self.slot_1)        
        c2 = self.button.clicked.connect(self.slot_2)
        c3 = self.button.toggled.connect(self.slot_3)
        self.connections.extend([c1, c2, c3])
        self.update_label()

    def on_disconnect_1(self):
        for c in self.connections:
            QObject.disconnect(c)
        self.update_label()
        
    def on_disconnect_2(self):
        QObject.disconnect(self.button, None, None, None)
        self.update_label()
        
    def on_disconnect_3(self):
        QObject.disconnect(self.button, SIGNAL('clicked(bool)'), None, None)
        self.update_label()
        
    def on_disconnect_4(self):
        QObject.disconnect(self.button, None, self, None)
        self.update_label()
        
    @Slot(bool)
    def slot_1(self, checked):
        print('Slot 1 executing')
        self.update_label()
        
    @Slot()
    def slot_2(self):
        print('Slot 2 executing')
        self.update_label()
        
    @Slot(bool)
    def slot_3(self, checked):
        print('Slot 3 executing')
        self.update_label()
        
    def update_label(self):
        count_1 = self.button.receivers(SIGNAL('clicked(bool)'))
        count_2 = self.button.receivers(SIGNAL('toggled(bool)'))
        count = count_1 + count_2
        self.label.setText(f'Button: {count} receivers')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())