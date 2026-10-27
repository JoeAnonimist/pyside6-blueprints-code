from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QGridLayout, QTabWidget,
    QLineEdit, QComboBox, QListWidget,
    QPushButton, QRadioButton, QCheckBox, QProgressBar, QSlider)


class WidgetFactory(QWidget):

    def __init__(self, style=None, parent=None):

        super().__init__(parent)
        self.setLayout(QGridLayout())

        self.line_edit = QLineEdit('A plain QLineEdit')

        self.combo_box = QComboBox()
        self.combo_box.setEditable(True)
        self.combo_box.addItems(['Editable QComboBox', 'Second item', 'Third item'])

        self.list_widget = QListWidget()
        self.list_widget.setAlternatingRowColors(True)
        self.list_widget.addItems([f'Row {i}' for i in range(1, 10)])
        self.list_widget.setCurrentRow(2)
        self.list_widget.setFixedHeight(100)

        self.enabled_button = QPushButton('Enabled')

        self.disabled_button = QPushButton('Disabled')
        self.disabled_button.setEnabled(False)

        self.radio_button = QRadioButton('A radio button')

        self.check_box = QCheckBox('A checkbox')

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(60)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setValue(40)

        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(QWidget(), 'Tab 1')
        self.tab_widget.addTab(QWidget(), 'Tab 2')
        self.tab_widget.setFixedHeight(60)

        self.layout().addWidget(self.line_edit, 0, 0)
        self.layout().addWidget(self.combo_box, 0, 1)
        self.layout().addWidget(self.list_widget, 1, 0, 1, 2)
        self.layout().addWidget(self.enabled_button, 2, 0)
        self.layout().addWidget(self.disabled_button, 2, 1)
        self.layout().addWidget(self.radio_button, 3, 0)
        self.layout().addWidget(self.check_box, 3, 1)
        self.layout().addWidget(self.progress_bar, 4, 0)
        self.layout().addWidget(self.slider, 4, 1)
        self.layout().addWidget(self.tab_widget, 5, 0, 1, 2)
