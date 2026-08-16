import sys
from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


def report_layer(layer, receiver, event):
    print(layer,
          f'rec: {receiver.objectName()}, ',
          f'evt id: {id(event)}, ',
          f'timer id: {event.timerId()}')


class TracingApplication(QApplication):

    def notify(self, receiver, event):
        if event.type() == QEvent.Type.Timer:
            report_layer('1. notify()       -', receiver, event)
        return super().notify(receiver, event)


class GlobalEventFilter(QObject):

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.Timer:
            report_layer('2. Global filter  -', watched, event)
        return super().eventFilter(watched, event)


class ObjectEventFilter(QObject):

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.Timer:
            report_layer('3. Object filter  -', watched, event)
        return super().eventFilter(watched, event)


class TrackedLabel(QLabel):
    
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setObjectName('label')
        timer_id = self.startTimer(2000)
        print(f'Timer id {timer_id} started\n')

    def event(self, event):
        if event.type() == QEvent.Type.Timer:
            report_layer('4. event()        -', self, event)
        return super().event(event)

    def timerEvent(self, event):
        report_layer('5. timerEvent()   -', self, event)


class TimerWidget(QWidget):

    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = TrackedLabel('A TrackedLabel')
        layout.addWidget(self.label)
        
        self.setObjectName('timer_widget')

        self.object_filter = ObjectEventFilter()
        self.label.installEventFilter(self.object_filter)

    def event(self, event):
        if event.type() == QEvent.Type.Timer:
            report_layer('4. event()        -', self, event)
        return super().event(event)

    def timerEvent(self, event):
        report_layer('5. timerEvent()   -', self, event)


if __name__ == '__main__':

    app = TracingApplication(sys.argv)
    global_filter = GlobalEventFilter()
    app.installEventFilter(global_filter)

    window = TimerWidget()
    window.show()
    
    window.windowHandle().installEventFilter(window.object_filter)

    sys.exit(app.exec())