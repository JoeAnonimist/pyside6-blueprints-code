import sys
from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import (QApplication, QWidget,
    QLineEdit, QVBoxLayout)


def report_layer(layer, receiver, event):
    print(layer,
          f'rec: {receiver.objectName()}, ',
          f'id: {id(event)}, ',
          f'key: {event.key()}')


class TracingApplication(QApplication):

    def notify(self, receiver, event):
        if event.type() == QEvent.Type.KeyPress:
            report_layer('1. notify()          -', receiver, event)
        return super().notify(receiver, event)


class GlobalEventFilter(QObject):

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.KeyPress:
            report_layer('2. Global filter     -', watched, event)
        return super().eventFilter(watched, event)


class ObjectEventFilter(QObject):

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.KeyPress:
            report_layer('3. Object filter     -', watched, event)
        return super().eventFilter(watched, event)


class TrackedLineEdit(QLineEdit):

    def event(self, event):
        if event.type() == QEvent.Type.KeyPress:
            report_layer('4. event()           -', self, event)
        return super().event(event)

    def keyPressEvent(self, event):
        report_layer('5. keyPressEvent() -', self, event)
        super().keyPressEvent(event)


class KeyWidget(QWidget):

    def __init__(self):

        super().__init__()
        self.setObjectName('key_widget')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.line_edit = TrackedLineEdit(
            'Type a letter, then try Escape')
        self.line_edit.setObjectName('LineEdit')

        self.object_filter = ObjectEventFilter()
        self.installEventFilter(self.object_filter)
        self.line_edit.installEventFilter(self.object_filter)

        layout.addWidget(self.line_edit)

    def event(self, event):
        if event.type() == QEvent.Type.KeyPress:
            report_layer('4. event()           -', self, event)
        return super().event(event)

    def keyPressEvent(self, event):
        report_layer('5. keyPressEvent() -', self, event)
        super().keyPressEvent(event)


if __name__ == '__main__':

    app = TracingApplication(sys.argv)
    global_filter = GlobalEventFilter()
    app.installEventFilter(global_filter)

    window = KeyWidget()
    window.show()
    window.line_edit.setFocus()
    window.windowHandle().installEventFilter(window.object_filter)

    sys.exit(app.exec())
