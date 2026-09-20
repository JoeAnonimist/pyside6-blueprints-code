import sys
from PySide6.QtWidgets import (QApplication, QGroupBox,
    QComboBox, QWidget, QCheckBox, QVBoxLayout, QLabel,
    QPushButton)


STYLES = {
    'No QSS' : '',
    'Hover' : 'QCheckBox:hover { background: orange; }',
    'Pressed' : 'QCheckBox:pressed { background: orange; }',
    'Checked' : 'QCheckBox:checked { background: orange; }',
    'Indeterminate' : 'QCheckBox:indeterminate { background: orange; }',
    'Focus' : 'QCheckBox:focus { background: orange; }',
    'Disabled' : 'QCheckBox:disabled { background: orange; }',
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
        
        self.test_checkbox = QCheckBox('CheckBox')
        self.test_checkbox.setMinimumHeight(60)
        self.test_checkbox.setTristate(True)
        groupbox_layout.addWidget(self.test_checkbox)
        
        self.disable_button = QPushButton('Disable the checkbox')
        self.disable_button.setCheckable(True)
        self.disable_button.clicked.connect(self.toggle_checkbox_enabled)
        groupbox_layout.addWidget(self.disable_button)

        self.selector_combo = QComboBox()
        self.selector_combo.setEditable(False)
        
        for selector, qss in STYLES.items():
            self.selector_combo.addItem(selector, qss)
        
        self.selector_combo.currentIndexChanged.connect(self.set_style)
        layout.addWidget(self.selector_combo)
        
        self.qss_label = QLabel()
        layout.addWidget(self.qss_label)
        
        self.test_checkbox.setStyleSheet('border: 1px solid red;')

        
    def set_style(self, idx):
        qss = self.selector_combo.itemData(idx)
        self.groupbox.setStyleSheet(qss)
        self.qss_label.setText(qss)
        
    def toggle_checkbox_enabled(self):
        if self.disable_button.isChecked():
            self.test_checkbox.setEnabled(False)
        else:
            self.test_checkbox.setEnabled(True)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
