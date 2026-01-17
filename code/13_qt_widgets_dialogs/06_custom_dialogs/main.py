import sys
from PySide6.QtCore import Qt, QSettings
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication,
    QMainWindow, QTextEdit)
from settingsdialog import SettingsDialog

# 4. Use the dialog.

class Editor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Notes')
        self.resize(500, 300)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        self.settings = QSettings('./settings.ini',
            QSettings.Format.IniFormat)
        
        self.exit_action = QAction(self)
        self.exit_action.setText('E&xit')
        self.exit_action.setShortcut('Alt+X')
        self.exit_action.setIcon(QIcon('./icons/exit.png'))
        self.exit_action.triggered.connect(self.close)
        
        self.settings_action = QAction(self)
        self.settings_action.setText('&Settings')
        self.settings_action.setIcon(QIcon('./icons/settings.png'))
        self.settings_action.triggered.connect(self.show_settings)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(self.exit_action)
        
        tools_menu = menu_bar.addMenu('&Tools')
        tools_menu.addAction(self.settings_action)
        
        file_toolbar = self.addToolBar('File')
        file_toolbar.addAction(self.settings_action)
        file_toolbar.addAction(self.exit_action)
        file_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        
    def show_settings(self):
        dialog = SettingsDialog(self.settings, self)
        dialog.exec()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())
