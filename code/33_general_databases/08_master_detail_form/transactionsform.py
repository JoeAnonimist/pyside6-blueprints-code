from PySide6.QtCore import QModelIndex, QDate, Qt, Slot
from PySide6.QtWidgets import (QWidget, QVBoxLayout,
        QTableView, QDateEdit, QStyledItemDelegate)
from PySide6.QtSql import QSqlRelationalDelegate
from navbar import NavBar


class DateDelegate(QStyledItemDelegate):
    
    def createEditor(self, parent, option, index):
        editor = QDateEdit(parent)
        editor.setCalendarPopup(True)
        editor.setDisplayFormat("yyyy-MM-dd")
        return editor
    
    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.ItemDataRole.EditRole)
        if value:
            date = QDate.fromString(value, "yyyy-MM-dd")
            editor.setDate(date)
    
    def setModelData(self, editor, model, index):
        date = editor.date()
        model.setData(index, date.toString("yyyy-MM-dd"),
            Qt.ItemDataRole.EditRole)


class TransactionsForm(QWidget):
    
    def __init__(self, model, category_id=None, parent=None):

        super().__init__(parent)
        self.category_id = category_id
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.model = model
        
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.hideColumn(0)
        self.view.hideColumn(2)
        
        self.view.setSelectionBehavior(
            QTableView.SelectionBehavior.SelectRows)
        self.view.setSelectionMode(
            QTableView.SelectionMode.SingleSelection)
        if self.model.rowCount() > 0:
            self.view.selectRow(0)
        
        delegate = QSqlRelationalDelegate()
        self.view.setItemDelegate(delegate)
        date_delegate = DateDelegate()
        self.view.setItemDelegateForColumn(4, date_delegate)
        layout.addWidget(self.view)
        
        self.nav_bar = NavBar()
        self.nav_bar.toFirst.connect(self.to_first)
        self.nav_bar.toPrevious.connect(self.to_previous)
        self.nav_bar.toNext.connect(self.to_next)
        self.nav_bar.toLast.connect(self.to_last)
        self.nav_bar.new.connect(self.add_new_record)
        self.nav_bar.save.connect(self.save_changes)
        layout.addWidget(self.nav_bar)
        
        self.to_first()
        self.update_record_label(
            self.view.selectionModel().currentIndex())
        self.view.selectionModel().currentChanged.connect(
            self.update_record_label)
    
    @Slot()
    def to_first(self):
        if self.model.rowCount() > 0:
            self.view.selectRow(0)
            self.view.setFocus()
    
    @Slot()
    def to_previous(self):
        row = self.view.currentIndex().row() 
        if row > 0:
            self.view.selectRow(row - 1)
            self.view.setFocus()
            
    @Slot()
    def to_next(self):
        row = self.view.currentIndex().row()
        if row < self.model.rowCount() - 1:
            self.view.selectRow(row + 1)
            self.view.setFocus()
            
    @Slot()
    def to_last(self):
        if self.model.rowCount() > 0:
            self.view.selectRow(self.model.rowCount() - 1)
            self.view.setFocus()

    @Slot()
    def add_new_record(self):
        row = self.model.rowCount()
        if self.model.insertRow(row):
            category_index = self.model.index(row, 2)
            self.model.setData(category_index, self.category_id)
            self.view.selectRow(row)
            self.view.setFocus()
        
    @Slot()
    def save_changes(self):
        if self.model.submitAll():
            self.model.select()
        else:
            print(f'{self.model.lastError().text()}')

    @Slot(int)
    def update_record_label(self, current):
        total = self.model.rowCount()
        if total == 0:
            self.nav_bar.update_record_label('No Records')
        else:
            self.nav_bar.update_record_label(
                f'{current.row() + 1} of {total}')
