import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QColorDialog)


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
        
        # 1. Provide a method for users to display the dialog
        
        self.fg_color_action = QAction(self)
        self.fg_color_action.setText('Text Color')
        self.fg_color_action.setIcon(QIcon('./icons/fgcolor.png'))
        self.fg_color_action.triggered.connect(
            self.set_foreground_color)
        
        self.bg_color_action = QAction(self)
        self.bg_color_action.setText('Background Color')
        self.bg_color_action.setIcon(QIcon('./icons/bgcolor.png'))
        self.bg_color_action.triggered.connect(
            self.set_background_color)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(self.exit_action)
        
        format_menu = menu_bar.addMenu('F&ormat')
        format_menu.addAction(self.fg_color_action)
        format_menu.addAction(self.bg_color_action)
        
        file_toolbar = self.addToolBar('File')
        file_toolbar.addAction(self.exit_action)
        file_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        
        format_toolbar = self.addToolBar('Format')
        format_toolbar.addAction(self.fg_color_action)
        format_toolbar.addAction(self.bg_color_action)
        format_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
    
    # 2. Show the dialog.
    
    def set_foreground_color(self):
        
        char_format = self.text_edit.currentCharFormat()
        initial_color = char_format.foreground().color()
        color = QColorDialog.getColor(
            initial_color, self, 'Set Text Color')
        
        # 3. If the dialog returns a valid color
        #    use it in your application.
        
        if color.isValid():
            if not self.text_edit.textCursor().hasSelection():
                self.text_edit.selectAll()
            self.text_edit.setTextColor(color)
            
    def set_background_color(self):

        char_format = self.text_edit.currentCharFormat()
        initial_color = char_format.background().color()

        if char_format.background().style() == Qt.BrushStyle.NoBrush:
            initial_color = Qt.GlobalColor.white

        bg_color = QColorDialog.getColor(
            initial_color, self, 'Set Background Color')
        if bg_color.isValid():
            if not self.text_edit.textCursor().hasSelection():
                self.text_edit.selectAll()
            self.text_edit.setTextBackgroundColor(bg_color)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())