from PySide6.QtCore import Property, Slot
from PySide6.QtWidgets import (QWidget, QRadioButton,
    QHBoxLayout)


# 1. Create the custom editor widget.

class SwitchWidget(QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.setAutoFillBackground(True)
        self._value = False
        
        self.true_radio = QRadioButton('Yes')
        self.false_radio = QRadioButton('No')
        self.true_radio.toggled.connect(self.on_toggled)
        
        layout = QHBoxLayout()
        layout.addWidget(self.true_radio)
        layout.addWidget(self.false_radio)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.setMinimumHeight(self.sizeHint().height())
    
    @Slot(bool)
    def on_toggled(self, checked):
        self.setValue(checked)
        
    def getValue(self):
        return self._value
    
    def setValue(self, value):
        if value != self._value:
            self._value = value
        if value:
            self.true_radio.setChecked(True)
        else:
            self.false_radio.setChecked(True)
        
    value = Property(bool, getValue, setValue, user=True)
