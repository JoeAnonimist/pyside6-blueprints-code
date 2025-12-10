# A group box provides a frame, a title on top
# and displays various other widgets inside itself.

import sys

from PySide6.QtWidgets import (QApplication,
    QWidget, QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton, QLabel)


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()

        layout = QHBoxLayout()

        self.label = QLabel()
        self.label.setFixedWidth(80)
        
        # 1 - Create the group box
        #     and add a layout to it. You can't 
        #     add widgets directly to the group box.
        
        self.groupbox = QGroupBox()
        self.groupbox.setTitle('Group box')

        groupbox_layout = QVBoxLayout()
        self.groupbox.setLayout(groupbox_layout)

        # 2 - Add widgets to the layout.

        self.radiobutton_1 = QRadioButton('Option 1')
        self.radiobutton_2 = QRadioButton('Set checkable')
        self.radiobutton_3 = QRadioButton('Set non-checkable')

        groupbox_layout.addWidget(self.radiobutton_1)
        groupbox_layout.addWidget(self.radiobutton_2)
        groupbox_layout.addWidget(self.radiobutton_3)
        
        # 4- Connect child widget signals with the slot
        
        self.radiobutton_1.toggled.connect(self.on_toggled)
        self.radiobutton_2.toggled.connect(self.on_toggled)
        self.radiobutton_3.toggled.connect(self.on_toggled)
        
        self.radiobutton_1.setChecked(True)

        layout.addWidget(self.groupbox)
        layout.addWidget(self.label)
        
        self.setLayout(layout)

    # 3 - Add slot method. If there are 
    #     multiple radio buttons in a group box
    #     only one can be checked, unlike checkboxes.
    
    def on_toggled(self):

        if self.radiobutton_1.isChecked():
            self.label.setText(self.radiobutton_1.text())
        elif self.radiobutton_2.isChecked():
            self.label.setText(self.radiobutton_2.text())
            self.groupbox.setCheckable(True)
        else:
            self.label.setText(self.radiobutton_3.text())
            self.groupbox.setCheckable(False)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
