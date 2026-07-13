from PySide6.QtCore import QRectF, QPointF, Qt
from PySide6.QtGui import (QPainter, QBrush, QPen, QColor,
    QPolygonF, QPainterPath)
from PySide6.QtWidgets import QGraphicsItem
from enum import Enum


DOG_EAR = 25

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
    
    def __init__(self, width=150, height=180,
                 color=Color.YELLOW, text='', parent=None):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.color = color
        self.text = text
    
    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)
    
    def body_polygon(self):
        polygon = QPolygonF([
            QPointF(0, 0), QPointF(self.width, 0),
            QPointF(self.width, self.height - DOG_EAR),
            QPointF(self.width - DOG_EAR, self.height),
            QPointF(0, self.height)])
        return polygon
    
    def paint(self, painter, option, widget):
        
        pen_width = 2
        top_strip_height = 30
        
        # 1. Draw the sticky note body.

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(self.color.light)))
        painter.setPen(QPen(QColor(self.color.dark), pen_width))
        painter.drawPolygon(self.body_polygon())
        
        # 2. Draw the note header.
        
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor(self.color.dark)))
        painter.drawRect(0, 0, self.width, top_strip_height)
        
        # 3. Draw the dog-ear triangle.
        
        ear = QPolygonF([
            QPointF(self.width - DOG_EAR, self.height - DOG_EAR),
            QPointF(self.width, self.height - DOG_EAR),
            QPointF(self.width - DOG_EAR, self.height)])
        fold_color = QColor(self.color.light).darker(130)
        painter.setBrush(fold_color)
        painter.setPen(QPen(QColor(self.color.dark), pen_width))
        painter.drawPolygon(ear)
        
        # 4. Draw the text.
        
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
        
    def shape(self):
        path = QPainterPath()
        path.addPolygon(self.body_polygon())
        path.closeSubpath()
        return path
