from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStyledItemDelegate
from widgets import LedWidget
from ledpainter import draw_led

# 3. Create the QStyledItemDelegate subclass
#    and reimplement createEditor(), setEditorData()
#    and setModelData()

class LedDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        editor = LedWidget(parent)
        return editor

    def setEditorData(self, editor, index):
        editor.setValue(index.data(Qt.ItemDataRole.EditRole))
    
    def setModelData(self, editor, model, index):
        model.setData(index, editor.getValue(),
            Qt.ItemDataRole.EditRole)

    def paint(self, painter, option, index):
        value = index.data(Qt.ItemDataRole.EditRole)
        draw_led(painter, option.rect, value)
        super().paint(painter, option, index)
