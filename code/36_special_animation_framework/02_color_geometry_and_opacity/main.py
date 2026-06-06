import sys
import random
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication,QWidget,
    QVBoxLayout, QPushButton, QComboBox)
from notificationpanel import NotificationPanel, AnimationType


MESSAGES = [
    'Spending limit reached: Food & Drink',
    'Transfer of €250.00 completed',
    'Unusual activity detected on account',
    'Budget reset on 1 July']


class Window(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.resize(500, 300)

        self.anim_combo = QComboBox()
        for anim_type in AnimationType:
            self.anim_combo.addItem(anim_type.name, anim_type)

        self.show_button = QPushButton('Click for a notification!')
        self.show_button.clicked.connect(self.show_notification)
        
        layout = QVBoxLayout()
        layout.addWidget(self.anim_combo)
        layout.addWidget(self.show_button)
        layout.addStretch()
        self.setLayout(layout)

    @Slot()
    def show_notification(self):
        panel = NotificationPanel(self.anim_combo.currentData(), self)
        panel.show_panel(random.choice(MESSAGES))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
