from PySide6.QtWidgets import QItemEditorCreatorBase
from switchwidget import SwitchWidget

# 2. Create an editor creator.

class SwitchCreator(QItemEditorCreatorBase):
    
    def createWidget(self, parent):
        return SwitchWidget(parent)
