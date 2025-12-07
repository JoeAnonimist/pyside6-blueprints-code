import sys
from PySide6.QtCore import QTime, QTimer, Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QLabel, QVBoxLayout)

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the button object
        
        self.button = QPushButton('Start timer')
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)
        
        self.label = QLabel('Start the timer')
        layout.addWidget(self.label)
    
    # 2. Call the singleShot() class method
    
    @Slot()
    def on_button_clicked(self):
        self.button.setDisabled(True)
        self.label.setText('Waiting...')
        QTimer.singleShot(1000, self.on_single_shot)
    
    # 3. Set the label text after 1000ms 
    
    @Slot()
    def on_single_shot(self):
        current_time = QTime.currentTime()
        text = f'Done! {current_time.toString("hh:mm:ss")}'
        self.label.setText(text)
        self.button.setEnabled(True)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
