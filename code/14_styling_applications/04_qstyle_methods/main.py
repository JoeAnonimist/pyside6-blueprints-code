import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from customwidgets import WidgetFactory
from proxystyles import MyProxyStyle


class Window(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setMinimumWidth(400)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(WidgetFactory())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    style = MyProxyStyle()
    app.setStyle(style)

    window = Window()
    window.show()

    # Process the initial show/paint events 
    # and disable logging.
    app.processEvents()
    style.logging_enabled = False

    sys.exit(app.exec())
