from enum import Enum
from PySide6.QtCore import Slot, QPropertyAnimation, QRect
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QFrame, QPushButton,
    QVBoxLayout, QGraphicsOpacityEffect)
from customwidgets import ColoredLabel


class AnimationType(Enum):
    Color = 1
    Opacity = 2
    Geometry = 3


class NotificationPanel(QFrame):
    
    def __init__(self, anim_type=AnimationType.Color, parent=None):
        
        super().__init__(parent)
        self.resize(200, 100)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.message_label = ColoredLabel(color=QColor(220, 220, 220))
        self.message_label.setWordWrap(True)
        self.dismiss_button = QPushButton('Dismiss')
        self.dismiss_button.clicked.connect(self.deleteLater)
        
        layout.addWidget(self.message_label)
        layout.addWidget(self.dismiss_button)
        
        self.setStyleSheet('''
            QFrame {
                background-color: #f8f9fa;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            QLabel {
                qproperty-alignment: AlignCenter;
            }
        ''')
        
        # 1. Create a color animation.

        color_animation = QPropertyAnimation(self.message_label, b'color', self)
        color_animation.setDuration(1000)
        color_animation.setStartValue(QColor(250, 250, 0))
        color_animation.setEndValue(QColor(200, 250, 210))
        
        # 2. Create an opacity animation.
        
        opacity_effect = QGraphicsOpacityEffect(self)
        opacity_effect.setOpacity(1.0)
        self.setGraphicsEffect(opacity_effect)
        
        opacity_animation = QPropertyAnimation(
            opacity_effect, b'opacity', self)
        opacity_animation.setDuration(1000)
        opacity_animation.setStartValue(0.0)
        opacity_animation.setEndValue(1.0)
        
        # 3. Create a geometry animation.
        
        self.geometry_animation = QPropertyAnimation(
            self, b'geometry', self)
        self.geometry_animation.setDuration(200)
        
        # 4. Store the animations in a dictionary.
        
        self.animations = {
            AnimationType.Color: color_animation,
            AnimationType.Opacity: opacity_animation,
            AnimationType.Geometry: self.geometry_animation
        }
        
        self.active_animation = self.animations[anim_type]

    def target_x(self):
        return (self.parent().width() - self.width()) // 2
        
    def target_y(self):
        return (self.parent().height() - self.height()) // 2
    
    def setup_geometry_animation(self):
        final_rect = QRect(self.target_x(), self.target_y(),
                           self.width(), self.height())
        center_x = self.target_x() + self.width() // 2
        center_y = self.target_y() + self.height() // 2
        start_rect = QRect(center_x, center_y, 1, 1)
        self.geometry_animation.setStartValue(start_rect)
        self.geometry_animation.setEndValue(final_rect)
    
    @Slot(str)
    def show_panel(self, message=''):

        self.move(self.target_x(), self.target_y())
        self.setup_geometry_animation()        
        self.message_label.setText(message)
        self.show()
        self.active_animation.start()
    