# Screen Dimensions

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Side Image Scrolling Speed
SCROLLING_SPEED = SCREEN_HEIGHT // 150

# Button Dimensions

BUTTON_WIDTH = (SCREEN_WIDTH // 3) * 0.95
BUTTON_HEIGHT = ((SCREEN_HEIGHT / 2) // 3) * 0.80
BUTTON_SPACING = SCREEN_HEIGHT // 25

# Option Button Dimensions

OPTION_BUTTON_WIDTH = (SCREEN_WIDTH // 3) * 0.95
OPTION_BUTTON_HEIGHT = ((SCREEN_HEIGHT / 2) // 3) * 0.60

# Image Dimensions
IMAGE_SPACING = SCREEN_HEIGHT // 6

class Dimensions:
    def __init__(self, width, height):
        self.dimensions = (width, height)

ScreenDimensions = Dimensions(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT
)

TitleLogoDimension = Dimensions(
    width=SCREEN_WIDTH/2,
    height=SCREEN_HEIGHT/2
)

ButtonDimension = Dimensions(
    width=BUTTON_WIDTH,
    height=BUTTON_HEIGHT
)

OptionButtonDimension = Dimensions(
    width=OPTION_BUTTON_WIDTH,
    height=OPTION_BUTTON_HEIGHT
)

LoutishImageDimension = Dimensions(
    width=SCREEN_WIDTH * 0.7,
    height=SCREEN_HEIGHT  * 0.7
)

endScreenLoutishDimension = Dimensions(
    width=SCREEN_WIDTH * 0.4,
    height=SCREEN_HEIGHT * 0.4
)

optionLogoDimension = Dimensions(
    width=SCREEN_WIDTH * 0.4,
    height=SCREEN_HEIGHT * 0.4
)

favouriteImageDimension = Dimensions(
    width=SCREEN_WIDTH * 0.25,
    height=SCREEN_HEIGHT * 0.25
)