import sys
from PySide6.QtWidgets import (QApplication, QWidget, QTableView,
    QListView, QVBoxLayout, QLabel, QAbstractItemView)
from csvmodel import CsvModel


class Window(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()

        # 1. Create the quick-pick view.

        quick_pick_view = QListView()
        quick_pick_view.setFlow(QListView.Flow.LeftToRight)
        quick_pick_view.setModel(model)
        quick_pick_view.setModelColumn(0)
        quick_pick_view.setFixedHeight(40)
        quick_pick_view.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)

        # 2. Create the detail view and share
        #    the first view's selection model.

        detail_view = QTableView()
        detail_view.setModel(model)
        detail_view.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows)
        detail_view.setSelectionModel(quick_pick_view.selectionModel())
        detail_view.resizeColumnsToContents()

        layout.addWidget(QLabel('Quick-pick View'))
        layout.addWidget(quick_pick_view)
        layout.addWidget(QLabel('Detail View'))
        layout.addWidget(detail_view)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
