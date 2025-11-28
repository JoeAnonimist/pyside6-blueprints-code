# The QLineEdit widget is a one-line text editor. 

import sys

from PySide6.QtCore import Slot
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QLineEdit, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        self.resize(240, 20)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create a line edit widget instance
        
        self.line_edit = QLineEdit()
        validator = QRegularExpressionValidator('^[a-zA-Z]*$')
        self.line_edit.setValidator(validator)
        
        self.label = QLabel()
        
        # 3 - Connect the signals with the slots
        
        self.line_edit.editingFinished.connect(self.on_editing_finished)
        self.line_edit.inputRejected.connect(self.on_input_rejected)
        
        layout.addWidget(self.line_edit)
        layout.addWidget(self.label)

    # 2 - Create methods to handle line edit signals. 
    
    @Slot()
    def on_editing_finished(self):
        self.label.setText(
            f'Editing finished: {self.line_edit.text()}')
        
    @Slot()
    def on_input_rejected(self):
        self.label.setText('Only letters allowed')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())