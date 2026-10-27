import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor, QBrush
from PySide6.QtWidgets import (QApplication, QStyleFactory,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,
    QComboBox)


def make_color_item(color):
    
    item = QTableWidgetItem(color.name())
    item.setBackground(color)
    lum = 0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue()
    item.setForeground(Qt.black if lum > 127 else Qt.white)
    item.setTextAlignment(Qt.AlignCenter)
    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    return item


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.resize(350, 700)
        
        self.combo = QComboBox()
        for key in QStyleFactory.keys():
            self.combo.addItem(key.lower())
        self.combo.setCurrentText(QApplication.style().name())
        self.combo.currentTextChanged.connect(self.change_style)
        
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(
            ['Role', 'palette()', 'standardPalette()'])
        
        self.roles = []
        for role in QPalette.ColorRole:
            if role in (QPalette.ColorRole.NoRole,
                        QPalette.ColorRole.NColorRoles):
                continue
            self.roles.append(role)
            
        self.table.setRowCount(len(self.roles))
        
        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.table)
        self.setLayout(layout)
        
        self.rebuild()

    def change_style(self, name):
        QApplication.setStyle(name)
        self.rebuild()

    def rebuild(self):

        name = QApplication.style().name()
        app_palette = QApplication.palette()
        standard_palette = QStyleFactory.create(name).standardPalette()

        for row, role in enumerate(self.roles):
            themed = app_palette.color(role)
            standard = standard_palette.color(role)

            name_item = QTableWidgetItem(role.name)
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
            if themed.name() != standard.name():
                name_item.setBackground(QBrush(QColor('#fff3cd')))

            self.table.setItem(row, 0, name_item)
            self.table.setItem(row, 1, make_color_item(themed))
            self.table.setItem(row, 2, make_color_item(standard))


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
