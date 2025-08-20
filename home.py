from functions import *

def createHomeButtons(screen, button_width, button_height, primary_color, font, mouse):
    """
    Generates the home screen buttons, that gets highlighted if hovered by the user's mouse cursor.

    Keyword arguments:
        screen: Surface 
            Surface resolution used for image representation      
        button_width: float
            The width of the button
        button_height: float
            The height of the button    
        primary_color: tuple[int, int, int]
            The primary color used to create the buttons (body when not hovered, outline when hovered) 
            coded in RGB integers (0 to 255)
        font: sysFont
            System Font loading all characteristics of the desired font for the message
        mouse: tuple[int, int]
            The cursor position of the mouse
        """
    # Center Button
    screen_left, screen_top, screen_width, screen_height = screen.get_rect()

    button_x = (screen_width - button_width) / 2
    button_y = screen_height / 2

    # First Button
    first_button_x = button_x
    first_button_y = button_y
    first_button_text_pos = screen_width / 2, screen_height / 2 + 0.5 * button_height

    if checkMouseInButton(mouse = mouse, button_x = button_x, button_width = button_width,
                           button_y = button_y, button_height = button_height):
        
        createButton(screen = screen, color_bg = WHITE, color_outline = primary_color, 
                     position_x = first_button_x, position_y = first_button_y,
                     button_width = button_width, button_height = button_height,
                     font = font, text = "I need Therapy !", 
                     text_pos = first_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = first_button_x, position_y = first_button_y,
                     button_width = button_width, button_height = button_height,
                     font = font, text = "I need Therapy !", 
                     text_pos = first_button_text_pos)       

    # Second Button
    second_button_x = button_x
    second_button_y = button_y + button_height + BUTTON_SPACING
    second_button_text_pos = screen_width / 2, screen_height / 2 + 1.5 * button_height + BUTTON_SPACING

    if checkMouseInButton(mouse = mouse, button_x = second_button_x, button_width = button_width, 
                          button_y = second_button_y, button_height= button_height):
        
        createButton(screen = screen, color_bg = WHITE, color_outline = primary_color, 
                     position_x = second_button_x, position_y = second_button_y,
                     button_width = button_width, button_height = button_height,
                     font = font, text = "Settings", 
                     text_pos = second_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = second_button_x, position_y = second_button_y,
                     button_width = button_width, button_height = button_height,
                     font = font, text = "Settings",
                     text_pos = second_button_text_pos)         
        
    # Third Button
    third_button_x = button_x
    third_button_y = button_y + 2 * (button_height + BUTTON_SPACING)
    third_button_text_pos = screen_width / 2, screen_height / 2 + 2.5 * button_height + 2 * BUTTON_SPACING
    
    if checkMouseInButton(mouse = mouse, button_x = third_button_x, button_width = button_width, 
                          button_y = third_button_y, button_height = button_height):
        
        createButton(screen = screen, color_bg = WHITE, color_outline = primary_color, 
                     position_x = third_button_x, position_y = third_button_y,
                     button_width = button_width, button_height = button_height,
                     font = font, text = "Exit Application", 
                     text_pos = third_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = third_button_x, position_y = third_button_y,
                     button_width = button_width, button_height = button_height,
                     font = font, text = "Exit Application",
                     text_pos = third_button_text_pos)      
        
def checkHomeButtonClick(screen, button_width, button_height, mouse):
    """
    Verifies if one of the home buttons has been clicked by the user.

    Keyword arguments: 
        screen: Surface 
            Surface resolution used for image representation      
        button_width: float
            The width of the button
        button_height: float
            The height of the button  
        mouse: tuple[int, int]
            The cursor position of the mouse
    """
    homeScreen, gameScreen, optionScreen = False, False, False

    # Center Button
    screen_left, screen_top, screen_width, screen_height = screen.get_rect()

    button_x = (screen_width - button_width) / 2
    button_y = screen_height / 2

    # First Button
    first_button_x = button_x
    first_button_y = button_y

    # Second Button
    second_button_x = button_x
    second_button_y = button_y + button_height + BUTTON_SPACING

    # Third Button
    third_button_x = button_x
    third_button_y = button_y + 2 * (button_height + BUTTON_SPACING)

    if checkMouseInButton(mouse = mouse, button_x = first_button_x, button_width = button_width, 
                          button_y = first_button_y, button_height = button_height):
        gameScreen = True     

    elif checkMouseInButton(mouse = mouse, button_x = second_button_x, button_width = button_width,
                            button_y = second_button_y, button_height = button_height):
        optionScreen = True
    
    elif checkMouseInButton(mouse = mouse, button_x = third_button_x, button_width = button_width, 
                            button_y = third_button_y, button_height = button_height):
        pygame.quit()  
        sys.exit()
    else:
        homeScreen = True
    return homeScreen, gameScreen, optionScreen 

def createHome(screen, button_width, button_height, font, mouse):
    """
    Generates the Home Screen.

    Keyword arguments:
        screen: Surface
            Surface resolution used for image representation      
        button_width: float
            The width of the button
        button_height: float
            The height of the button    
        font: sysFont
            System Font loading all characteristics of the desired font for the message
        mouse: tuple[int, int]
            The cursor position of the mouse
    """
    image = pygame.image.load("Game_Images/title_screen.png")
    image = pygame.transform.scale(image, TitleLogoDimension.dimensions)

    centered_image_x, centered_image_y = image.get_rect(center=screen.get_rect().center).left, image.get_rect(center=screen.get_rect().center).top
    image_position = (centered_image_x, 0) # Center Title Logo
    screen.blit(image, dest = image_position)
    createHomeButtons(screen = screen, button_width = button_width,
                    button_height = button_height, primary_color = LOUTISH_COLOR,
                    font = font, mouse = mouse)