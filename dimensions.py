# Screen Dimensions

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Button Dimensions

BUTTON_WIDTH = (SCREEN_WIDTH // 3) * 0.95
BUTTON_HEIGHT = ((SCREEN_HEIGHT / 2) // 3) * 0.80
BUTTON_SPACING = SCREEN_HEIGHT // 25

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

LoutishImageDimension = Dimensions(
    width=SCREEN_WIDTH * 0.7,
    height=SCREEN_HEIGHT  * 0.7
)

endScreenDimension = Dimensions(
    width=SCREEN_WIDTH * 0.4,
    height=SCREEN_HEIGHT * 0.4
)