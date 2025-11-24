# A QCheckBox is an option button that can be 
# checked, unchecked or partially checked. 

import sys

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QCheckBox, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the checkboxes and add them to the layout
        
        self.windows_checkbox = QCheckBox('Windows')
        self.windows_checkbox.setObjectName('Windows')

        self.linux_checkbox = QCheckBox('Linux')
        self.linux_checkbox.setObjectName('Linux')
        
        self.macos_checkbox = QCheckBox('macOS')
        self.macos_checkbox.setObjectName('macOS')
        self.macos_checkbox.setTristate(True)

        self.label = QLabel()
        
        layout.addWidget(self.windows_checkbox)
        layout.addWidget(self.linux_checkbox)
        layout.addWidget(self.macos_checkbox)
        
        layout.addWidget(self.label)
        
        # 3 - For each checkbox connect QCheckBox.
        #     checkStateChanged signal with the slot.
        #     checkStateChanged is emitted when a checkbox
        #     state changes.
        
        self.windows_checkbox.checkStateChanged.connect(
            self.on_state_changed)
        self.linux_checkbox.checkStateChanged.connect(
            self.on_state_changed)
        self.macos_checkbox.checkStateChanged.connect(
            self.on_state_changed)
    
    # 2 - Create the slot. Mark it with the @Slot() decorator
    #     If you don't import PySide6.QtCore.Qt above, you will
    #     get an error: TypeError: Cannot call meta function ...
    
    @Slot(Qt.CheckState)
    def on_state_changed(self, state):
        sender_name = self.sender().objectName()
        self.label.setText(f'{sender_name} {state}')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())