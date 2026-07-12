from PySide6.QtGui import QTransform
from PySide6.QtWidgets import QGraphicsScene


# 1. Create a custom graphics scene
#    that supports  reordering items.

class Scene(QGraphicsScene):
    
    def mousePressEvent(self, event):

        item = self.itemAt(event.scenePos(), QTransform())
        if item:
            max_z = max(i.zValue() for i in self.items())
            item.setZValue(max_z + 1)
        super().mousePressEvent(event)