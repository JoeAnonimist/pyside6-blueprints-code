from PySide6.QtGui import QTransform
from PySide6.QtWidgets import QGraphicsView


# 2. Create a custom graphics view and implement
#    zooming in and out on mouse wheel scroll,
#    and logging mouse pointer position changes
#    in scene, view, and item-local coordinates.

class GraphicsView(QGraphicsView):

    def wheelEvent(self, event):
        factor = 1.15
        if event.angleDelta().y() > 0:
            self.scale(factor, factor)
        else:
            self.scale(1 / factor, 1 / factor)

    def mouseMoveEvent(self, event):

        scene_pos = self.mapToScene(event.position().toPoint())
        view_pos = self.mapFromScene(scene_pos)

        text = f'Scene ({scene_pos.x():.0f}, {scene_pos.y():.0f})  ' \
               f'View ({view_pos.x()}, {view_pos.y()})  '

        item = self.scene().itemAt(scene_pos, QTransform())
        if item is not None:
            item_pos = item.mapFromScene(scene_pos)
            text += f'Item ({item_pos.x():.0f}, {item_pos.y():.0f})'
            
        self.window().status_label.setText(text)
        super().mouseMoveEvent(event)
