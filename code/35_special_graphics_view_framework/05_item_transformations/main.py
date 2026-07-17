import sys
from random import randint
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLineEdit, QComboBox, QGraphicsItem,
    QGraphicsView)

from customscene import Scene
from stickynoteitem import StickyNoteItem, Color


WIDTH = 150
HEIGHT = 150
SCENE_WIDTH = 600
SCENE_HEIGHT = 500


class Window(QWidget):

    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.scene = Scene()
        self.scene.setSceneRect(0, 0, SCENE_WIDTH, SCENE_HEIGHT)

        self.view = QGraphicsView(self.scene)
        self.view.setMouseTracking(True)
        layout.addWidget(self.view)
        
        inner_layout = QHBoxLayout()
        layout.addLayout(inner_layout)
        
        self.note_edit = QLineEdit()
        self.note_edit.setMaxLength(180)
        self.note_edit.setPlaceholderText('Note text...')
        
        self.color_combo = QComboBox()
        for i, color in enumerate(Color):
            self.color_combo.addItem(color.name.capitalize(), userData=color)
            self.color_combo.setItemData(
                i, color, Qt.ItemDataRole.UserRole)
            self.color_combo.setItemData(i, QBrush(color.light),
                Qt.ItemDataRole.BackgroundRole)
        
        self.add_button = QPushButton('Add Note')
        self.add_button.clicked.connect(self.add_note)
        
        inner_layout.addWidget(self.note_edit)
        inner_layout.addWidget(self.color_combo)
        inner_layout.addWidget(self.add_button)
        
    def get_random_coords(self):
        return (randint(1, SCENE_WIDTH - WIDTH), 
                randint(1, SCENE_HEIGHT - HEIGHT))
        
    def add_note(self):

        x, y = self.get_random_coords()
        color = self.color_combo.currentData(Qt.ItemDataRole.UserRole)
        text = self.note_edit.text()
        
        note = StickyNoteItem(color=color, text=text)
        note.setPos(x, y)
        note.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        note.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        self.scene.addItem(note)
        self.scene.notes.append(note)
        self.note_edit.clear()
        self.view.setFocus()
        note.setFocus()
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
