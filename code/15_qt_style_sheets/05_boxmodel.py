import sys
from PySide6.QtWidgets import (QApplication, QGroupBox,
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpinBox)


STYLE = '''
QGroupBox {
    background-color: white;
}

QLabel {
    border: 1px solid orange;
    background-color: #BFBFBF;
}

#controlLabel {
    margin-top: 10px;
}
'''


class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.resize(400, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.groupbox = QGroupBox()
        self.groupbox.setStyleSheet(STYLE)
        self.groupbox.setFlat(True)
        groupbox_layout = QVBoxLayout()
        self.groupbox.setLayout(groupbox_layout)
        layout.addWidget(self.groupbox)

        self.styled_label = QLabel('Styled Label')
        groupbox_layout.addWidget(self.styled_label)

        self.control_label = QLabel('Control Label')
        self.control_label.setObjectName('controlLabel')
        groupbox_layout.addWidget(self.control_label)

        self.margin_spin = QSpinBox()
        self.margin_spin.setRange(0, 200)
        self.margin_spin.valueChanged.connect(self.update_style)
        margin_layout = QHBoxLayout()
        margin_layout.addWidget(QLabel('Margin'))
        margin_layout.addWidget(self.margin_spin)
        layout.addLayout(margin_layout)

        self.border_spin = QSpinBox()
        self.border_spin.setRange(0, 200)
        self.border_spin.valueChanged.connect(self.update_style)
        border_layout = QHBoxLayout()
        border_layout.addWidget(QLabel('Border'))
        border_layout.addWidget(self.border_spin)
        layout.addLayout(border_layout)

        self.padding_spin = QSpinBox()
        self.padding_spin.setRange(0, 200)
        self.padding_spin.valueChanged.connect(self.update_style)
        padding_layout = QHBoxLayout()
        padding_layout.addWidget(QLabel('Padding'))
        padding_layout.addWidget(self.padding_spin)
        layout.addLayout(padding_layout)

        self.update_style()

    def update_style(self):
        user_style = f'''
            QLabel {{
                margin: {self.margin_spin.value()}px;
                border: {self.border_spin.value()}px solid orange;
                padding: {self.padding_spin.value()}px;
            }}
        '''
        self.styled_label.setStyleSheet(user_style)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())