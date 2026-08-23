import sys
from PySide6.QtWidgets import (QApplication,
    QWidget, QListView, QLineEdit, QPushButton,
    QHBoxLayout, QVBoxLayout, QDataWidgetMapper)
from PySide6.QtTest import QAbstractItemModelTester
from txtfilemodel import TxtFileModel


class Window(QWidget):
    
    def __init__(self, parent=None):

        super().__init__(parent)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.model = TxtFileModel('data.txt')
        QAbstractItemModelTester(self.model,
            QAbstractItemModelTester.FailureReportingMode.Warning)
        
        self.view = QListView()
        self.view.setModel(self.model)
        
        # 2. Create the widgets for displaying
        #    and editing the data
        
        self.lineedit = QLineEdit()
        self.lineedit.returnPressed.connect(self.submit_new_value)
        self.view.activated.connect(self.lineedit.setFocus)
        
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_new_value)
        
        # 3. Create the mapper object and set its model
        
        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)
        
        # 4. Add the mappings

        self.mapper.addMapping(self.lineedit, 0)
        
        self.mapper.setSubmitPolicy(
            QDataWidgetMapper.SubmitPolicy.ManualSubmit)
        self.mapper.toFirst()
        
        # 5. Synchronize the model with the mapper
        
        self.view.selectionModel().currentChanged.connect(
            self.mapper.setCurrentModelIndex)
        
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.lineedit)
        horizontal_layout.addWidget(self.submit_button)
        
        layout.addWidget(self.view)
        layout.addLayout(horizontal_layout)
        
    def submit_new_value(self):
        self.mapper.submit()
        self.view.setFocus()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
