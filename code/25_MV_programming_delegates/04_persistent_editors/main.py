import sys
from PySide6.QtCore import QMetaType
from PySide6.QtWidgets import (QApplication, QTableView,
    QWidget, QVBoxLayout, QItemEditorFactory, QStyledItemDelegate)
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

        view = QTableView()
        view.setModel(model)
        view.resizeColumnsToContents()
        
        # 3. Set up the factory and the delegate.
        
        factory = QItemEditorFactory()
        factory.registerEditor(QMetaType.Type.Int, NumericLineEditCreator())
        delegate = QStyledItemDelegate()
        delegate.setItemEditorFactory(factory)
        view.setItemDelegateForColumn(1, delegate)
        
        # 4. Open a persistent editor for each cell in column 1.

        for row in range(model.rowCount()):
            index = model.index(row, 1)
            view.openPersistentEditor(index)

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
