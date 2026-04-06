from PySide6.QtCore import Property
from PySide6.QtWidgets import QLabel


# 1. Create a QObject subclass

class StepsLabel(QLabel):
    
    def __init__(self, daily_goal=8000, parent=None):
        
        super().__init__(parent)
        
        # 2. Declare the backing attributes 
        
        self._user_name = self.load_user_name()
        self._steps = 0
        self._daily_goal = daily_goal
        self.template_text = 'User: {}\nSteps: {}, Daily Goal: {}'
        
        self.update_text()

    def load_user_name(self):
        # Simulate retrieving the current logged-in user.
        return 'Jon'
    
    # 3. Declare the properties.
    
    @Property(str)
    def userName(self):
        return self._user_name
    
    def steps(self):
        return self._steps
    
    def setSteps(self, steps):
        if steps != self._steps:
            self._steps = steps
            self.update_text()

    steps = Property(int, fget=steps, fset=setSteps)
        
    @Property(int)
    def dailyGoal(self):
        return self._daily_goal
    
    @dailyGoal.setter
    def dailyGoal(self, daily_goal):
        if daily_goal != self._daily_goal:
            self._daily_goal = daily_goal
            self.update_text()
            
    def update_text(self):
        self.setText(
            f'User: <b>{self.userName}</b><br>'
            f'Steps: {self.steps}<br>'
            f'Goal: {self.dailyGoal}')
