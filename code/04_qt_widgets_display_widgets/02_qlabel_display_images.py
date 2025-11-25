import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QHBoxLayout)

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # 1. Create a QPixmap object
        #    Optionally, resize it.

        pixmap = QPixmap('image.png')
        resized_pixmap = pixmap.scaledToWidth(
            100, Qt.TransformationMode.SmoothTransformation)
        
        # 2. Create a QLabel object
        
        png_label = QLabel()
        
        # 3. Set the label's pixmap
        
        # Same steps for animated gif
        
        png_label.setPixmap(resized_pixmap)
        layout.addWidget(png_label)
        
        animated_gif = QMovie('spinner.gif')
        animated_gif.setScaledSize(QSize(100, 100))
        animated_gif.start()
        
        gif_label = QLabel()
        gif_label.setMovie(animated_gif)
        layout.addWidget(gif_label)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
