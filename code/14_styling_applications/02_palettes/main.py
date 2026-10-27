import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import (QApplication, QStyleFactory,
    QWidget, QComboBox, QVBoxLayout, QColorDialog, QPushButton)
from customwidgets import WidgetFactory


ROLES = (QPalette.ColorRole.Window, QPalette.ColorRole.WindowText,
         QPalette.ColorRole.Base, QPalette.ColorRole.Text,
         QPalette.ColorRole.Button, QPalette.ColorRole.ButtonText,
         QPalette.ColorRole.Highlight, QPalette.ColorRole.HighlightedText,
         QPalette.ColorRole.AlternateBase,QPalette.ColorRole.Midlight)


class Window(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setMinimumWidth(400)
        self.setLayout(QVBoxLayout())
        
        self.style_combo = QComboBox()
        
        # 1. Add the styles combobox.
        
        for key in QStyleFactory.keys():
            self.style_combo.addItem(key)
            
        current_style = QApplication.style().name()
        idx = self.style_combo.findText(
            current_style, Qt.MatchFlag.MatchFixedString)
        self.style_combo.setCurrentIndex(idx)
        
        # 2. Add the color roles combobox.

        self.role_combo = QComboBox()        
        for role in ROLES:
            self.role_combo.addItem(role.name, role)
            
        # 3. Add the color groups combobox.

        self.group_combo = QComboBox()
        for group in QPalette.ColorGroup:
            if group != QPalette.ColorGroup.NColorGroups:
                self.group_combo.addItem(group.name, group)
        
        # 4. Add the select color button.
        
        self.color_button = QPushButton('Select a color')
        
        # 5. Connect the signals.
        
        self.style_combo.currentIndexChanged.connect(self.set_style)
        self.role_combo.currentIndexChanged.connect(self.apply_palette)
        self.group_combo.currentIndexChanged.connect(self.apply_palette)
        self.color_button.clicked.connect(self.set_color)
        
        self.layout().addWidget(self.style_combo)
        self.layout().addWidget(self.role_combo)
        self.layout().addWidget(self.group_combo)
        self.layout().addWidget(self.color_button)
        
        self.widget_factory = WidgetFactory()
        
        self.layout().addWidget(self.widget_factory)
        
        self.original_palette = QApplication.palette()
        self.color = QColor('green')
        self.color_button.setStyleSheet('background-color: green')
        self.apply_palette()

        
    @Slot(int)
    def set_style(self, idx):
        style_name = self.style_combo.itemText(idx)
        style = QStyleFactory.create(style_name)
        QApplication.setStyle(style)
        
    def set_color(self):
        ret_color = QColorDialog.getColor(parent=self)
        if ret_color.isValid():
            self.color = ret_color
            self.apply_palette()
    
    # 6. Apply the palette to the selected group and role.
    
    def apply_palette(self):
        color_name = self.color.name(QColor.NameFormat.HexRgb)
        palette = QPalette(self.original_palette)
        palette.setColor(
            self.group_combo.currentData(),
            self.role_combo.currentData(),
            self.color)
        self.color_button.setStyleSheet(f'background-color: {color_name}')
        self.widget_factory.setPalette(palette)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    style = QStyleFactory.create('Fusion')
    QApplication.setStyle(style)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
