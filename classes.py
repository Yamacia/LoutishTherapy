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
        self.original_image = image
        
        self.x = x
        self.y = y

        self.type = type
        match type:
            case SideImagePosition.FAVOURITE:
                self.text = "Your Favourite Image :"
            case SideImagePosition.LAST:
                self.text = "Your Last Image :"
        self.text_size = TINY_FONT_SIZE
        self.text_font = MAIN_FONT

        self.scrolling_speed = SCROLLING_SPEED

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
        self.resizeFont(screen = screen)
        self.reposition_x(screen = screen, position = position)
        self.reposition_y(screen = screen)
        self.adaptScrolling(screen = screen)

    def resizeImage(self, screen):
        """
        Get the resized image

        Keyword arguments:
            screen: Surface
                Surface resolution used for image representation
        """
        if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
            self.image = pygame.transform.scale(self.original_image, favouriteImageDimension.dimensions)
        
        else:
            # Get current screen dimensions
            screen_width = screen.get_width()
            screen_height = screen.get_height()

            # Get button dimensions BASED on current screen dimensions
            image_width = screen_width * 0.25
            image_height = screen_height * 0.25
            self.image = pygame.transform.scale(self.original_image, (image_width, image_height))

    def resizeFont(self, screen):
        """
        Get the resized font

        Keyword arguments:
            screen: Surface
                Surface resolution used for image representation
        """
        if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
            self.text_size = TINY_FONT_SIZE

        else:
            # Get current screen dimensions
            screen_width = screen.get_width()
            screen_height = screen.get_height()

            # Get current screen ratios
            screen_width_ratio = screen_width / SCREEN_WIDTH
            screen_height_ratio = screen_height / SCREEN_HEIGHT

            self.text_size = int(TINY_FONT_SIZE * min(screen_width_ratio, screen_height_ratio))

    def reposition_x(self, screen, position):
        """
        Repositions the side image when resizing game screen
        on the x-axis

        Keyword arguments:
            screen: Surface
                Surface resolution used for image representation
            position: SideImagePosition(Enum)
                the position of the image on the screen
        """
        if position == HomePosition.RIGHT:
            self.x = screen.get_width() - self.image.get_width()

    def reposition_y(self, screen):
        """
        Repositions the side image when resizing game screen
        on the y-axis

        Keyword arguments:
            screen: Surface
                Surface resolution used for image representation
        """
        screen_height = screen.get_height()

        match self.type:
            case SideImagePosition.FAVOURITE:
                self.y = - self.image.get_height()
            case SideImagePosition.LAST:
                self.y = screen_height / 2
    
    def adaptScrolling(self, screen):
        """
        Adapts the image's scrolling speed to the resized game screen

        Keyword arguments:
            screen: Surface
                Surface resolution used for image representation
        """
        if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
            self.scrolling_speed = SCROLLING_SPEED

        else:
            # Get current screen height
            screen_height = screen.get_height()

            # Get current height ratios
            screen_height_ratio = screen_height / SCREEN_HEIGHT

            self.scrolling_speed = int(SCROLLING_SPEED * screen_height_ratio)
