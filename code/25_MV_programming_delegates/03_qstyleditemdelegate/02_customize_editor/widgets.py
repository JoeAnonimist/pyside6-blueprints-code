from PySide6.QtCore import Qt, Property, Slot
from PySide6.QtGui import QPainter, QKeyEvent
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout
from ledpainter import draw_led


class LedButton(QPushButton):
    
    def __init__(self, led_value, parent=None):
        super().__init__(parent)
        self.led_value = led_value
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
    
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rect = self.rect()
        draw_led(painter, rect, self.led_value)

# 2. Create the custom editor widget.

class LedWidget(QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.setAutoFillBackground(True)
        self._value = False
        
        self.true_button = LedButton(True)
        self.true_button.setCheckable(True)
        self.true_button.setAutoExclusive(True)

        self.false_button = LedButton(False)
        self.false_button.setCheckable(True)
        self.false_button.setAutoExclusive(True)
        self.true_button.toggled.connect(self.on_toggled)
        
        layout = QHBoxLayout()
        layout.addWidget(self.true_button)
        layout.addWidget(self.false_button)
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
            self.true_button.setChecked(True)
        else:
            self.false_button.setChecked(True)
        
    value = Property(bool, getValue, setValue, user=True)
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in (Qt.Key.Key_Left, Qt.Key.Key_Right):
            self.setValue(not self._value)
            event.accept()
            return
        super().keyPressEvent(event)
