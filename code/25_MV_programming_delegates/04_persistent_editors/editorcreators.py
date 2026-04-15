from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QItemEditorCreatorBase, QLineEdit


class StrictIntValidator(QIntValidator):
    def validate(self, input_, pos):
        state, input_, pos = super().validate(input_, pos)
        if state == QIntValidator.State.Intermediate:
            try:
                if int(input_) not in range(self.bottom(), self.top() + 1):
                    state = QIntValidator.State.Invalid
            except ValueError:
                pass
        return state, input_, pos


# 1. Create the editor creator class.

class NumericLineEditCreator(QItemEditorCreatorBase):

    def createWidget(self, parent):
        editor = QLineEdit(parent)
        editor.setAutoFillBackground(True)
        editor.setValidator(StrictIntValidator(-100, 100, editor))
        editor.setAlignment(Qt.AlignmentFlag.AlignRight)
        return editor

    def valuePropertyName(self):
        return 'text'
