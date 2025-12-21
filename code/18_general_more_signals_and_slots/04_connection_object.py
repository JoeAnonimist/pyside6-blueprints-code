import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Click me!')
        layout.addWidget(self.button)
        
        # 1. Get a reference to the Connection object
        
        self.conn = self.button.clicked.connect(
            self.on_button_clicked)
        
        self.disconnect_button = QPushButton('Disconnect')
        layout.addWidget(self.disconnect_button)
        self.disconnect_button.clicked.connect(
            self.on_disconnect_button_clicked)
    
    def on_button_clicked(self):
        print('Button clicked')
    
    # 2. Use the reference to disconnect signal from slot
    
    def on_disconnect_button_clicked(self):

        print(type(self.conn))

        if self.conn:
            print('Connection is valid')
            self.button.clicked.disconnect(self.conn)
        else:
            print('Connection is invalid')
            print('Already disconnected')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
