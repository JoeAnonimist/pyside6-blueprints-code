import sys
from PySide6.QtWidgets import (QApplication, QGroupBox,
    QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel,
    QFrame, QComboBox, QStyle)


STYLES = {
    'No QSS' : '',
    'Universal selector' : '* { background: orange; }',
    'Type selector' : 'QPushButton { background: orange; }',
    'Property selector':
        'QPushButton[orange="true"] { background: orange; }',
    'Class selector' : '.QPushButton { background: orange; }',
    'ID selector' : '#headingLabel { background: orange; }',
    'Descendant selector' : 'QGroupBox QLabel { background: orange; }',
    'Child selector' : 'QGroupBox > QPushButton { background: orange; }'
    }


class IconButton(QPushButton):
    
    def __init__(self, text='', parent=None):
        super().__init__(parent)
        icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_MessageBoxCritical)
        self.setText(text)
        self.setIcon(icon)


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
        
        heading_label = QLabel('Heading label')
        heading_label.setObjectName('headingLabel')
        groupbox_layout.addWidget(heading_label)

        save_button = QPushButton('Save')
        groupbox_layout.addWidget(save_button)
        
        delete_button = IconButton('Delete')
        groupbox_layout.addWidget(delete_button)
        
        flat_button = QPushButton('Flat button')
        flat_button.setProperty('orange', 'true')
        groupbox_layout.addWidget(flat_button)
        
        panel_frame = QFrame()
        panel_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        panel_layout = QVBoxLayout()
        panel_frame.setLayout(panel_layout)

        nested_label = QLabel('Nested label')
        panel_layout.addWidget(nested_label)

        nested_edit = QLineEdit()
        nested_edit.setPlaceholderText('Nested line edit')
        panel_layout.addWidget(nested_edit)
        
        nested_button = QPushButton('Nested button')
        panel_layout.addWidget(nested_button)
        
        groupbox_layout.addWidget(panel_frame)
        
        self.selector_combo = QComboBox()
        
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
