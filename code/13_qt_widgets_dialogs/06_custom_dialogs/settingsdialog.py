from PySide6.QtWidgets import (QDialog, QVBoxLayout,
    QCheckBox, QSpinBox, QLabel, QDialogButtonBox,
    QHBoxLayout)

# 1. Create a QDialog subclass.

class SettingsDialog(QDialog):
    
    def __init__(self, settings, parent=None):
        
        super().__init__(parent)
        self.setWindowTitle('Settings')
        self.setModal(True)
        
        # 2. Add the child widgets to the dialog.
        
        self.setLayout(QVBoxLayout())
        self.settings = settings
        
        self.autosave_checkbox = QCheckBox('Autosave Note')
        self.autosave_checkbox.setChecked(
            self.settings.value('autosave', True, type=bool))
        self.autosave_checkbox.toggled.connect(self.toggle_interval)

        self.autosave_interval_spinbox = QSpinBox()
        self.autosave_interval_spinbox.setRange(1, 60)
        self.autosave_interval_spinbox.setSuffix(' min')
        self.autosave_interval_spinbox.setValue(
            self.settings.value('interval', 10, type=int))
        self.autosave_interval_spinbox.setEnabled(
            self.autosave_checkbox.isChecked())
        
        self.remember_last_checkbox = QCheckBox(
            'Remember Last Edited Note')
        self.remember_last_checkbox.setChecked(
            self.settings.value(
                'remember_last', True, type=bool))
        
        # 3. Add QDialogButtonBox to the dialog.
        
        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        self.layout().addWidget(self.autosave_checkbox)
        inner_layout = QHBoxLayout()
        inner_layout.addWidget(QLabel('Autosave Interval:'))
        inner_layout.addWidget(self.autosave_interval_spinbox)
        self.layout().addLayout(inner_layout)
        self.layout().addWidget(self.remember_last_checkbox)
        self.layout().addWidget(self.button_box)
        
    def toggle_interval(self, checked):
        self.autosave_interval_spinbox.setEnabled(checked)
        
    def save_settings(self):
        
        self.settings.setValue('autosave',
            self.autosave_checkbox.isChecked())
        self.settings.setValue('interval',
            self.autosave_interval_spinbox.value())
        self.settings.setValue('remember_last',
            self.remember_last_checkbox.isChecked())
        
    def accept(self):
        self.save_settings()
        super().accept()
