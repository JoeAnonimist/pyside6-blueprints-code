from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QStyledItemDelegate
from ledpainter import draw_led


class LedDelegate(QStyledItemDelegate):
    
    # 1. Return None from createEditor.

    def createEditor(self, parent, option, index):
        return None

    # 2. Reimplement paint()
    
    def paint(self, painter, option, index):
        value = index.data(Qt.ItemDataRole.EditRole)
        draw_led(painter, option.rect, value)
        super().paint(painter, option, index)
    
    # 3. Reimplement editorEvent()
    
    def editorEvent(self, event, model, option, index):

        if event.type() == QEvent.Type.MouseButtonRelease:
            if event.button() == Qt.MouseButton.LeftButton:
                if option.rect.contains(event.pos()):
                    current = model.data(index, Qt.ItemDataRole.EditRole)
                    model.setData(index, not current,
                        Qt.ItemDataRole.EditRole)
                    return True
                
        if event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Space:
                current = model.data(index, Qt.ItemDataRole.EditRole)
                model.setData(index, not current,
                    Qt.ItemDataRole.EditRole)
                return True
    
        return super().editorEvent(event, model, option, index)
