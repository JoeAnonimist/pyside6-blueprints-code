from PySide6.QtCore import Property
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QLabel


class ColoredLabel(QLabel):
    
    def __init__(self, text='', color=None, parent=None):
        
        super().__init__(text, parent)
        self._color = color
    
    @Property(QColor)
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if color != self._color:
            self._color = color
            self.setStyleSheet(
                f'background-color: {color.name()}')