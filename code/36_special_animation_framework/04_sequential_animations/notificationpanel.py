from PySide6.QtCore import (Slot, QPropertyAnimation,
    QPoint, QSequentialAnimationGroup)
from PySide6.QtWidgets import (QFrame, QPushButton, QLabel,
    QVBoxLayout, QGraphicsOpacityEffect, QGraphicsDropShadowEffect)


class NotificationPanel(QFrame):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self.setFixedSize(200, 100)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.message_label = QLabel()
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
        
        # 1. Create the animations.
        
        self.pos_animation = QPropertyAnimation(self, b'pos', self)
        self.pos_animation.setDuration(500)
        
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.opacity_effect.setOpacity(0.0)
        self.message_label.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QPropertyAnimation(
            self.opacity_effect, b'opacity', self)
        self.opacity_animation.setDuration(500)
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)

        self.glow_effect = QGraphicsDropShadowEffect(self)
        self.glow_effect.setBlurRadius(0)
        self.glow_effect.setColor('orange')
        self.glow_effect.setOffset(0, 0)
        self.dismiss_button.setGraphicsEffect(self.glow_effect)
        
        self.glow_animation = QPropertyAnimation(
            self.glow_effect, b'blurRadius', self)
        self.glow_animation.setDuration(400)
        self.glow_animation.setStartValue(0)
        self.glow_animation.setEndValue(10)
        
        # 2. Create the animation group and add the animations.

        self.animation_group = QSequentialAnimationGroup(self)
        self.animation_group.addAnimation(self.pos_animation)
        self.animation_group.addAnimation(self.opacity_animation)
        self.animation_group.addAnimation(self.glow_animation)

    def target_x(self):
        return (self.parent().width() - self.width()) // 2
    
    def target_y(self):
        return (self.parent().height() - self.height()) // 2
    
    # 3. Start the animation group.
    
    @Slot(str)
    def show_panel(self, message=''):

        self.message_label.setText(message)
        
        starting_point = QPoint(-self.width(), self.target_y())
        end_point = QPoint(self.target_x(), self.target_y())

        self.pos_animation.setStartValue(starting_point)
        self.pos_animation.setEndValue(end_point)
        
        self.show()
        self.animation_group.start()
