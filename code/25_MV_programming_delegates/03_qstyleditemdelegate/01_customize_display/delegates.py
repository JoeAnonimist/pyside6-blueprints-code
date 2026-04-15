from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QBrush, QRadialGradient, QColor
from PySide6.QtWidgets import QStyledItemDelegate


# 1. Subclass QStyledItemDelegate

class LedDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):

        value = index.data(Qt.ItemDataRole.EditRole)
        self.draw_led(painter, option.rect, value)
        super().paint(painter, option, index)

    # 2. Draw the delegate

    def draw_led(self, painter, rect, value):

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
