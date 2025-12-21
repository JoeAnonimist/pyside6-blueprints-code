import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Click me!')
        
        '''
        for i in range(5):
            button.clicked.connect(
                lambda : self.log_to_file(i))
        '''
        
        for i in range(5):
            self.button.clicked.connect(
                lambda checked=self.button.isChecked(),
                x=i: self.log_to_file(checked, x))

        layout.addWidget(self.button)
    
    def log_to_file(self, checked, log_id):
        print('Button clicked')
        print(f'Logging to file no: {log_id}')
        print(f'Checked: {checked}')
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
