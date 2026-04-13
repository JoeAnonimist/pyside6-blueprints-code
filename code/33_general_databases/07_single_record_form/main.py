import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtSql import QSqlDatabase
from singlerecordform import SingleRecordForm
from categoriestablemodel import CategoriesTableModel


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle('Edit Categories')
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('finance_demo.sqlite')
        
        result = self.db.open()
        if result:
            print('Connected!')
        else:
            print('Failed to connect to the database')
        
        table_model = CategoriesTableModel()
        table_model.setTable('Categories')

        mappings = {
            0: 'Category Id',
            1: 'Category Name',
            2: 'Description'}
        
        # 5. Add the form to the main window.
        
        detail_form = SingleRecordForm(table_model, mappings)
        layout.addWidget(detail_form)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
