from PySide6.QtCore import (Slot, QPropertyAnimation,
    QPoint, QEasingCurve)
from PySide6.QtWidgets import QFrame, QPushButton, QLabel, QVBoxLayout


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
        
        self.animation = QPropertyAnimation(self, b'pos', self)
        self.animation.setDuration(500)

    def target_x(self):
        return (self.parent().width() - self.width()) // 2
    
    def target_y(self):
        return (self.parent().height() - self.height()) // 2
    
    @Slot(QEasingCurve.Type)
    def set_easing_curve(self, curve):
        self.animation.setEasingCurve(curve)

    @Slot(str)
    def show_panel(self, message=''):
        
        self.message_label.setText(message)
        
        starting_point = QPoint(-self.width(), self.target_y())
        end_point = QPoint(self.target_x(), self.target_y())
        
        self.animation.setStartValue(starting_point)
        self.animation.setEndValue(end_point)
        
        self.show()
        self.animation.start()
