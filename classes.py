from default_values import *

class ScreenState:
    """
    Class to fix the value of the screen state
    This state value is used to know on which screen the user is currently on
    """
    
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value