import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QInputDialog, QLabel, QWidget, QSizePolicy)


class Editor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Notes')
        self.resize(500, 300)
        
        self.note_title = ''
        self.title_label = QLabel('<i>Title not set</i>')

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        # 1. Provide a way for the user to invoke the dialog.
        
        self.set_title_action = QAction(self)
        self.set_title_action.setText('Set Title')
        self.set_title_action.setIcon(QIcon('./icons/untitled.png'))
        self.set_title_action.triggered.connect(self.set_note_title)

        self.exit_action = QAction(self)
        self.exit_action.setText('Exit')
        self.exit_action.setShortcut('Alt+X')
        self.exit_action.setIcon(QIcon('./icons/exit.png'))
        self.exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(self.exit_action)
        
        file_toolbar = self.addToolBar('File')
        file_toolbar.addAction(self.exit_action)
        file_toolbar.addAction(self.set_title_action)
        
        spacer = QWidget()
        spacer.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        file_toolbar.addWidget(spacer)

        file_toolbar.addWidget(self.title_label)
        
        file_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
    
    @Slot()
    def set_note_title(self):
        
        # 2. Show the dialog.
        
        note_title, ok = QInputDialog.getText(
            self, 'Note Title', 'Enter Note Title')

        # 3. Check the return values
        #    and handle the user response.

        if ok and note_title:
            self.note_title = note_title
            self.title_label.setText(f'Title: {note_title}')
            self.set_title_action.setIcon(
                QIcon('./icons/has_title.png'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())
