# QFormLayout lets you create forms

import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, 
    QWidget, QFormLayout, QLineEdit, QLabel)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        # 1 - Create the layout and set it as the window layout
        
        layout = QFormLayout()
        self.setLayout(layout)
        
        # 2 - Create widgets
        #     Will need to access all widgets from the slot
        
        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.age_edit = QLineEdit()
        # The label will display entered data
        self.summary_label = QLabel()
        
        # 3 - Add widgets to the form
        #     QFormLayout will automagically add a label 
        #     for each widget based on the text you pass to addRow()
        
        layout.addRow('Name', self.name_edit)
        layout.addRow('e-mail', self.email_edit)
        layout.addRow('Age', self.age_edit)
        layout.addRow('Summary:', self.summary_label)
        
        # self.on_editing_finished() will handle events for all widgets.
        # editingFinished() is fired when Return is pressed
        # or the line edit loses focus.
        
        self.name_edit.editingFinished.connect(self.on_editing_finished)
        self.email_edit.editingFinished.connect(self.on_editing_finished)
        self.age_edit.editingFinished.connect(self.on_editing_finished)
    
    @Slot()    
    def on_editing_finished(self):
        
        self.summary_label.setText(
            f'Name:\t{self.name_edit.text()}\n' +
            f'e-mail:\t{self.email_edit.text()}\n' +
            f'Age:\t{self.age_edit.text()}')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())