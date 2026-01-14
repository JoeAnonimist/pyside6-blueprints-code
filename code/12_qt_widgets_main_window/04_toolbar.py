# The QToolBar class provides a movable 
# panel that contains a set of controls.

import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QLabel, QMessageBox)


class QEditor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Editor')
        self.resize(500, 300)

        self.text_edit = QTextEdit()        
        self.setCentralWidget(self.text_edit)

        self.position_label = QLabel()
        self.charcount_label = QLabel()
        self.statusBar().addWidget(self.position_label)
        self.statusBar().addPermanentWidget(self.charcount_label)
        
        self.text_edit.textChanged.connect(self.update_stats)
        self.text_edit.selectionChanged.connect(
            self.show_selection_size)
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        
        # You can add icons to QActions.
        # Icons are shown both in the menu and in the toolbar.
        # The icons used here are from the Tango project.
        
        exit_action = QAction(self)
        exit_action.setText('Exit')
        exit_action.setShortcut('Alt+X')
        exit_action.setIcon(QIcon('./icons/exit.png'))
        exit_action.triggered.connect(QApplication.quit)
        
        file_menu.addAction(exit_action)
          
        help_menu = menu_bar.addMenu('&Help')
        
        about_action = QAction(self)
        about_action.setText('About')
        about_action.setShortcut('Alt+A')
        about_action.setIcon(QIcon('./icons/about.png'))
        about_action.triggered.connect(self.show_messagebox)
        
        help_menu.addAction(about_action)
        
        # 1 - Create the toolbar
        
        file_toolbar = self.addToolBar('File')
        
        # 2 - Add actions to it. We reuse the same actions
        #     that we used for the menu.
        
        file_toolbar.addAction(exit_action)
        file_toolbar.addAction(about_action)
        
        # 3 - ... and that's about it. Here we just
        #     set the icons to be displayed besides the text.
        
        file_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
    
    @Slot()
    def update_stats(self):
        cursor = self.text_edit.textCursor()
        size = self.text_edit.document().characterCount()
        x = str(cursor.blockNumber() + 1)
        y = str(cursor.columnNumber() + 1)
        self.position_label.setText(f'Ln: {x}, Col: {y}')
        self.charcount_label.setText(f'Chars: {size}')
        
    @Slot()
    def show_selection_size(self):
        cursor = self.text_edit.textCursor()
        count = len(cursor.selectedText())
        msg = f'{count} characters selected'
        self.statusBar().showMessage(msg, 2000)
        
    def show_messagebox(self):
        messagebox = QMessageBox()
        messagebox.setText('QMainWindow Example\nVersion 1.1')
        messagebox.exec()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = QEditor()
    editor.show()
    sys.exit(app.exec())
