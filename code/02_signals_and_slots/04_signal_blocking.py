import sys
from PySide6.QtCore  import Slot, Qt
from PySide6.QtWidgets import (QApplication, 
    QWidget, QPushButton, QCheckBox, QVBoxLayout)

class Window(QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.button = QPushButton('Click me!')
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)
        
        block_checkbox = QCheckBox('Block signals')
        block_checkbox.checkStateChanged.connect(
            self.on_check_state_changed)
        layout.addWidget(block_checkbox)

    @Slot(bool)
    def on_button_clicked(self, checked):
        print('Button clicked,', 'checked:', checked)
    
    # Use QObject.blockSignals() to block/unblock a signal
    
    @Slot(bool)
    def on_check_state_changed(self, state):
        if state == Qt.CheckState.Checked:
            self.button.blockSignals(True)
            print('Signals blocked!')
        else:
            self.button.blockSignals(False)
            print('Signals unblocked!')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
