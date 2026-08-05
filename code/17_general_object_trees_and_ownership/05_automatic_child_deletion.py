import sys
import time
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QVBoxLayout)


class MyLabel(QLabel):

    def __init__(self, text='', parent=None):

        super().__init__(text, parent)
        self.setObjectName(self.text())
        self.destroyed.connect(MyLabel.on_destroyed)

    def __del__(self):
        print(f'__del__:      {self.objectName()}')
        
    @Slot()
    @staticmethod
    def on_destroyed(obj):
        print(f'destroyed():  {obj.objectName()}')


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        # Force deletion on close
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        
        self.setObjectName('MainWindow')
        self.setMinimumHeight(150)

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label1 = MyLabel('Label 1')
        layout.addWidget(label1)
        
        label2 = MyLabel('Label 2')
        layout.addWidget(label2)
        
        label3 = MyLabel('Label 3')
        
        self.label4 = MyLabel('Label 4')

        print('Label 1 parent:', label1.parent().objectName())
        print('Label 2 parent:', label2.parent().objectName())
        print('Label 3 parent:', label3.parent())
        print('Label 4 parent:', self.label4.parent())

        print('Window.__init__() end')
        
    def closeEvent(self, event):
        print('\nWindow close event\n')
        QWidget.closeEvent(self, event)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
