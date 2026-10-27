from PySide6.QtGui import QColor, QPen, QPainter
from PySide6.QtWidgets import QStyle, QProxyStyle, QStyleFactory, QFrame


# 1. Create a custom style.

class MyProxyStyle(QProxyStyle):

    def __init__(self):

        super().__init__(QStyleFactory.create('Fusion'))

    def drawControl(self, element, option, painter, widget=None):
        
        # 2. Check if the element is a frame.

        if (element != QStyle.ControlElement.CE_ShapedFrame
                or option.frameShape != QFrame.Shape.StyledPanel):
            super().drawControl(element, option, painter, widget)
            return

        color = QColor('#7B5EA7')
        frame = option.rect.adjusted(14, 14, -14, -14)

        painter.save()
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # 3. Draw the rectangles.

        # Outer glow
        glow = QColor(color)
        glow.setAlpha(50)
        painter.setPen(QPen(glow, 7))
        painter.drawRect(frame)

        # Main border
        painter.setPen(QPen(color, 2))
        painter.drawRect(frame)

        # Inner border
        painter.setPen(QPen(color, 1))
        painter.drawRect(frame.adjusted(5, 5, -5, -5))

        painter.restore()
