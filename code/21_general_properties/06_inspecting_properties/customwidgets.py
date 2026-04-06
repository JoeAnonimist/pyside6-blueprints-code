from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout


# 1. Create the PropertyInspector subclass of QWidget.

class PropertyInspector(QWidget):
    
    def __init__(self, target_widget, parent=None):

        super().__init__(parent)
        
        self.target = target_widget
        
        self.inspect_button = QPushButton('Inspect Properties')
        self.inspect_button.clicked.connect(self.inspect)
        
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.inspect_button)
        layout.addWidget(self.output)
    
    # 2. Implement a method to inspect
    #    the target object's properties.
    
    @Slot()
    def inspect(self):

        self.output.clear()
        
        # Static properties
        meta = self.target.metaObject()
        self.output.append('Static Properties:')
        for i in range(meta.propertyOffset(), meta.propertyCount()):
            try:
                prop = meta.property(i)
                value = prop.read(self.target)
                self.output.append(f'    {prop.name()}: {value}')
            except Exception:
                self.output.append(f'    {prop.name()}: <unreadable>')
        
        # Dynamic properties
        self.output.append('\nDynamic Properties:')
        for name in self.target.dynamicPropertyNames():
            value = self.target.property(name.toStdString())
            self.output.append(f'    {name.toStdString()}: {value}')
