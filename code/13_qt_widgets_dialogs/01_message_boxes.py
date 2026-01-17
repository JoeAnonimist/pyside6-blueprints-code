import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QMessageBox)


class Editor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Notes')
        self.resize(500, 300)

        self.text_edit = QTextEdit()        
        self.setCentralWidget(self.text_edit)

        exit_action = QAction(self)
        exit_action.setText('Exit')
        exit_action.setShortcut('Alt+X')
        exit_action.setIcon(QIcon('./icons/exit.png'))
        exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)
        file_toolbar = self.addToolBar('File')
        file_toolbar.addAction(exit_action)
        
        file_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
    
    def closeEvent(self, event):
        
        if self.text_edit.document().isModified():
            
            # 1. Create a messagebox object
            
            msgbox = QMessageBox()
            
            # 2. Set the object's properties
            
            msgbox.setWindowTitle('Unsaved Changes')
            msgbox.setIcon(QMessageBox.Icon.Question)
            msgbox.setText('Do you want to save changes?')
            msgbox.setInformativeText('The document has been modified.')
            msgbox.setStandardButtons(
                QMessageBox.StandardButton.Save |
                QMessageBox.StandardButton.Discard |
                QMessageBox.StandardButton.Cancel)
            msgbox.setDefaultButton(
                QMessageBox.StandardButton.Save)
            
            # 3. Display the messagebox and take actions
            #    based on its return value.
            
            ret_val = msgbox.exec()
            if ret_val == QMessageBox.StandardButton.Save:
                print('Saving the document')
                self.text_edit.document().setModified(False)
                event.accept()
            elif ret_val == QMessageBox.StandardButton.Discard:
                print('Changes discarded.')
                event.accept()
            else:
                print('Exit canceled')
                event.ignore()
        else:
            super().closeEvent(event)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())
