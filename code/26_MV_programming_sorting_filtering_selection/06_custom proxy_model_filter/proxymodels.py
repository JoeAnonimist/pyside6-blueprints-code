from PySide6.QtCore import QSortFilterProxyModel, Qt


# 1. Subclass QSortFilterProxyModel.

class OutlierProxyModel(QSortFilterProxyModel):
    
    def __init__(self, low, high, parent=None):
        super().__init__(parent)
        self.low = low
        self.high = high
    
    # 2. Reimplement filterAcceptsRow().
    
    def filterAcceptsRow(self, source_row, source_parent):
        
        model = self.sourceModel()
        
        value_index = model.index(source_row, 1, source_parent) 
        value = model.data(value_index, self.filterRole())
        aggregate_index = model.index(source_row, 2, source_parent)
        aggregate = model.data(aggregate_index, self.filterRole())
        
        if aggregate == 1 and (value < self.low or value > self.high):
            return True
        return False