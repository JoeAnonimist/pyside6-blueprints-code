
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QWidget, QFormLayout,
    QLineEdit, QDataWidgetMapper, QMessageBox)
from categoriestablemodel import CategoriesTableModel
from navbar import NavBar

# 3. Create the detail form.

class SingleRecordForm(QWidget):
    
    def __init__(self, model, mappings, parent=None):

        super().__init__(parent)

        layout = QFormLayout()
        self.setLayout(layout)
        self.model = model
        
        self.widgets = {}
        for col, label in mappings.items():
            widget = QLineEdit()
            if col == 0:
                widget.setDisabled(True)
            layout.addRow(f'{label}: ', widget)
            self.widgets[col] = widget

        self.model.select()
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)
        for col, widget in self.widgets.items():
            self.mapper.addMapping(widget, col)
        self.mapper.toFirst()
        
        self.nav_bar = NavBar()
        self.nav_bar.save.connect(self.save_data)
        self.nav_bar.toFirst.connect(self.mapper.toFirst)
        self.nav_bar.toPrevious.connect(self.mapper.toPrevious)
        self.nav_bar.toNext.connect(self.mapper.toNext)
        self.nav_bar.toLast.connect(self.mapper.toLast)
        self.nav_bar.new.connect(self.add_new_record)
        layout.addWidget(self.nav_bar)
        
        self.update_record_label(self.mapper.currentIndex())
        self.mapper.currentIndexChanged.connect(self.update_record_label)
    
    # 4. Save and add records.
    
    @Slot()
    def save_data(self):
        current_row = self.mapper.currentIndex()
        if not self.mapper.submit():
            QMessageBox.critical(
                self, 'Error', self.model.lastError().text())
            return
        if not self.model.submitAll():
            QMessageBox.critical(
                self, 'Error', self.model.lastError().text())
            return
        self.model.select()
        self.mapper.setCurrentIndex(current_row)
    
    @Slot()
    def add_new_record(self):
        self.mapper.submit()
        row = self.model.rowCount()
        self.model.insertRow(row)
        self.mapper.toLast()
        
    @Slot()
    def update_record_label(self, index):
        total = self.model.rowCount()
        if total == 0:
            self.nav_bar.update_record_label('No Records')
        else:
            self.nav_bar.update_record_label(
                f'{index + 1} of {total}')
