from classes import *

def initializeGame():
    """
    Initialize the game screen and resolution with the default size.
    """
    pygame.init()
    pygame.display.set_caption("Loutish Therapy")
    screen = pygame.display.set_mode(ScreenDimensions.dimensions, pygame.RESIZABLE)  
    return screen

def initializeScreenState():
    """
    Initialize the screen state class and sets the home screen as the open one.
    """
    
    return ScreenState(value = ScreenValue.HOME.value)

def loadMusic():
    """
    Load the game's music.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(f"Music/{MAIN_MUSIC}")
    pygame.mixer.music.play()

def textHollow(font, message, fontcolor):
    """
    Renders the same message but as a hollow font, having only the outline of the text staying.

    Keyword arguments : 
        font: sysFont
            System Font loading all characteristics of the desired font for the message
        message: string
            The message that needs to be hollowed
        fontcolor: tuple[int, int, int]
            The color used for the hollow message, coded in RGB integers (0 to 255)
    """
    notcolor = [c^0xFF for c in fontcolor]
    base = font.render(message, 0, fontcolor, notcolor)
    size = base.get_width() + 2, base.get_height() + 2
    img = pygame.Surface(size, 16)
    img.fill(notcolor)
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (2, 0))
    img.blit(base, (0, 2))
    img.blit(base, (2, 2))
    base.set_colorkey(0)
    base.set_palette_at(1, notcolor)
    img.blit(base, (1, 1))
    img.set_colorkey(notcolor)
    return img

def textOutline(font, message, fontcolor, outlinecolor):
    """
    Renders the same message but ajusted with a colored outline.

    Keyword arguments : 
        font: sysFont
            System Font loading all characteristics of the desired font for the message
        message: string
            The message that needs to be outlined
        fontcolor: tuple[int, int, int]
            The color used for the original message, coded in RGB integers (0 to 255)
        outlinecolor: tuple[int, int, int]
            The color used for the outline of the message, coded in RGB integers (0 to 255)
    """
    base = font.render(message, 0, fontcolor)
    outline = textHollow(font, message, outlinecolor)
    img = pygame.Surface(outline.get_size(), 16)
    img.blit(base, (1, 1))
    img.blit(outline, (0, 0))
    img.set_colorkey(0)
    return img

def getFontDimensions(screen):
    """
    Gets the dimensions of the main font used for the game. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return FONT_SIZE
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get current screen ratios
    screen_width_ratio = screen_width / SCREEN_WIDTH
    screen_height_ratio = screen_height / SCREEN_HEIGHT

    font_size = int(FONT_SIZE * min(screen_width_ratio, screen_height_ratio))

    return font_size

def getTinyFontDimensions(screen):
    """
    Gets the dimensions of the tiny font used for the game. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return TINY_FONT_SIZE
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get current screen ratios
    screen_width_ratio = screen_width / SCREEN_WIDTH
    screen_height_ratio = screen_height / SCREEN_HEIGHT

    tiny_font_size = int(TINY_FONT_SIZE * min(screen_width_ratio, screen_height_ratio))

    return tiny_font_size

def getSmallFontDimensions(screen):
    """
    Gets the dimensions of the small font used for the game. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return SMALL_FONT_SIZE
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get current screen ratios
    screen_width_ratio = screen_width / SCREEN_WIDTH
    screen_height_ratio = screen_height / SCREEN_HEIGHT

    small_font_size = int(SMALL_FONT_SIZE * min(screen_width_ratio, screen_height_ratio))

    return small_font_size

def getBigFontDimensions(screen):
    """
    Gets the dimensions of the bigger font used for the game. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return BIG_FONT_SIZE
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get current screen ratios
    screen_width_ratio = screen_width / SCREEN_WIDTH
    screen_height_ratio = screen_height / SCREEN_HEIGHT

    big_font_size = int(BIG_FONT_SIZE * min(screen_width_ratio, screen_height_ratio))

    return big_font_size

def getLargeFontDimensions(screen):
    """
    Gets the dimensions of the larger font used for the game. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return LARGE_FONT_SIZE
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get current screen ratios
    screen_width_ratio = screen_width / SCREEN_WIDTH
    screen_height_ratio = screen_height / SCREEN_HEIGHT

    large_font_size = int(LARGE_FONT_SIZE * min(screen_width_ratio, screen_height_ratio))

    return large_font_size

