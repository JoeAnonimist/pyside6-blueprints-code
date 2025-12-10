import sys

from PySide6.QtCore import QThreadPool, Slot, Qt
from PySide6.QtWidgets import (QApplication,
    QPushButton, QLabel, QWidget, QVBoxLayout)
from runnable import Runnable


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        button = QPushButton('Start background thread')
        button.clicked.connect(self.on_button_clicked)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(button)
        layout.addWidget(self.label)
    
    # When the button is clicked:
    
    @Slot()
    def on_button_clicked(self):
        
        # 2. Create a Runnable object
        
        runnable = Runnable()

        runnable.signals.progress.connect(self.label.setText)
        runnable.signals.error.connect(self.on_error)
        
        # 3. Access the QThreadPool global instance
        #    and run the task. 

        QThreadPool.globalInstance().start(runnable)
    
    @Slot()
    def on_error(self, message):
        print(message)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())

