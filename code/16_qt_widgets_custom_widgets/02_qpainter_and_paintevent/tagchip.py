from PySide6.QtCore import Signal, QSize, QRect, Qt
from PySide6.QtGui import QPainter, QColor, QBrush, QPen, QFont
from PySide6.QtWidgets import QWidget


class TagChip(QWidget):
    
    closed = Signal(str)
    
    def __init__(self, tag, parent=None):
        
        super().__init__(parent)
        
        self.chip_height = 28
        self.border_width = 1
        self.radius = 14
        self.text_padding = 14
        self.close_width = 28
        self.close_radius = 9
        self.close_padding = 4
        
        self.bg_color = '#e0d4f5'
        self.border_color = '#c4a4e8'
        self.close_color = '#4a2c8f'
        self.btn_hover_color = '#ebe2fa'
        
        self.tag = tag
        
        self.setMinimumHeight(self.chip_height)
        self.setMaximumHeight(self.chip_height)
        
    def sizeHint(self):
        font_metrics = self.fontMetrics()
        text_width = font_metrics.horizontalAdvance(self.tag)
        total_width = text_width + 2 * self.text_padding + self.close_width
        return QSize(total_width, self.chip_height)
    
    def get_close_rect(self):
        return QRect(
            self.width() - self.close_width + self.close_padding,
            self.close_padding,
            self.close_width - 2 * self.close_padding,
            self.chip_height - 2 * self.close_padding)
    
    def paintEvent(self, event):
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        
        rect = self.rect()

        painter.setBrush(QBrush(self.bg_color))
        painter.setPen(QPen(QColor(self.border_color)))
        
        # 1. Draw the widget shape.
        
        painter.drawRoundedRect(
            rect.adjusted(self.border_width,
                          self.border_width,
                          -self.border_width,
                          -self.border_width),
            self.radius, self.radius)
        
        painter.setPen(QColor(self.close_color))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        painter.setFont(font)
        
        # 2. Draw the widget text.
        
        text_rect = rect.adjusted(self.text_padding, 0, -self.close_width, 0)
        painter.drawText(text_rect, Qt.AlignmentFlag.AlignVCenter, self.tag)
        
        # 3. Draw the widget user interaction area.
        
        close_rect = self.get_close_rect()
        painter.setBrush(QColor(Qt.GlobalColor.transparent))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(close_rect.center(), self.close_radius, self.close_radius)
        
        painter.setPen(QColor(self.close_color))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        painter.setFont(font)
        
        painter.drawText(close_rect, Qt.AlignmentFlag.AlignCenter, '\u2715')
