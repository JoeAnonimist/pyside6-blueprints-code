import sys
from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import (QApplication, QWidget, 
    QPushButton, QVBoxLayout)


def report_layer(layer, receiver, event):
    x = int(event.position().x())
    y = int(event.position().y())
    print(layer,
          f'rec: {receiver.objectName()}, ',
          f'id: {id(event)}, ',
          f'pos: ({x}, {y})')


class TracingApplication(QApplication):

    def notify(self, receiver, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            report_layer('1. notify()          -', receiver, event)
        return super().notify(receiver, event)


class GlobalEventFilter(QObject):

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            report_layer('2. Global filter     -', watched, event)
        return super().eventFilter(watched, event)


class ObjectEventFilter(QObject):

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            report_layer('3. Object filter     -', watched, event)
        return super().eventFilter(watched, event)


class TrackedButton(QPushButton):

    def event(self, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            report_layer('4. event()           -', self, event)
        return super().event(event)

    def mousePressEvent(self, event):
        report_layer('5. mousePressEvent() -', self, event)
        super().mousePressEvent(event)


class MouseWidget(QWidget):

    def __init__(self):

        super().__init__()
        self.setObjectName('mouse_widget')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button = TrackedButton('Button')
        self.button.setObjectName('Button')

        self.object_filter = ObjectEventFilter()
        self.installEventFilter(self.object_filter)
        self.button.installEventFilter(self.object_filter)

        layout.addWidget(self.button)

    def event(self, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            report_layer('4. event()           -', self, event)
        return super().event(event)

    def mousePressEvent(self, event):
        report_layer('5. mousePressEvent() -', self, event)
        super().mousePressEvent(event)


if __name__ == '__main__':

    app = TracingApplication(sys.argv)
    global_filter = GlobalEventFilter()
    app.installEventFilter(global_filter)

    window = MouseWidget()
    window.show()
    window.windowHandle().installEventFilter(window.object_filter)

    sys.exit(app.exec())
