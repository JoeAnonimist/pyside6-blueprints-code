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
        
        self.button.clicked.connect(self.on_button_clicked_1)
        self.button.clicked.connect(self.on_button_clicked_2)
        self.button.clicked.connect(self.on_button_clicked_3)
    
    def on_button_clicked_1(self):
        print('Executed first')
        
    def on_button_clicked_2(self):
        print('Executed second')
        
    def on_button_clicked_3(self):
        print('Executed third')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()
    
    sys.exit(app.exec())
