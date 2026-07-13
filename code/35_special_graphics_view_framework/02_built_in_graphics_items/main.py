import sys
from random import randint
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor, QBrush
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLineEdit, QComboBox, QGraphicsItem,
    QGraphicsView)

from customscene import Scene


COLORS = {
    'yellow':   ('#FFF4B2', '#FED900'),
    'green':    ('#E1FDD6', '#B4E4A2'),
    'pink':     ('#FFD9E5', '#FFB8CE'),
    'purple':   ('#EEDCFF', '#C8B0E0'),
    'blue':     ('#D4EEFF', '#A8D8F8'),
    'grey':     ('#E8E8E8', '#C8C8C8')
}

WIDTH = 150
HEIGHT = 150
SCENE_WIDTH = 600
SCENE_HEIGHT = 500


class Window(QWidget):

    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 2. Create the scene and view objects.

        self.scene = Scene()
        self.scene.setSceneRect(0, 0, SCENE_WIDTH, SCENE_HEIGHT)

        self.view = QGraphicsView(self.scene)
        layout.addWidget(self.view)
        
        inner_layout = QHBoxLayout()
        layout.addLayout(inner_layout)
        
        # 3. Add a line edit to enter note text, a combo box
        #    to select note color, and a push button
        #    to add note to the board.
        
        self.note_edit = QLineEdit()
        self.note_edit.setMaxLength(180)
        self.note_edit.setPlaceholderText('Note text...')
        
        self.color_combo = QComboBox()
        for i, (name, colors) in enumerate(COLORS.items()):
            self.color_combo.addItem(name)
            self.color_combo.setItemData(
                i, colors, Qt.ItemDataRole.UserRole)
            self.color_combo.setItemData(i, QBrush(colors[0]),
                Qt.ItemDataRole.BackgroundRole)
        
        self.add_button = QPushButton('Add Note')
        self.add_button.clicked.connect(self.add_note)
        
        inner_layout.addWidget(self.note_edit)
        inner_layout.addWidget(self.color_combo)
        inner_layout.addWidget(self.add_button)
        
    def get_random_coords(self):
        return (randint(1, SCENE_WIDTH - WIDTH), 
                randint(1, SCENE_HEIGHT - HEIGHT))
    
    # 4. Add the note to the board.
    
    def add_note(self):

        x, y = self.get_random_coords()
        colors = self.color_combo.currentData(Qt.ItemDataRole.UserRole)

        rect = self.scene.addRect(
            0, 0, WIDTH, HEIGHT,
            QPen(QColor(colors[1]), 2),
            QBrush(QColor(colors[0])))
        rect.setPos(x, y)

        label = self.scene.addText(self.note_edit.text())
        label.setDefaultTextColor(QColor('#333333'))
        label.setPos(x + 10, y + 10)
        label.setTextWidth(WIDTH - 20)
        self.note_edit.clear()
        
        group = self.scene.createItemGroup([rect, label])
        group.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        group.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
