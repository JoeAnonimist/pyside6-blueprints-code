import sys
from PySide6.QtCore import QMetaType
from PySide6.QtWidgets import (QApplication, QWidget,
    QTableView, QVBoxLayout, QItemEditorFactory,
    QStyledItemDelegate)
from PySide6.QtTest import QAbstractItemModelTester
from models import CsvModel
from switchcreator import SwitchCreator


class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()
        QAbstractItemModelTester(model,
            QAbstractItemModelTester.FailureReportingMode.Warning)
        
        # 3. Create a factory and register the editor.
        #    Create a delegate, and assign the factory to it.
        #    Assign the delegate to the target columns.
        
        factory = QItemEditorFactory()
        factory.registerEditor(
            QMetaType.Type.Bool, SwitchCreator())
        
        delegate = QStyledItemDelegate()
        delegate.setItemEditorFactory(factory)
        
        view = QTableView()
        view.setModel(model)
        
        view.setItemDelegateForColumn(2, delegate)
        view.setItemDelegateForColumn(3, delegate)
        
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
