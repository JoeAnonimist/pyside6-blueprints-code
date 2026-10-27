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
    
    # 4. Apply your custom style.

    app = QApplication(sys.argv)
    app.setStyle(MyProxyStyle())
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
