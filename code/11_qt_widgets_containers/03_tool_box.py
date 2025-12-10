# The QToolBox class provides a column of tabbed widget items

import sys

from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QToolBox, QPushButton, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 1 - Create the toolbox
        
        toolbox = QToolBox()
        
        # 2 - Create the widgets (buttons in this case)
        
        windows_button = QPushButton('Windows')
        mac_button = QPushButton('Mac')
        linux_widget = QWidget()

        linux_widget.setLayout(QVBoxLayout())
        debian_button = QPushButton('Debian')
        arch_button = QPushButton('Arch')
        linux_widget.layout().addWidget(debian_button)
        linux_widget.layout().addWidget(arch_button)
        
        # 3 - Add widgets to the toolbox
        
        toolbox.addItem(windows_button, 'Win')
        toolbox.addItem(mac_button, 'Mac')
        toolbox.addItem(linux_widget, 'Lin')
        
        windows_button.clicked.connect(self.on_clicked)
        mac_button.clicked.connect(self.on_clicked)
        debian_button.clicked.connect(self.on_clicked)
        arch_button.clicked.connect(self.on_clicked)
        
        self.label = QLabel()

        layout.addWidget(toolbox)
        layout.addWidget(self.label)
        
    def on_clicked(self):
        self.label.setText(self.sender().text() + ' clicked!')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())
