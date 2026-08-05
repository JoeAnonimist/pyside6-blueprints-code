# A group box provides a frame, a title on top
# and displays various other widgets inside itself.

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,
    QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QLabel)


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.resize(340, 140)
        layout = QHBoxLayout()

        self.label = QLabel()
        
        # 1. Create the group box and add a layout to it.
        #   You can't add widgets directly to the group box,
        #   you have to use a layout.
        
        self.groupbox = QGroupBox()
        self.groupbox.setCheckable(True)
        self.groupbox.setChecked(True)
        self.groupbox.setTitle('Recurring Transfer')

        groupbox_layout = QVBoxLayout()
        self.groupbox.setLayout(groupbox_layout)

        # 2 - Add widgets to the layout.

        self.weekly_radio = QRadioButton('Weekly')
        self.monthly_radio = QRadioButton('Monthly')
        self.quarterly_radio = QRadioButton('Quarterly')

        groupbox_layout.addWidget(self.weekly_radio)
        groupbox_layout.addWidget(self.monthly_radio)
        groupbox_layout.addWidget(self.quarterly_radio)

        # 4- Connect the signals with the slot.
        
        self.groupbox.toggled.connect(self.set_frequency)
        self.weekly_radio.toggled.connect(self.set_frequency)
        self.monthly_radio.toggled.connect(self.set_frequency)
        self.quarterly_radio.toggled.connect(self.set_frequency)

        layout.addWidget(self.groupbox)
        layout.addWidget(self.label)
        
        self.monthly_radio.setChecked(True)
        
        self.setLayout(layout)

    # 3 - Add the slot method.
    
    @Slot()
    def set_frequency(self):

        if not self.groupbox.isChecked():
            self.label.setText('Recurring transfer: Disabled')
            return

        if self.weekly_radio.isChecked():
            self.label.setText('Recurring transfer: Weekly')
        elif self.monthly_radio.isChecked():
            self.label.setText('Recurring transfer: Monthly')
        elif self.quarterly_radio.isChecked():
            self.label.setText('Recurring transfer: Quarterly')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
