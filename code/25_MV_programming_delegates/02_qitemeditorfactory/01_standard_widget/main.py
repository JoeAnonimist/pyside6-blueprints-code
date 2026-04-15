import sys
from PySide6.QtCore import QMetaType
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QItemEditorFactory,
    QStyledItemDelegate)
from PySide6.QtTest import QAbstractItemModelTester
from models import CsvModel
from editorcreators import NumericLineEditCreator


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()
        QAbstractItemModelTester(model,
            QAbstractItemModelTester.FailureReportingMode.Warning)
        
        # 2. Create a QItemEditorFactory object
        #    and register the custom editor with it.
        
        factory = QItemEditorFactory()
        factory.registerEditor(
            QMetaType.Type.Int, NumericLineEditCreator())
        
        # 3. Create a styled item delegate
        #    and and set factory as its editor factory.
        
        delegate = QStyledItemDelegate()
        delegate.setItemEditorFactory(factory)
        
        view = QTableView()
        view.setModel(model)
        
        # 4. Set delegate as the item delegate
        #    for the appropriate column.
        
        view.setItemDelegateForColumn(1, delegate)
        
        view.resizeColumnsToContents()
        layout.addWidget(view)
        model.dataChanged.connect(self.on_data_changed)
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        for row in topLeft.model().csv_data:
            print(row)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
