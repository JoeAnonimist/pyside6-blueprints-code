from PySide6.QtCore import Property, Signal
from PySide6.QtWidgets import QWidget, QComboBox, QVBoxLayout


# 1. Create a QObject subclass
#    and add a custom signal to it.

class ThemeSelector(QWidget):

    themeChanged = Signal(str)

    def __init__(self, themes, parent=None):

        super().__init__(parent)
        
        self.themes = themes
        self._default_theme = 'System'
        self._theme = None

        self.combo = QComboBox()
        for theme_name in self.themes:
            self.combo.addItem(theme_name)

        self.combo.currentTextChanged.connect(self.setTheme)
        self.setTheme(self._default_theme)

        layout = QVBoxLayout(self)
        layout.addWidget(self.combo)
    
    # 2. Declare the getter and setter.
    
    def getTheme(self):
        return self._theme

    def setTheme(self, value):
        if value != self._theme:
            self._theme = value
            self.combo.setCurrentText(value)
            self.themeChanged.emit(self.combo.currentText())
    
    # 3. Declare the reset method
    
    def resetTheme(self):
        self.setTheme(self._default_theme)
    
    # 4. Declare the property, setting the getter,
    #    setter, reset method and notify signal,
    
    theme = Property(
        str,
        fget=getTheme,
        fset=setTheme,
        freset=resetTheme,
        notify=themeChanged
    )
