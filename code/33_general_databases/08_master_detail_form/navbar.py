from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar, QLabel


class NavBar(QToolBar):
    
    save = Signal()
    toFirst = Signal()
    toPrevious = Signal()
    toNext = Signal()
    toLast = Signal()
    new = Signal()
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
       
        self.save_action = QAction('💾')
        self.addSeparator()
        self.first_action = QAction('◀◀')
        self.prev_action = QAction('◀')
        self.record_label = QLabel()
        self.record_label.setFixedWidth(60)
        self.next_action = QAction('▶')
        self.last_action = QAction('▶▶')
        self.addSeparator()
        self.new_action = QAction('✚')
        
        self.save_action.triggered.connect(self.save.emit)
        self.first_action.triggered.connect(self.toFirst.emit)
        self.prev_action.triggered.connect(self.toPrevious.emit)
        self.next_action.triggered.connect(self.toNext.emit)
        self.last_action.triggered.connect(self.toLast.emit)
        self.new_action.triggered.connect(self.new.emit)

        self.addAction(self.save_action)
        self.addAction(self.first_action)
        self.addAction(self.prev_action)
        self.addWidget(self.record_label)
        self.addAction(self.next_action)
        self.addAction(self.last_action)
        self.addAction(self.new_action)
        self.setStyleSheet(
            ' QAction { font-size: 14px; color: black;}')
        
    @Slot(str)
    def update_record_label(self, text):
        self.record_label.setText(text)
