import sys
import psutil
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from customwidgets import AnimatedBar


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.cpu_widget = AnimatedBar(
            data_function=lambda: psutil.cpu_percent(interval=None),
            label='CPU')
        
        self.ram_widget = AnimatedBar(
            data_function=lambda: psutil.virtual_memory().percent,
            label='RAM')
        
        layout.addWidget(self.cpu_widget)
        layout.addWidget(self.ram_widget)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
