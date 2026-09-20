import sys
from PySide6.QtWidgets import (QApplication, QGroupBox,
    QComboBox, QWidget, QLineEdit, QVBoxLayout, QLabel)


STYLES = {
    'No QSS': '',
    'Color':
        'QLineEdit { color: orange; }',
    'Background color':
        'QLineEdit { background-color: #FFA500; }',
    'Font size + Padding': 
        'QLineEdit { font-size: 22px; padding: 12px; }',
    'Font':
        'QLineEdit { font: bold italic 18px Arial ; }',
    'Alignment':
        'QLineEdit { qproperty-alignment: AlignRight; }',
    'Border + Radius':
        'QLineEdit { border: 2px solid #555; '
        'border-radius: 12px; padding: 8px; }',
    'Gradient background':
        'QLineEdit { background: qlineargradient('
        'x1:0, y1:0, x2:0, y2:1, '
        'stop:0 #FFF8E1, stop:1 #FFBB33); }'
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
        
        self.line_edit = QLineEdit()
        self.line_edit.setMinimumHeight(80)
        font = self.line_edit.font()
        font.setPixelSize(18)
        self.line_edit.setFont(font)
        self.line_edit.setText('Styling properties with QSS')
        groupbox_layout.addWidget(self.line_edit)

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
