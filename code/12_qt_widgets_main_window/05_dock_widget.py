# The QDockWidget class provides a widget that can be 
# docked inside a QMainWindow or floated 
# as a top-level window on the desktop

import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QIcon,QTextCharFormat, QFont
from PySide6.QtWidgets import (QApplication, QMainWindow,
    QTextEdit, QLabel, QMessageBox, QVBoxLayout, QPushButton,
    QSpinBox, QDockWidget, QWidget)


class Editor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Editor')
        self.resize(500, 300)

        self.text_edit = QTextEdit()
        self.text_edit.cursorPositionChanged.connect(
            self.update_dock_widgets)
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
        
        file_toolbar = self.addToolBar('File')
        file_toolbar.addAction(exit_action)
        file_toolbar.addAction(about_action)
        file_toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        
        # 1. Create the dock widget
            
        dock_widget = QDockWidget('Formatting')
        dock_widget.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea
            | Qt.DockWidgetArea.RightDockWidgetArea)
            
        vbox = QVBoxLayout()
        
        self.button_bold = QPushButton()
        self.button_bold.setIcon(QIcon('./icons/bold.png'))
        self.button_bold.setCheckable(True)
        self.button_bold.toggled.connect(self.update_bold)
        
        self.button_italic = QPushButton()
        self.button_italic.setIcon(QIcon('./icons/italic.png'))
        self.button_italic.setCheckable(True)
        self.button_italic.toggled.connect(self.update_italic)
        
        self.font_size_spinbox = QSpinBox()
        self.font_size_spinbox.setMinimumWidth(26)
        self.font_size_spinbox.setMinimum(1)
        self.font_size_spinbox.setMaximum(24)
        self.font_size_spinbox.valueChanged.connect(
            self.update_font_size)
        
        self.point_size = 12
        
        char_format = QTextCharFormat()
        char_format.setFontPointSize(self.point_size)
        self.text_edit.mergeCurrentCharFormat(char_format)
        self.font_size_spinbox.setValue(self.point_size)
        
        vbox.addWidget(self.button_bold)
        vbox.addWidget(self.button_italic)
        vbox.addWidget(self.font_size_spinbox)
        vbox.addStretch()
        
        container = QWidget()
        container.setLayout(vbox)
        container.setMinimumWidth(20)
        dock_widget.setWidget(container)
        
        # 2. Add the dock widget to the main window
        
        self.addDockWidget(
            Qt.DockWidgetArea.LeftDockWidgetArea, dock_widget)
    
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
    
    @Slot()
    def show_messagebox(self):
        messagebox = QMessageBox()
        messagebox.setText('QMainWindow Example\nVersion 1.2')
        messagebox.exec()
    
    # 3. Handle the dock widget children signals
    
    def update_bold(self, checked):
        char_format = QTextCharFormat()
        if checked:
            char_format.setFontWeight(QFont.Weight.Bold)
        else:
            char_format.setFontWeight(QFont.Weight.Normal)
        self.text_edit.mergeCurrentCharFormat(char_format)
        self.text_edit.setFocus(Qt.FocusReason.OtherFocusReason)
        
    def update_italic(self, checked):
        char_format = QTextCharFormat()
        char_format.setFontItalic(checked)
        self.text_edit.mergeCurrentCharFormat(char_format)
        self.text_edit.setFocus(Qt.FocusReason.OtherFocusReason)
        
    def update_font_size(self, i):
        char_format = QTextCharFormat()
        char_format.setFontPointSize(i)
        self.text_edit.mergeCurrentCharFormat(char_format)
        
    def update_dock_widgets(self):
        char_format = self.text_edit.textCursor().charFormat() 
        self.button_bold.setChecked(char_format.font().bold())
        self.button_italic.setChecked(char_format.font().italic())
        self.font_size_spinbox.setValue(char_format.font().pointSize())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    editor = Editor()
    editor.show()
    sys.exit(app.exec())
