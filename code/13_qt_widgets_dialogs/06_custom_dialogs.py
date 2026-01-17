import sys
from PySide6.QtCore import Qt, QSettings
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication,
    QMainWindow, QLabel, QTextEdit, QDialog,
    QVBoxLayout, QHBoxLayout, QCheckBox, QSpinBox,
    QDialogButtonBox)


class SettingsDialog(QDialog):
    
    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Settings')
        self.setLayout(QVBoxLayout())
        self.layout().setSpacing(10)
        self.settings = settings
        self.autosave_checkbox = QCheckBox('Autosave Note')
        self.autosave_checkbox.setChecked(
            self.settings.value('autosave', True, type=bool))
        self.layout().addWidget(self.autosave_checkbox) 
        self.autosave_interval_spinbox = QSpinBox()
        self.autosave_interval_spinbox.setRange(1, 60)
        self.autosave_interval_spinbox.setSuffix(' min')
        self.autosave_interval_spinbox.setValue(
            self.settings.value('interval', 10, type=int))
        self.layout().addWidget(QLabel('Autosave Interval (minutes):'))
        self.layout().addWidget(self.autosave_interval_spinbox)
        self.remember_last_checkbox = QCheckBox('Remember Last Edited Note')
        self.remember_last_checkbox.setChecked(
            self.settings.value('remember_last', True, type=bool))
        self.layout().addWidget(self.remember_last_checkbox)
        
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.accepted.connect(self.save_settings)
        self.button_box.rejected.connect(self.reject)
        
        self.layout().addWidget(self.button_box)
        
    def save_settings(self):
        self.settings.setValue('autosave', self.autosave_checkbox.isChecked())
        self.settings.setValue('interval', self.autosave_interval_spinbox.value())
        self.settings.setValue('remember_last', self.remember_last_checkbox.isChecked())


class Editor(QMainWindow):
    
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('Acme Notes')
        self.resize(500, 300)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        self.settings = QSettings(
            './settings.ini', QSettings.Format.IniFormat)
        
        self.exit_action = QAction(self)
        self.exit_action.setText('Exit')
        self.exit_action.setShortcut('Alt+X')
        self.exit_action.setIcon(QIcon('./icons/exit.png'))
        self.exit_action.triggered.connect(self.close)
        
        self.settings_action = QAction(self)
        self.settings_action.setText('Settings')
        self.settings_action.setIcon(QIcon('./icons/settings.png'))
        self.settings_action.triggered.connect(self.show_settings)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(self.exit_action)
        file_menu.addAction(self.settings_action)
        
        file_toolbar = self.addToolBar('File')
        file_toolbar.addAction(self.exit_action)
        file_toolbar.addAction(self.settings_action)
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
