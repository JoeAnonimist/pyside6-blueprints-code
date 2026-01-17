import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QFontDialog)


class Editor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Notes')
        self.resize(500, 300)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.exit_action = QAction(self)
        self.exit_action.setText('Exit')
        self.exit_action.setShortcut('Alt+X')
        self.exit_action.setIcon(QIcon('./icons/exit.png'))
        self.exit_action.triggered.connect(self.close)
        
        # 1. Create an action to trigger the dialog.
        
        self.font_action = QAction(self)
        self.font_action.setText('Set Font')
        self.font_action.setIcon(QIcon('./icons/font.png'))
        self.font_action.triggered.connect(self.set_font)
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(self.exit_action)
        
        format_menu = menu_bar.addMenu('F&ormat')
        format_menu.addAction(self.font_action)
        
        file_toolbar = self.addToolBar('File')
        file_toolbar.addAction(self.exit_action)
        file_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        
        format_toolbar = self.addToolBar('Format')
        format_toolbar.addAction(self.font_action)
        format_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
    
    # 2. Show the dialog to the user.
    
    @Slot()
    def set_font(self):

        initial = self.text_edit.currentCharFormat().font()
        ok, font = QFontDialog.getFont(initial, self, 'Choose Font')
        
        # 3. If the user presses Ok, update the font.
        
        if ok:
            self.text_edit.setCurrentFont(font)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())