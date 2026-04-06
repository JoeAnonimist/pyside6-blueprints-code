import sys
from PySide6.QtWidgets import (QApplication,
    QWidget, QPushButton, QVBoxLayout)
from customwidgets import ThemeSelector


THEMES = {
    'Light': ['#fcfcfc', '#333333'],
    'Dark': ['#2e3440', '#d8dee9'],
    'System': ['#f0f0f0', '#000000'],
    }

class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.theme_selector = ThemeSelector(THEMES)
        layout.addWidget(self.theme_selector)
        
        self.theme_selector.themeChanged.connect(self.apply_theme)
        self.apply_theme(self.theme_selector.theme)
        
        self.reset_button = QPushButton("Reset to Default")
        self.reset_button.clicked.connect(self.reset_theme)
        layout.addWidget(self.reset_button)
        
        for i in range(5):
            layout.addWidget(QPushButton(f'Widget {i}'))

    def reset_theme(self):

        # self.theme_selector.resetTheme()
        meta = self.theme_selector.metaObject()
        idx = meta.indexOfProperty('theme')
        if idx != -1:
            prop = meta.property(idx)
            prop.reset(self.theme_selector)
        else:
            print('Property "theme" not found.')
            
    def apply_theme(self, theme_name):
        
        if not theme_name or theme_name not in THEMES:
            return
        
        colors = THEMES[theme_name]
        
        QApplication.instance().setStyleSheet(
            f'''
            QWidget {{
                color: {colors[1]}; 
                background-color: {colors[0]};
            }}
            ''')
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
