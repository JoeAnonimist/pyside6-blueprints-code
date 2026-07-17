from PySide6.QtCore import QRectF, QPointF, Qt
from PySide6.QtGui import (QPainter, QBrush, QPen, QColor,
    QPolygonF, QPainterPath, QImage)
from PySide6.QtWidgets import (QGraphicsItem,
    QGraphicsDropShadowEffect, QStyle)
from enum import Enum


DOG_EAR = 25
EXPANDED_SCALE = 1.4
TILT_ANGLE = 3


class Color(Enum):

    YELLOW = ('#FFF4B2', '#FED900')
    GREEN = ('#E1FDD6', '#B4E4A2')
    PINK = ('#FFD9E5', '#FFB8CE')
    PURPLE = ('#EEDCFF', '#C8B0E0')
    BLUE = ('#D4EEFF', '#A8D8F8')
    GREY = ('#E8E8E8', '#C8C8C8')
    
    @property
    def light(self):
        return self.value[0]
    
    @property
    def dark(self):
        return self.value[1]


class StickyNoteItem(QGraphicsItem):
    
    lock_image = QImage('locked.png')
    
    def __init__(self, width=150, height=180,
                 color=Color.YELLOW, text='', parent=None):

        super().__init__(parent)

        self.width = width
        self.height = height
        self.color = color
        self.text = text
        
        self.locked = False
        self.expanded = False
        self.lock_rect = QRectF(2, 2, 26, 26)
        
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(5)
        self.shadow.setYOffset(5)
        self.shadow.setColor(QColor(130, 130, 130))
        self.setGraphicsEffect(self.shadow)

        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)

    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)
    
    def body_polygon(self):
        polygon = QPolygonF([
            QPointF(0, 0), QPointF(self.width, 0),
            QPointF(self.width, self.height - DOG_EAR),
            QPointF(self.width - DOG_EAR, self.height),
            QPointF(0, self.height)])
        return polygon
    
    def hoverEnterEvent(self, event):
        self.shadow.setColor(QColor(100, 100, 100))
        
    def hoverLeaveEvent(self, event):
        self.shadow.setColor(QColor(130, 130, 130))
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Delete:
            self.scene().remove_note(self)
        else:
            super().keyPressEvent(event)
    
    # 1. Set the transform origin to the note's center.
    
    def mousePressEvent(self, event):
        if self.lock_rect.contains(event.pos()):
            self.locked = not self.locked
            self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable,
                         not self.locked)
            self.update()
            if self.scene():
                self.scene().clearSelection()
        else:
            self.setFocus()
            if not self.locked and not self.expanded:
                self.setTransformOriginPoint(self.boundingRect().center())
            super().mousePressEvent(event)
    
    # 2. Tilt the note as it's dragged.
    
    def mouseMoveEvent(self, event):
        if not self.locked:
            dx = event.scenePos().x() - event.lastScenePos().x()
            if dx > 0:
                self.setRotation(TILT_ANGLE)
            elif dx < 0:
                self.setRotation(-TILT_ANGLE)
            else:
                self.setRotation(0)
        super().mouseMoveEvent(event)
    
    # 3. Straighten the note back once it's released.
    
    def mouseReleaseEvent(self, event):
        self.setRotation(0)
        super().mouseReleaseEvent(event)
    
    # 4. Expand/collapse the note on double-click.
    
    def mouseDoubleClickEvent(self, event):
        self.expanded = not self.expanded
        if self.expanded:
            self.setTransformOriginPoint(event.pos())
            self.setScale(EXPANDED_SCALE)
        else:
            self.setScale(1.0)
        event.accept()
    
    # 5. Automatically collapse an expanded note
    #    once it loses focus.
    
    def focusOutEvent(self, event):
        if self.expanded:
            self.expanded = False
            self.setScale(1.0)
        super().focusOutEvent(event)
    
    def paint(self, painter, option, widget):
        
        pen_width = 2
        top_strip_height = 30

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(self.color.light)))
        painter.setPen(QPen(QColor(self.color.dark), pen_width))
        painter.drawPolygon(self.body_polygon())
        
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor(self.color.dark)))
        painter.drawRect(0, 0, self.width, top_strip_height)
        
        ear = QPolygonF([
            QPointF(self.width - DOG_EAR, self.height - DOG_EAR),
            QPointF(self.width, self.height - DOG_EAR),
            QPointF(self.width - DOG_EAR, self.height)])
        fold_color = QColor(self.color.light).darker(130)
        painter.setBrush(fold_color)
        painter.setPen(QPen(QColor(self.color.dark), pen_width))
        painter.drawPolygon(ear)
        
        painter.save()
        cx = self.lock_rect.center().x()
        cy = self.lock_rect.center().y()
        if not self.locked:
            painter.translate(cx, cy)
            painter.rotate(45)
            painter.translate(-cx, -cy)
            painter.setOpacity(0.4)
        painter.drawImage(self.lock_rect.toRect(), StickyNoteItem.lock_image)
        painter.restore()
        
        if self.text:
            padding = 8
            text_rect = QRectF(
                padding,
                top_strip_height + padding,
                self.width - padding * 2,
                self.height - top_strip_height - DOG_EAR - padding)
            painter.setPen(QPen(QColor('#333333')))
            flags = (Qt.AlignmentFlag.AlignLeft |
                    Qt.AlignmentFlag.AlignTop |
                    Qt.TextFlag.TextWordWrap)
            painter.drawText(text_rect, flags, self.text)
            
        if option.state & QStyle.StateFlag.State_Selected:
            painter.save()
            painter.setPen(QPen(QColor('#4A90D9'), 1))
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawPolygon(self.body_polygon())
            painter.restore()
        
    def shape(self):
        path = QPainterPath()
        path.addPolygon(self.body_polygon())
        path.closeSubpath()
        return path
