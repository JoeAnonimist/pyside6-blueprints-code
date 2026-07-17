from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QToolButton


# 1. Create the TagChip widget.

class TagChip(QFrame):

    closed = Signal(str)

    def __init__(self, tag, parent=None):

        super().__init__(parent)
        
        self.bg_color = '#e0d4f5'
        self.border_color = '#c4a4e8'
        self.close_color = '#4a2c8f'
        self.btn_hover_color = '#ebe2fa'

        self.tag = tag

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 2, 4, 2)
        layout.setSpacing(4)

        label = QLabel(tag)

        close_button = QToolButton()
        close_button.setText('\u2715')
        close_button.setCursor(
            Qt.CursorShape.PointingHandCursor)
        close_button.setAutoRaise(True)

        close_button.clicked.connect(
            lambda: self.closed.emit(self.tag))

        layout.addWidget(label)
        layout.addWidget(close_button)

        self.setStyleSheet(f'''
            TagChip {{
                background-color: {self.bg_color};
                border: 1px solid {self.border_color};
                border-radius: 10px;
            }}
            QToolButton {{
                border: none;
                background: transparent;
                padding: 0px;
                color: {self.close_color};
                font-weight: bold;
                border-radius: 7px;
            }}
            QToolButton:hover {{
                background: {self.btn_hover_color};
            }}
        ''')
