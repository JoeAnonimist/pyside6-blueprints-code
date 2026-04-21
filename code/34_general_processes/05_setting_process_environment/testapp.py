import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
)

class SimpleStyleTest(QWidget):
    
    def __init__(self):
        
        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('<h2>Qt Widgets Style Test</h2>'))
        layout.addWidget(QLabel(
            f'<b>Current style:</b> {QApplication.style().objectName()}'
        ))
        override = os.environ.get('QT_STYLE_OVERRIDE', 'Not set')
        layout.addWidget(QLabel(
            f'<b>QT_STYLE_OVERRIDE:</b> {override}'
        ))
        layout.addWidget(QLabel(''))

        layout.addWidget(QLabel('Standard buttons:'))
        layout.addWidget(QPushButton('Button 1'))
        layout.addWidget(QPushButton('Button 2'))

        disabled = QPushButton('Disabled Button')
        disabled.setEnabled(False)
        layout.addWidget(disabled)

        layout.addStretch()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = SimpleStyleTest()
    window.show()
    sys.exit(app.exec())
