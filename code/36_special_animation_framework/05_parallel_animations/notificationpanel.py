from PySide6.QtCore import (Slot, QAbstractAnimation,
    QPropertyAnimation, QPoint, QParallelAnimationGroup,
    QEasingCurve)
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton,
    QVBoxLayout, QGraphicsOpacityEffect)


class NotificationPanel(QFrame):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.resize(200, 100)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.message_label = QLabel()
        self.message_label.setWordWrap(True)
        self.dismiss_button = QPushButton('Dismiss')
        self.dismiss_button.clicked.connect(self.hide_panel)

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
        
        # 1. Create the individual animations.
        
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)

        self.pos_animation = QPropertyAnimation(self, b'pos', self)
        self.pos_animation.setDuration(1000)

        self.opacity_animation = QPropertyAnimation(
            self.opacity_effect, b'opacity', self)
        self.opacity_animation.setDuration(1000)
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)
        
        # 2. Create the group and add both animations.
        
        self.anim_group = QParallelAnimationGroup(self)
        self.anim_group.addAnimation(self.pos_animation)
        self.anim_group.addAnimation(self.opacity_animation)

        self.opacity_effect.setOpacity(0.0)

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
        self.pos_animation.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.anim_group.setDirection(QAbstractAnimation.Direction.Forward)

        self.show()
        self.anim_group.start()
        
    @Slot()
    def hide_panel(self):
        self.opacity_animation.setDuration(300)
        self.pos_animation.setDuration(300)
        self.pos_animation.setEasingCurve(QEasingCurve.Type.Linear)
        self.anim_group.setDirection(QAbstractAnimation.Direction.Backward)
        self.anim_group.start()
        self.anim_group.finished.connect(self.deleteLater)
