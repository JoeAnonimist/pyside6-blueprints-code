import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from customwidgets import PropertyInspector


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.target_edit = QLineEdit()
        self.target_edit.setObjectName('Test widget')
        self.target_edit.setPlaceholderText(
            'Widget to be inspected - enter text here.')
        self.target_edit.setProperty('extraData', 'Runtime info')
        layout.addWidget(self.target_edit)
        
        # 3. Create a property inspector object.

        self.inspector = PropertyInspector(self.target_edit)
        layout.addWidget(self.inspector)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
