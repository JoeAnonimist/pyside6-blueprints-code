from PySide6.QtGui import QTransform
from PySide6.QtWidgets import QGraphicsScene


class Scene(QGraphicsScene):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.notes = []
        
    def remove_note(self, note):
        self.notes.remove(note)
        self.removeItem(note)
        if self.notes:
            self.notes[-1].setFocus()
    
    def mousePressEvent(self, event):

        item = self.itemAt(event.scenePos(), QTransform())
        if item:
            max_z = max(i.zValue() for i in self.items())
            item.setZValue(max_z + 1)
        super().mousePressEvent(event)