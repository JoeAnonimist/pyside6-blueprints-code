import sys
from random import randint
from PySide6.QtGui import QPen, QColor, QBrush
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from graphicsview import GraphicsView
from customscene import Scene


COLORS = {
    'yellow':   ('#FED900', '#C9A800'),
    'green':    ('#B4E4A2', '#6DBF5B'),
    'pink':     ('#FFB8CE', '#E0658A'),
    'purple':   ('#C8B0E0', '#8E6BBF'),
    'blue':     ('#A8D8F8', '#3B8FCC'),
    'grey':     ('#C8C8C8', '#8C8C8C')
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
        
        # 3. Create a Scene and add items to it.

        self.scene = Scene()
        self.scene.setSceneRect(0, 0, SCENE_WIDTH, SCENE_HEIGHT)
        
        z = 0
        for _, (fill, border) in COLORS.items():
            x = randint(1, SCENE_WIDTH - WIDTH)
            y = randint(1, SCENE_HEIGHT - HEIGHT)
            pen = QPen(QColor(border), 2)
            brush = QBrush(QColor(fill))  
            rect = self.scene.addRect(0, 0, WIDTH, HEIGHT, pen, brush)
            rect.setPos(x, y)
            rect.setZValue(z)
            z += 1
            
        # 4. Create the GraphicsView
        #    and add it to the main window layout.

        self.view = GraphicsView(self.scene)
        self.view.setMouseTracking(True)
        layout.addWidget(self.view)
        
        self.status_label = QLabel()
        layout.addWidget(self.status_label)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
