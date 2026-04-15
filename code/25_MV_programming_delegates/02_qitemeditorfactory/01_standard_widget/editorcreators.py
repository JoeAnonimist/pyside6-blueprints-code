from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QItemEditorCreatorBase, QLineEdit


# 1. Create an item editor creator.

class NumericLineEditCreator(QItemEditorCreatorBase):
    
    def __init__(self, min_val=-100, max_val=100):
        super().__init__()
        self.min_val = min_val
        self.max_val = max_val
    
    def createWidget(self, parent):
        editor = QLineEdit(parent)
        editor.setAutoFillBackground(True)
        validator = QIntValidator(self.min_val, self.max_val, editor)
        editor.setValidator(validator)
        editor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # If we don't implement valuePropertyName()
        # the widget's user property is used
        # (in this case 'text')
        print(editor.metaObject().userProperty().name())
        
        return editor
