import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QWidget,
    QVBoxLayout, QFrame)
from PySide6.QtSql import (QSqlDatabase,
    QSqlRelationalTableModel, QSqlRelation)
from categoriestablemodel import CategoriesTableModel
from singlerecordform import SingleRecordForm
from transactionsform import TransactionsForm

class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        
        result = self.db.open()
        if result:
            print('Connected!')
        else:
            print('Failed to connect to the database')
        
        self.categories_model = CategoriesTableModel()
        self.categories_model.setTable('Categories')

        mappings = {
            0: 'Category Id',
            1: 'Category Name',
            2: 'Description'}
        
        master_form = SingleRecordForm(self.categories_model, mappings)
        layout.addWidget(master_form)
        
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(separator)
        
        self.transactions_model = QSqlRelationalTableModel()
        self.transactions_model.setTable('Transactions')
        self.transactions_model.setRelation(1,
            QSqlRelation('Accounts', 'account_id', 'account_name'))        
        master_form.mapper.currentIndexChanged.connect(self.filter_transactions)
        
        self.details_form = TransactionsForm(self.transactions_model)
        layout.addWidget(self.details_form)
        
        self.filter_transactions(master_form.mapper.currentIndex())
        
    @Slot(int)
    def filter_transactions(self, row):
        index = self.categories_model.index(row, 0)
        category_id = self.categories_model.data(index)
        self.transactions_model.setFilter(f'category_id = {category_id}')
        self.transactions_model.select()
        self.details_form.category_id = category_id
        row_count = self.transactions_model.rowCount()
        self.details_form.view.clearSelection()
        if row_count > 0:
            self.details_form.view.selectRow(0)
        self.details_form.update_record_label(
            self.details_form.view.currentIndex())


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
