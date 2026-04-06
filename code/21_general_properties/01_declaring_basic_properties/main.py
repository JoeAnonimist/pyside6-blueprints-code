import sys
from PySide6.QtWidgets import (QApplication,
    QWidget, QSpinBox, QVBoxLayout)
from customwidgets import StepsLabel

class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.steps_label = StepsLabel()
        layout.addWidget(self.steps_label)
        
        self.steps_label.steps = 5000
        
        self.goal_spinbox = QSpinBox()
        self.goal_spinbox.setMaximum(20000)
        self.goal_spinbox.setValue(self.steps_label.dailyGoal)
        self.goal_spinbox.valueChanged.connect(self.set_daily_goal)
        layout.addWidget(self.goal_spinbox)
        
    def set_daily_goal(self, goal):
        self.steps_label.dailyGoal = goal


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
