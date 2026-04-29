from PySide6.QtCore import (QItemSelectionModel,
    QItemSelection, QModelIndex, Qt)


# 1. Create a QItemSelectionModel subclass
#    and reimplement select().

class AggregateSelectionModel(QItemSelectionModel):

    def is_aggregate(self, row):
        index = self.model().index(row, 2)
        data = self.model().data(index, Qt.ItemDataRole.DisplayRole)
        return data  == 1
    
    def select(self, selection, command):

        if isinstance(selection, QModelIndex):
            if selection.isValid() and not self.is_aggregate(selection.row()):
                return
            super().select(selection, command)

        else:
            filtered = QItemSelection()
            for item_range in selection:
                top = item_range.top()
                bottom = item_range.bottom()
                for row in range(top, bottom + 1):
                    if self.is_aggregate(row):
                        index = self.model().index(row, 0)
                        filtered.select(index, index)
            super().select(filtered, command)