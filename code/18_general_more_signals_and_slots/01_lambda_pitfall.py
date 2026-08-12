import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, 
    QWidget, QCheckBox, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the checkbox
        
        self.checkbox = QCheckBox('Log State')
        
        '''
        
        # This will not work:
        
        for i in range(5):
            self.checkbox.checkStateChanged.connect(
                lambda : self.log_to_file(self.checkbox.checkState(), i))
        '''
        
        # 2. Use a loop to connect the signal.
        #    Each lambda captures the arguments' current values.
        
        for i in range(5):
            self.checkbox.checkStateChanged.connect(
                lambda state, x=i:
                    self.log_to_file(state, x))

        layout.addWidget(self.checkbox)
    
    # 3. Log state change signals.
    
    def log_to_file(self, state, log_id):
        print(f'Logging to file no: {log_id}')
        print(f'State: {state}')
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
