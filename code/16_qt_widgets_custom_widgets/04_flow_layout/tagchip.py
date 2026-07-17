from PySide6.QtCore import Signal, QSize, QRect, QRectF, Qt
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
        
        self.hover = False
        self.close_hover = False
        
        self.tag = tag
        
        self.setMouseTracking(True)
        
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
        
        text_rect = rect.adjusted(self.text_padding, 0, -self.close_width, 0)
        painter.drawText(text_rect, Qt.AlignmentFlag.AlignVCenter, self.tag)
        
        close_rect = self.get_close_rect()
        if self.close_hover:
            painter.setBrush(QColor(self.btn_hover_color))
        else:
            painter.setBrush(QColor(Qt.GlobalColor.transparent))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(QRectF(close_rect).center(), self.close_radius, self.close_radius)
        
        painter.setPen(QColor(self.close_color))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        painter.setFont(font)
        
        painter.drawText(close_rect, Qt.AlignmentFlag.AlignCenter, '\u2715')
        
    def enterEvent(self, event):
        self.hover = True
        self.update()
        super().enterEvent(event)
        
    def leaveEvent(self, event):
        self.hover = False
        self.close_hover = False
        self.update()
        super().leaveEvent(event)
        
    def mouseMoveEvent(self, event):
        close_rect = self.get_close_rect()
        new_close_hover = close_rect.contains(event.pos())
        if new_close_hover != self.close_hover:
            self.close_hover = new_close_hover
            self.update()
        super().mouseMoveEvent(event)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            close_rect = self.get_close_rect()
            if close_rect.contains(event.pos()):
                self.closed.emit(self.tag)
                return
        super().mousePressEvent(event)
        
    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
