from librairies import *
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

class SideImage:
    """
    Class that defines the image displayed on the sides of the home screen,
    as well as its position
    Also combined with a text defining the corresponding image
    """

    def __init__(self, image, x, y, type):
        self.image = image
        self.x = x
        self.y = y

        match type:
            case SideImagePosition.FAVOURITE:
                self.text = "Your Favourite Image :"
            case SideImagePosition.LAST:
                self.text = "Your Last Image :"
        self.text_size = TINY_FONT_SIZE
        self.text_font = MAIN_FONT

    def get_image(self):
        return self.image
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_text(self):
        return self.text

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def resize(self, screen, position):
        """
        Resizes the side image when resizing game screen
        """
        self.resizeImage(screen = screen)
        self.reposition_x(screen = screen, position = position)

    def resizeImage(self, screen):
        """
        Get the resized image
        """
        if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
            self.image = pygame.transform.scale(self.image, favouriteImageDimension.dimensions)
        
        else:
            # Get current screen dimensions
            screen_width = screen.get_width()
            screen_height = screen.get_height()

            # Get button dimensions BASED on current screen dimensions
            image_width = screen_width * 0.25
            image_height = screen_height * 0.25
            self.image = pygame.transform.scale(self.image, (image_width, image_height))

    def reposition_x(self, screen, position):
        """
        Repositions the side image when resizing game screen
        """
        if position == HomePosition.RIGHT:
            self.x = screen.get_width() - self.image.get_width()