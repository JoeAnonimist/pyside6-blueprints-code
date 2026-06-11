import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        self.setWindowTitle('Account Categories')
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # 1. Create QPixmap objects and a QMovie.

        housing_pixmap = QPixmap('housing.png')
        services_pixmap = QPixmap('online-services.png')
        utilities_pixmap = QPixmap('utilities.png')
        
        spinner_gif = QMovie('spinner.gif')
        spinner_gif.setScaledSize(QSize(24, 24))
        
        # 2. Create QLabel objects
        
        housing_label = QLabel()
        services_label = QLabel()
        utilities_label = QLabel()
        groceries_label = QLabel()
        
        housing_label.setToolTip('Housing')
        services_label.setToolTip('Online Services')
        utilities_label.setToolTip('Utilities')
        groceries_label.setToolTip('Groceries (loading...)')
        
        # 3. Set the labels' images.
        
        housing_label.setPixmap(housing_pixmap)
        services_label.setPixmap(services_pixmap)
        utilities_label.setPixmap(utilities_pixmap)
        groceries_label.setMovie(spinner_gif)
        spinner_gif.start()
        
        layout.addWidget(housing_label)
        layout.addWidget(services_label)
        layout.addWidget(utilities_label)
        layout.addWidget(groceries_label)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
