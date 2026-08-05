# The QTabWidget class provides a stack of tabbed widgets.

import sys
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QTabWidget, QRadioButton, QCheckBox)


class Window(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 1. Create the tab widget.

        self.tab_widget = QTabWidget()

        # 2. Create the widgets.

        notifications_widget = QWidget()
        notifications_layout = QVBoxLayout()
        notifications_layout.addWidget(QCheckBox('Low balance'))
        notifications_layout.addWidget(QCheckBox('Large transaction'))
        notifications_layout.addWidget(QCheckBox('Weekly summary'))
        notifications_widget.setLayout(notifications_layout)

        format_widget = QWidget()
        format_layout = QVBoxLayout()
        format_layout.addWidget(QRadioButton('PDF'))
        format_layout.addWidget(QRadioButton('CSV'))
        format_layout.addWidget(QRadioButton('OFX'))
        format_widget.setLayout(format_layout)

        # 3. Add tabs to the tab widget.

        self.tab_widget.addTab(
            notifications_widget, 'Notifications Triggers')
        self.tab_widget.addTab(format_widget, 'Export File Format')

        layout.addWidget(self.tab_widget)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
