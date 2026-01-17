import os
import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QFileDialog, QMessageBox)


class Editor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Notes')
        self.resize(500, 300)
        
        self.current_file_name = ''

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        # 1. Provide a means for the user to display the dialog.
        
        self.open_action = QAction(self)
        self.open_action.setText('Open')
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.setIcon(QIcon('./icons/open.png'))
        self.open_action.triggered.connect(self.open_note)
        
        self.save_action = QAction(self)
        self.save_action.setText('Save')
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setIcon(QIcon('./icons/save.png'))
        self.save_action.triggered.connect(self.save_note)

        self.exit_action = QAction(self)
        self.exit_action.setText('Exit')
        self.exit_action.setShortcut('Alt+X')
        self.exit_action.setIcon(QIcon('./icons/exit.png'))
        self.exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.exit_action)
        
        file_toolbar = self.addToolBar('File')
        file_toolbar.addAction(self.open_action)
        file_toolbar.addAction(self.save_action)
        file_toolbar.addAction(self.exit_action)
        
        file_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        
        self.update_window_title()
        
    def update_window_title(self):
        if self.current_file_name:
            print(self.current_file_name)
            title = os.path.basename(self.current_file_name)
            print(title)
        else:
            title = 'Untitled'
        self.setWindowTitle(f'{title} - Acme Notes')
    
    # 2. Display the dialog.
    
    @Slot()
    def save_note(self):
        note_contents = self.text_edit.document().toHtml()
        if self.current_file_name:
            try:
                with open(self.current_file_name, 'w') as f:
                    f.write(note_contents)
                self.text_edit.document().setModified(False)
            except Exception as e:
                QMessageBox.warning(self,
                    'Save Error', f'Failed to save file: {str(e)}')
        else:
            
            # 3. Inspect the return value and handle the user's response.
            
            ret_value = QFileDialog.getSaveFileName(
                self, 'Save Note', '.', 'Acme Files (*.acme)')
            if ret_value[0]:
                file_name = ret_value[0]
                if not file_name.endswith('.acme'):
                    file_name += '.acme'
                try:
                    with open(file_name, 'w') as f:
                        f.write(note_contents)
                    self.current_file_name = file_name
                    self.text_edit.document().setModified(False)
                    self.update_window_title()
                except Exception as e:
                    QMessageBox.warning(self,
                        'Save Error', f'Failed to save file: {str(e)}')
                
    @Slot()
    def open_note(self):
        ret_value = QFileDialog.getOpenFileName(
            self, 'Open Note', '.', 'Acme Files (*.acme)')
        if ret_value[0]:
            file_name = ret_value[0]
            try:
                with open(file_name, 'r') as f:
                    contents = f.read()
                self.text_edit.setHtml(contents)
                self.current_file_name = file_name
                self.text_edit.document().setModified(False)
                self.update_window_title()
            except Exception as e:
                QMessageBox.warning(self,
                    'Open Error', f'Failed to open file: {str(e)}')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())