def getButtonDimensions(screen):
    """
    Gets the dimensions of the primary button used for the game. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return BUTTON_WIDTH, BUTTON_HEIGHT

    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get button dimensions BASED on current screen dimensions
    button_width = (screen_width // 3) * 0.95
    button_height = (screen_height / 6) * 0.8 
    
    return button_width, button_height

def getButtonOutlineDimensions(screen):
    """
    Gets the dimensions of the outline font used for the game's buttons. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return BUTTON_OUTLINE
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get current screen ratios
    screen_width_ratio = screen_width / SCREEN_WIDTH
    screen_height_ratio = screen_height / SCREEN_HEIGHT

    outline_width = max(1, int(BUTTON_OUTLINE * min(screen_width_ratio, screen_height_ratio)))

    return outline_width


def getButtonSpacing(screen):
    """
    Gets the width of the spacing used for the game's buttons. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return BUTTON_SPACING

    # Get current screen height
    screen_height = screen.get_height()
    
    # Get button spacing size BASED on current screen dimensions
    button_spacing = screen_height // 25

    return button_spacing

def getLoutishLogoDimensions(screen):
    """
    Gets the dimensions of the Loutish Logo used for the game. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return TitleLogoDimension.dimensions
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get button dimensions BASED on current screen dimensions
    title_logo_width = screen_width / 2
    title_logo_height = screen_height / 2

    return title_logo_width, title_logo_height

def getLoutishImageDimensions(screen):
    """
    Gets the dimensions of the Loutish Images in the game. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return LoutishImageDimension.dimensions
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get button dimensions BASED on current screen dimensions
    loutish_image_width = screen_width * 0.7
    loutish_image_height = screen_height * 0.7

    return loutish_image_width, loutish_image_height

def getEndScreenLoutishDimensions(screen):
    """
    Gets the dimensions of the end screen picture. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return endScreenLoutishDimension.dimensions
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get button dimensions BASED on current screen dimensions
    endscreen_loutish_image_width = screen_width * 0.4
    endscreen_loutish_image_height = screen_height * 0.4

    return endscreen_loutish_image_width, endscreen_loutish_image_height

