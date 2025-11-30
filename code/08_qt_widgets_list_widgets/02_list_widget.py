# The QListWidget class provides
# an item-based list widget

import sys
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (QApplication,
    QWidget, QVBoxLayout, QListWidget, QLabel,
    QListWidgetItem)


class Window(QWidget):
    
    def __init__(self):

        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        weather_conditions = [
            ('☀️ Clear', 'Sunny skies with no cloud coverage'),
            ('⛅ Partly Cloudy', 'Sun and clouds throughout the day'),
            ('☁️ Cloudy', 'Overcast skies with full cloud coverage'),
            ('🌧️ Rain', 'Precipitation with steady rainfall'),
            ('⛈️ Thunderstorm', 'Heavy rain with lightning and thunder'),
            ('❄️ Snow', 'Frozen precipitation and cold temperatures')
        ]
        
        # 1. Create a list widget and add items to it.
        
        self.weather_list = QListWidget()
        
        for name, description in weather_conditions:
            item = QListWidgetItem(name)
            item.setData(Qt.ItemDataRole.UserRole, description)
            self.weather_list.addItem(item)

        self.selected_label = QLabel()
        self.description_label = QLabel()
        self.selected_label.setStyleSheet("font-size: 24px;")
        
        layout.addWidget(self.weather_list)
        layout.addWidget(self.selected_label)
        layout.addWidget(self.description_label)
        
        # 3. Connect the signal to the slot.

        self.weather_list.currentItemChanged.connect(
            self.select_weather)
        self.weather_list.setCurrentRow(0)
    
    # 3. Create the slot.
    
    @Slot(QListWidgetItem, QListWidgetItem)
    def select_weather(self, current, previous):

        weather = current.data(Qt.ItemDataRole.DisplayRole)
        description = current.data(Qt.ItemDataRole.UserRole)
        self.selected_label.setText(weather)
        self.description_label.setText(description)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
