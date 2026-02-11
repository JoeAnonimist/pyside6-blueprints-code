import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QFormLayout, QDataWidgetMapper,
    QLineEdit, QPushButton)
from PySide6.QtTest import QAbstractItemModelTester
from csvmodel import CsvModel


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = CsvModel('data.csv')
        QAbstractItemModelTester(self.model,
            QAbstractItemModelTester.FailureReportingMode.Warning)

        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.selectionModel().currentChanged.connect(
            self.on_current_changed)
        self.view.resizeColumnsToContents()
        
        # 2. Create the widgets.
        
        self.fname_edit = QLineEdit()
        self.lname_edit = QLineEdit()
        self.prof_edit = QLineEdit()
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_new_values)
        
        # 3. Add the widgets to the data widget mapper.
        
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.setSubmitPolicy(
            QDataWidgetMapper.SubmitPolicy.ManualSubmit)
        
        self.mapper.addMapping(self.fname_edit, 1)
        self.mapper.addMapping(self.lname_edit, 2)
        self.mapper.addMapping(self.prof_edit, 3)
        self.mapper.toFirst()
        
        form_layout = QFormLayout()
        form_layout.addWidget(self.fname_edit)
        form_layout.addWidget(self.lname_edit)
        form_layout.addWidget(self.prof_edit)
        form_layout.addWidget(self.submit_button)
        
        layout.addWidget(self.view)
        layout.addLayout(form_layout)
        
        self.model.dataChanged.connect(self.on_data_changed)
        
    def submit_new_values(self):
        self.mapper.submit()
        self.view.setFocus()
    
    # Sync the view and the mapper
    def on_current_changed(self, current, previous):
        self.mapper.setCurrentIndex(current.row())
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        print(f'Model changed, r: {topLeft.row()}, c: {topLeft.column()}')
        data = topLeft.model().data(topLeft, Qt.ItemDataRole.DisplayRole)
        print(f'Data: {data}')
           

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
