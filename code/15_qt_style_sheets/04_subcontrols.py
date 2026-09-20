import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QGroupBox, QComboBox,
    QWidget, QSlider, QTabBar, QCheckBox, QVBoxLayout, QLabel)


STYLES = {
    'No QSS' : '',
    'Slider groove' : 'QSlider::groove { background: orange; } ',
    'Slider handle' : 'QSlider::handle { background: orange; }',
    'Tabbar tab' : 'QTabBar::tab { background: orange; }',
    'Tabbar tear' : 'QTabBar::tear { background: orange; }',
    'Checkbox indicator' : 'QCheckBox::indicator { background: orange; }'
        'QCheckBox::indicator:checked { background: green; }',
    'Combobox dropdown' : 'QComboBox::drop-down { background: orange; }'
        'QComboBox::down-arrow { background: green; }',
    'Groupbox title': 'QGroupBox::title { background: orange; }'
    }


class Window(QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setMinimumWidth(400)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.groupbox = QGroupBox('Widget gallery')
        groupbox_layout = QVBoxLayout()
        self.groupbox.setLayout(groupbox_layout)
        layout.addWidget(self.groupbox)
        
        self.slider = QSlider()
        self.slider.setValue(50)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        groupbox_layout.addWidget(self.slider)
        
        self.tabbar = QTabBar()
        self.tabbar.setMaximumWidth(380)
        self.tabbar.setUsesScrollButtons(True)
        self.tabbar.setElideMode(Qt.TextElideMode.ElideNone)
        for i in range(1, 10):
            self.tabbar.addTab(f'Tab {i}')
        self.tabbar.setCurrentIndex(8)
        groupbox_layout.addWidget(self.tabbar)
        
        self.checkbox = QCheckBox('checkbox')
        groupbox_layout.addWidget(self.checkbox)
        
        self.combobox = QComboBox()
        self.combobox.addItems(['Item 1', 'Item 2', 'Item 3'])
        groupbox_layout.addWidget(self.combobox)
        
        self.selector_combo = QComboBox()
        self.selector_combo.setEditable(False)
        
        for selector, qss in STYLES.items():
            self.selector_combo.addItem(selector, qss)
        
        self.selector_combo.currentIndexChanged.connect(self.set_style)
        layout.addWidget(self.selector_combo)
        
        self.qss_label = QLabel()
        layout.addWidget(self.qss_label)        

        
    def set_style(self, idx):
        qss = self.selector_combo.itemData(idx)
        self.groupbox.setStyleSheet(qss)
        self.qss_label.setText(qss)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
