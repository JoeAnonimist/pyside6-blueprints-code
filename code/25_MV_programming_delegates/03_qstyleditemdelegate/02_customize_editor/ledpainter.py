from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QColor, QRadialGradient, QPainter, QBrush 

# 1. Extract the drawing logic into a standalone function.

def draw_led(painter, rect, value):

    diameter = min(rect.width(), rect.height()) - 8
    diameter = min(diameter, 24)
    x = rect.x() + (rect.width() - diameter) // 2
    y = rect.y() + (rect.height() - diameter) // 2
    led_rect = QRect(x, y, diameter, diameter)

    base_color = QColor('#22cc22') if value else QColor('#cc2222')
    dark_color = QColor('#116611') if value else QColor('#661111')

    gradient = QRadialGradient(
        led_rect.x() + diameter * 0.35,
        led_rect.y() + diameter * 0.30,
        diameter * 0.65
    )
    gradient.setColorAt(0.0, QColor(255, 255, 255, 220))
    gradient.setColorAt(0.25, base_color.lighter(140))
    gradient.setColorAt(0.7, base_color)
    gradient.setColorAt(1.0, dark_color)

    painter.save()
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    painter.setBrush(QBrush(QColor('#333333')))
    painter.setPen(Qt.PenStyle.NoPen)
    painter.drawEllipse(led_rect)

    dome_rect = led_rect.adjusted(2, 2, -2, -2)
    painter.setBrush(QBrush(gradient))
    painter.drawEllipse(dome_rect)
    painter.restore()
