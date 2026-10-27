import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from proxystyles import MyProxyStyle
from customwidgets import WidgetFactory


class Window(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)
        layout.addWidget(WidgetFactory())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle(MyProxyStyle())
    window = Window()
    window.show()
    sys.exit(app.exec())