from PySide6.QtCore import (QTimer, QPropertyAnimation,
    QEasingCurve, Property)
from PySide6.QtWidgets import (QWidget, QProgressBar,
    QLabel, QVBoxLayout)


BAR_QSS = '''
QProgressBar {
    max-height: 12px;
    background-color: #e0e0e0;
    border: 1px solid #a0a0a0;
}
QProgressBar::chunk {
    background-color: #4CAF50;
}
'''


# 1. Create a custom Qt widget and add a property to it.

class AnimatedBar(QWidget):
    
    def __init__(self, data_function, label='Load',  parent=None):

        super().__init__(parent)
        
        self._value = 0.0
        self._data_function = data_function
        self._label_prefix = label
        
        self.bar = QProgressBar()
        self.bar.setRange(0, 100)
        self.bar.setValue(0)
        self.bar.setTextVisible(False)
        self.bar.setStyleSheet(BAR_QSS)
        
        self.status_label = QLabel(f'{self._label_prefix}: 0%')

        layout = QVBoxLayout(self)
        layout.addWidget(self.status_label)
        layout.addWidget(self.bar)
        
        # 2. Add a QPropertyAnimation object to the widget.
        
        self.animation = QPropertyAnimation(self, b'value')
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.OutBounce)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.refresh)
        self.timer.start()
        
    def getValue(self):
        return self._value
    
    def setValue(self, value):
        if value != self._value:
            self._value = value
            self.bar.setValue(int(value))
            self.status_label.setText(
                f'{self._label_prefix}: {int(value)}%')
    
    value = Property(float, fget=getValue, fset=setValue)
    
    def refresh(self):
        
        # 3. Animate the property.

        if self.animation.state() != QPropertyAnimation.State.Stopped:
            self.animation.stop()
        self.animation.setStartValue(self.value)
        self.animation.setEndValue(self._data_function())
        self.animation.start()