def getOptionLoutishDimensions(screen):
    """
    Gets the dimensions of the option's logo picture. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return optionLogoDimension.dimensions
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get button dimensions BASED on current screen dimensions
    option_loutish_image_width = screen_width * 0.4
    option_loutish_image_height = screen_height * 0.4

    return option_loutish_image_width, option_loutish_image_height

def getFavouriteLoutishDimensions(screen):
    """
    Gets the dimensions of the option's favourite Loutish picture. 
    
    Keyword arguments :
        screen: Surface
            Surface resolution used for image representation
    """ 
    # Check if default screen dimensions
    if screen.get_size() == (SCREEN_WIDTH, SCREEN_HEIGHT):
        return favouriteImageDimension.dimensions
    
    # Get current screen dimensions
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Get button dimensions BASED on current screen dimensions
    option_loutish_image_width = screen_width * 0.25
    option_loutish_image_height = screen_height * 0.25

    return option_loutish_image_width, option_loutish_image_height

def createButton(screen, position_x, position_y, button_width, button_height, button_outline, 
                  color_bg, color_outline, font, text, text_pos):
    """
    Generates a button that can be interacted with from the user's interface. 
    Also gives it a colored outline
    As well as changes color when hovered by the user's cursor

    Keyword arguments :
        screen: Surface 
            Surface resolution used for image representation
        position_x: float
            Starting position of the created button (on the x-axis)
        position_y: float
            Starting position of the created button (on the y-axis)
        button_width: float
            The length of the created button
        button_height: float
            The height of the created button
        button_outline: float
            The outline width of the created button
        color_bg: tuple[int, int, int]
            The color of the created button's body, coded in RGB integers (0 to 255)
        color_outline: tuple [int, int, int]
            The color of the created button's outline, coded in RGB (0 to 255)
        font: sysFont
            System Font loading all characteristics of the desired font for the message
        text: 
            The text superposed on the created button
        text_pos:
            The position of the text on the screen (tailored to be positionned in the center of the button)

    """
    pygame.draw.rect(screen, color_bg, [position_x, position_y, button_width, button_height])
    pygame.draw.rect(screen, color_outline, [position_x, position_y, button_width, button_height], button_outline)
    message = font.render(text, True, OUTLINE)
    screen.blit(message, message.get_rect(center=text_pos))

def checkMouseInButton(mouse, button_x, button_y, button_width, button_height):
    """
    Verifies if the user's mouse cursor is hovering on a button

    Keyword arguments: 
        mouse: tuple[int, int]
            The cursor position of the mouse
        button_x: float
            The starting positon of the button (on x-axis)
        button_y: float
            The starting positon of the button (on y-axis)
        button_width: float
            The width of the button
        button_height: float
            The height of the button        
    """
    return mouse[0] > button_x and mouse[0] < button_x + button_width and mouse[1] > button_y and mouse[1] < button_y + button_height

def selectLoutishImage(image_id):
    """
    Selects the corresponding Loutish image from the images folder (by it's ID)

    Keyword arguments:
        image_id : int
            The ID of the image that we want to select
    """
    images = next(os.walk("Loutish_Images"))[2]
    image = pygame.image.load(f"Loutish_Images/{images[image_id]}")
    return image

def selectFavouriteLoutishImage():
    """
    Selects the favourite Loutish image from the images folder 
    The favourite image is the one that the user that ended the game the most on
    """

    statistics = pd.read_csv("statistics.csv")
    favourite_image = statistics["Last Image"].value_counts().idxmax()

    image = pygame.image.load(f"Loutish_Images/{favourite_image}")
    return image

def createHomeFavouriteLoutishImage(screen, position):
    """
    Gets the favourite Loutish image from the images folder (by it's ID) and 
    positions it on the correct side of the home screen and positions it on the
    corresponding side of the screen

    Keyword arguments:
        image_id : int
            The ID of the image that we want to select
    """

    screen_width = screen.get_width()

    image = selectFavouriteLoutishImage()
    loutish_dimensions = getFavouriteLoutishDimensions(screen = screen)
    image = pygame.transform.scale(image, loutish_dimensions)

    # Positions the image on either side of the home screen
    if position == HomePosition.LEFT:
        favourite_image = SideImage(image = image, x = 0, y = - image.get_height(), type = SideImagePosition.FAVOURITE)
    if position == HomePosition.RIGHT:
        favourite_image = SideImage(image = image, x = screen_width - image.get_width(), y = - image.get_height(), type = SideImagePosition.FAVOURITE)

    return favourite_image

def selectLastLoutishImage():
    """
    Selects the favourite Loutish image from the images folder 
    The favourite image is the one that the user that ended the game the most on
    """

    statistics = pd.read_csv("statistics.csv")
    last_image = statistics["Last Image"].iloc[-1]

    image = pygame.image.load(f"Loutish_Images/{last_image}")
    return image

def selectHomeLastLoutishImage(screen, position):
    """
    Selects the favourite Loutish image from the images folder (by it's ID) and 
    positions it on the correct side of the home screen

    Keyword arguments:
        screen: Surface 
            Surface resolution used for image representation
        position: SideImagePosition(Enum)
            The position of the image on the screen
    """

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    image = selectLastLoutishImage()
    loutish_dimensions = getFavouriteLoutishDimensions(screen = screen)
    image = pygame.transform.scale(image, loutish_dimensions)

    # Positions the image on either side of the home screen
    if position == HomePosition.LEFT:
        favourite_image = SideImage(image = image, x = 0, y = screen_height / 2, type = SideImagePosition.LAST)
    if position == HomePosition.RIGHT:
        favourite_image = SideImage(image = image, x = screen_width - image.get_width(), y = screen_height / 2, type = SideImagePosition.LAST)

    return favourite_image

def getLoutishImageName(image_id):
    """
    Gets the name of the selected image (by its ID)

    Keyword arguments:
        image_id : int
            The ID of the image that we want to select
    """
    images = next(os.walk("Loutish_Images"))[2]
    return images[image_id]
