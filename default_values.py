from librairies import Enum

# Main Game Font
MAIN_FONT = 'Comic Sans'

# Default Font Size
TINY_FONT_SIZE = 25
SMALL_FONT_SIZE = 30
FONT_SIZE = 35
BIG_FONT_SIZE = 45
LARGE_FONT_SIZE = 60

# Main Music
MAIN_MUSIC = "shelter.mp3"

# Base Color
BACKGROUND_COLOR = (151, 206, 247) #97CEF7

# Button Outline Size
BUTTON_OUTLINE = 5

# All Mouse Actions
class MouseAction(Enum):
    LEFT_CLICK = 1
    SCROLL_WHEEL = 2
    RIGHT_CLICK = 3

# All Possible Screens
class ScreenValue(Enum):
    HOME = 1
    GAME = 2
    END = 3
    OPTION = 4

# Positions for Side Images on Home Screen
class HomePosition(Enum):
    LEFT = 1
    RIGHT = 2
    
# All Side Image Types
class SideImagePosition(Enum):
    FAVOURITE = 1
    LAST = 2