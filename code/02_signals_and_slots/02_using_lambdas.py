import sys
from PySide6.QtWidgets import (QApplication, 
    QWidget, QLabel, QPushButton, QVBoxLayout)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        self.setWindowTitle('Category selector')
        self.setMinimumWidth(150)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.category_label = QLabel('Category: -')
        layout.addWidget(self.category_label)
        
        # 1. Create three buttons and connect each to a lambda.
        #    The lambda is an anonymous function - it has no name.
        
        for category in ('Income', 'Expense', 'Transfer'):
            button = QPushButton(category)
            button.clicked.connect(
                lambda checked, c=category: self.select_category(c))
            layout.addWidget(button)
    
    # 2. A single named slot handles all three buttons.

    def select_category(self, category):
        self.category_label.setText(f'Category: {category}')
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
