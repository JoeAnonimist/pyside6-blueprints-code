import sys
import random
from PySide6.QtCore import Slot, QEasingCurve
from PySide6.QtWidgets import (QApplication,QWidget,
    QVBoxLayout, QPushButton, QComboBox)
from notificationpanel import NotificationPanel


MESSAGES = [
    'Spending limit reached: Food & Drink',
    'Transfer of €250.00 completed',
    'Unusual activity detected on account',
    'Budget reset on 1 July']


EXCLUDED_CURVE_TYPES = (
    QEasingCurve.Type.Custom,
    QEasingCurve.Type.NCurveTypes,
    QEasingCurve.Type.BezierSpline,
    QEasingCurve.Type.TCBSpline,
    QEasingCurve.Type.InCurve,
    QEasingCurve.Type.OutCurve,
    QEasingCurve.Type.SineCurve,
    QEasingCurve.Type.CosineCurve)


class Window(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.resize(500, 300)

        # 1. Populate the combo box.
        
        self.curves_combo = QComboBox()
        for curve in QEasingCurve.Type:
            if curve not in EXCLUDED_CURVE_TYPES:
                self.curves_combo.addItem(curve.name, curve)

        self.show_button = QPushButton('Click for a notification!')
        self.show_button.clicked.connect(self.show_notification)
        
        layout = QVBoxLayout()
        layout.addWidget(self.curves_combo)
        layout.addWidget(self.show_button)
        layout.addStretch()
        self.setLayout(layout)
    
    @Slot()
    def show_notification(self):
        
        # 2. Set the easing curve.

        curve = self.curves_combo.currentData()
        panel = NotificationPanel(self)
        panel.set_easing_curve(curve)
        
        # 3. Show the notification.
        
        panel.show_panel(random.choice(MESSAGES))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
