import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication, QStyleFactory,
    QWidget, QComboBox, QVBoxLayout)
from customwidgets import WidgetFactory


class Window(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setMinimumWidth(400)
        self.setLayout(QVBoxLayout())
        
        self.style_combo = QComboBox()
        
        # 1. Populate a combobox with available Qt styles.
        
        for key in QStyleFactory.keys():
            self.style_combo.addItem(key)
            
        current_style = QApplication.style().name()
        idx = self.style_combo.findText(
            current_style,
            Qt.MatchFlag.MatchFixedString)
        self.style_combo.setCurrentIndex(idx)
        
        # 2. Connect the currentIndexChanged() signal to a slot.
        
        self.style_combo.currentIndexChanged.connect(self.set_style)
        
        self.layout().addWidget(self.style_combo)
        self.layout().addWidget(WidgetFactory())

    # 3. Apply selected style.
        
    @Slot(int)
    def set_style(self, idx):

        style_name = self.style_combo.itemText(idx)
        style = QStyleFactory.create(style_name)
        QApplication.setStyle(style)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    style = QStyleFactory.create('Fusion')
    QApplication.setStyle(style)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
