from PySide6.QtCore import (Slot, QPropertyAnimation, QPoint,
    QAbstractAnimation, QSequentialAnimationGroup,
    QPauseAnimation)
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton,
    QVBoxLayout, QGraphicsOpacityEffect)


class NotificationPanel(QFrame):

    def __init__(self, hold_ms=2000, parent=None):

        super().__init__(parent)
        self.resize(200, 100)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.message_label = QLabel()
        self.message_label.setWordWrap(True)
        self.dismiss_button = QPushButton('Dismiss')
        self.dismiss_button.clicked.connect(self.dismiss)

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

        self.pos_animation = QPropertyAnimation(self, b'pos', self)
        self.pos_animation.setDuration(400)
        
        # 1. Create the animations.
        
        opacity_effect = QGraphicsOpacityEffect(self)
        opacity_effect.setOpacity(1.0)
        self.setGraphicsEffect(opacity_effect)
        
        self.opacity_animation = QPropertyAnimation(
            opacity_effect, b'opacity', self)
        self.opacity_animation.setDuration(400)
        self.opacity_animation.setStartValue(1.0)
        self.opacity_animation.setEndValue(0.0)
        
        # 2. Create the animation group and add the pause.

        self.animaton_group = QSequentialAnimationGroup(self)
        self.animaton_group.addAnimation(self.pos_animation)
        self.animaton_group.addPause(hold_ms)
        self.animaton_group.addAnimation(self.opacity_animation)

    def target_x(self):
        return (self.parent().width() - self.width()) // 2

    def target_y(self):
        return (self.parent().height() - self.height()) // 2

    @Slot()
    def dismiss(self):
        if self.opacity_animation.state() != QAbstractAnimation.State.Running:
            self.animaton_group.stop()
            self.opacity_animation.start()
            self.opacity_animation.finished.connect(self.deleteLater)

    @Slot(str)
    def show_panel(self, message=''):

        self.message_label.setText(message)
        
        starting_point = QPoint(-self.width(), self.target_y())
        end_point = QPoint(self.target_x(), self.target_y())
        
        self.pos_animation.setStartValue(starting_point)
        self.pos_animation.setEndValue(end_point)
        
        self.show()
        self.animaton_group.start()
