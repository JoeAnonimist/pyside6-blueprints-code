# The QTabWidget class provides a stack of tabbed widgets.  :S
# ie. tabs

import sys

from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QTabWidget, QRadioButton, QCheckBox)


class Window(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 1 - Create the tab widget

        self.tab_widget = QTabWidget()

        # 2 - Create some widgets
        #     A tab contains only one widget
        #     but that widget can be a QWidget instance
        #     or some other container.

        # Tab 0 widgets:

        styles = QWidget()
        styles_layout = QVBoxLayout()
        styles_layout.addWidget(QCheckBox('Heading'))
        styles_layout.addWidget(QCheckBox('Paragraph'))
        styles_layout.addWidget(QCheckBox('List'))
        styles.setLayout(styles_layout)

        # Tab 1 widgets

        margins = QWidget()
        margins_layout = QVBoxLayout()
        margins_layout.addWidget(QRadioButton('Normal'))
        margins_layout.addWidget(QRadioButton('Wide'))
        margins_layout.addWidget(QRadioButton('Narrow'))
        margins.setLayout(margins_layout)

        # 3 - Add tabs to the widget

        self.tab_widget.addTab(styles, 'Styles')
        self.tab_widget.addTab(margins, 'Margins')

        layout.addWidget(self.tab_widget)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
