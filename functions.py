from librairies import *

def initializeGame():
    """
    Initialize the game screen and resolution with the default size.
    """
    pygame.init()
    pygame.display.set_caption("Loutish Therapy")
    # screen = pygame.display.set_mode(ScreenDimensions.dimensions, pygame.RESIZABLE)  
    screen = pygame.display.set_mode(ScreenDimensions.dimensions)
    return screen

def initializeScreenState():
    """
    Initialize the status of each screen, and set home screen as the open one.
    """
    homeScreen = True
    gameScreen, optionScreen, endScreen = False, False, False
    return homeScreen, gameScreen, optionScreen, endScreen

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

def createButton(screen, position_x, position_y, button_width, button_height,
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
    pygame.draw.rect(screen, color_outline, [position_x, position_y, button_width, button_height], 5)
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