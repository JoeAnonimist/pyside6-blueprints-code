# The QComboBox widget is a combined button and popup list.

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QComboBox, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1. Create the combo box and add items to it
        
        self.combo_box = QComboBox()
        
        self.combo_box.addItems([
            'Technology',
            'Healthcare',
            'Finance',
            'Energy',
            'Real Estate'])
        
        # 2. Enable the user to add items
        
        self.combo_box.model().sort(0)
        self.combo_box.setCurrentIndex(1)
        self.combo_box.setEditable(True)
        self.combo_box.setInsertPolicy(
            QComboBox.InsertPolicy.InsertAlphabetically)

        self.label_activated = QLabel()

        layout.addWidget(self.combo_box)
        layout.addWidget(self.label_activated)

        self.combo_box.activated.connect(self.on_activated)
    
    # 3. Create the slot
    
    @Slot(int)
    def on_activated(self, index):
        item_text = self.combo_box.currentText()
        self.label_activated.setText(f'Selected: {item_text}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
