from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel,
    QPushButton, QComboBox, QCheckBox, QRadioButton, QSpinBox,
    QLineEdit, QTabBar, QTableWidget, QTableWidgetItem)


class WidgetFactory(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setLayout(QVBoxLayout())

        self.label = QLabel('Label')
        self.label.setObjectName('Label')
        
        self.push_button = QPushButton('Push button')
        self.push_button.setObjectName('Push button')
        
        self.combobox = QComboBox()
        self.combobox.addItems(['One', 'Two'])
        self.combobox.setObjectName('Combo box')
        
        self.checkbox = QCheckBox('Check box')
        self.checkbox.setObjectName('Checkbox')
        
        self.radiobutton = QRadioButton('Radio button')
        self.radiobutton.setObjectName('Radio button')
        
        self.spin_box = QSpinBox()
        self.spin_box.setObjectName('Spin box')
        
        self.line_edit = QLineEdit()
        self.line_edit.setObjectName('Line edit')
        
        self.tabbar = QTabBar()
        self.tabbar.setObjectName('Tab bar')
        self.tabbar.addTab('Tab 1')
        self.tabbar.addTab('Tab 2')
        
        self.table_widget = QTableWidget(1, 3)
        self.table_widget.setObjectName('Table view')
        self.table_widget.setItem(0, 0, QTableWidgetItem('One'))
        self.table_widget.setItem(0, 1, QTableWidgetItem('Two'))
        self.table_widget.setItem(0, 2, QTableWidgetItem('Three'))

        self.layout().addWidget(self.label)
        self.layout().addWidget(self.push_button)
        self.layout().addWidget(self.combobox)
        self.layout().addWidget(self.checkbox)
        self.layout().addWidget(self.radiobutton)
        self.layout().addWidget(self.line_edit)
        self.layout().addWidget(self.tabbar)
        self.layout().addWidget(self.table_widget)
        self.layout().addWidget(self.spin_box)
        