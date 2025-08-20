from functions import *

def createGameButtons(screen, button_width, button_height, button_spacing, button_outline, primary_color, font, mouse):
    """
    Generates the main game screen buttons, that gets highlighted if hovered by the user's mouse cursor.

    Keyword arguments:
        screen: Surface 
            Surface resolution used for image representation      
        button_width: float
            The width of the button
        button_height: float
            The height of the button    
        button_spacing: float
            The spacing surrounding a button    
        button_outline: float
            The outline width of the created button
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

    button_x = screen_width / 4
    button_y = screen_height - button_height - button_spacing

    # Left Button
    left_button_x = button_x - button_width / 2
    left_button_y = button_y
    left_button_text_pos = button_x, button_y + 0.5 * button_height

    if checkMouseInButton(mouse=mouse, button_x = left_button_x, button_width = button_width, 
                          button_y = left_button_y, button_height= button_height):
        
        createButton(screen = screen, color_bg = WHITE, color_outline = primary_color, 
                     position_x = left_button_x, position_y = left_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "I need another !", 
                     text_pos = left_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = left_button_x, position_y = left_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "I need another !", 
                     text_pos = left_button_text_pos)    
    
    # Right Button
    right_button_x = 3 * button_x - button_width / 2
    right_button_y = button_y
    right_button_text_pos = 3 * button_x, button_y + 0.5 * button_height

    if checkMouseInButton(mouse = mouse, button_x = right_button_x, button_width = button_width, 
                          button_y = right_button_y, button_height= button_height):
        
        createButton(screen = screen, color_bg = WHITE, color_outline = primary_color, 
                     position_x = right_button_x, position_y = right_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "I am good !", 
                     text_pos = right_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = right_button_x, position_y = right_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "I am good !", 
                     text_pos = right_button_text_pos)  
        
def checkGameButtonClick(screen, button_width, button_height, button_spacing, mouse, image_id, image_counter):
    """
    Verifies if one of the main game buttons has been clicked by the user.

    Keyword arguments: 
        screen: Surface 
            Surface resolution used for image representation      
        button_width: float
            The width of the button
        button_height: float
            The height of the button  
        button_spacing: float
            The spacing surrounding a button    
        mouse: tuple[int, int]
            The cursor position of the mouse
        image_id: int
            The ID of the selected Loutish image
        image_counter: int
            The number of Loutish images that have been generated so far
    """
    gameScreen, endScreen = True, False

    # Center Button
    screen_left, screen_top, screen_width, screen_height = screen.get_rect()

    button_x = screen_width / 4
    button_y = screen_height - button_height - button_spacing

    # Left Button
    left_button_x = button_x - button_width / 2
    left_button_y = button_y

    # Image Generation button

    if checkMouseInButton(mouse = mouse, button_x = left_button_x, button_width = button_width,
                          button_y = left_button_y, button_height = button_height):
        
        # Generates another image and updates the image counter
        for i in range(0,10):
            screen.fill(BACKGROUND_COLOR, (0, 0, screen_width, screen_height*0.75)) 

            number_images = len(next(os.walk("Loutish_Images"))[2]) - 1
            image_id = random.randint(0, number_images)
            image = selectLoutishImage(image_id)
            loutish_image_dimensions = getLoutishImageDimensions(screen = screen)
            image = pygame.transform.scale(image, loutish_image_dimensions)

            centered_image_x, centered_image_y = image.get_rect(center=screen.get_rect().center).left, image.get_rect(center=screen.get_rect().center).top
            image_position = (centered_image_x, 0) # Center Image
            screen.blit(image, dest = image_position)
            pygame.display.update()
            time.sleep(0.05)
        image_counter += 1
    
    # Right Button
    right_button_x = 3 * button_x - button_width / 2
    right_button_y = button_y

    # Exit button

    if checkMouseInButton(mouse = mouse, button_x = right_button_x, button_width = button_width, 
                          button_y = right_button_y, button_height = button_height):
        gameScreen = False
        endScreen = True

    return gameScreen, endScreen, image_id, image_counter

def createGame(screen, button_width, button_height, button_spacing, button_outline, font, mouse, image_id):
    """
    Generates the Home Screen.

    Keyword arguments:
        screen: Surface
            Surface resolution used for image representation      
        button_width: float
            The width of the button
        button_height: float
            The height of the button    
        button_spacing: float
            The spacing surrounding a button 
        button_outline: float
            The outline width of the created button   
        font: sysFont
            System Font loading all characteristics of the desired font for the message
        mouse: tuple[int, int]
            The cursor position of the mouse
        image_id: int
            The ID of the selected Loutish image
    """
    image = selectLoutishImage(image_id)
    loutish_image_dimensions = getLoutishImageDimensions(screen = screen)
    image = pygame.transform.scale(image, loutish_image_dimensions)

    centered_image_x, centered_image_y = image.get_rect(center=screen.get_rect().center).left, image.get_rect(center=screen.get_rect().center).top
    image_position = (centered_image_x, 0) # Center Image
    screen.blit(image, dest = image_position)
    createGameButtons(screen = screen, button_width = button_width, button_height = button_height, 
                    button_spacing = button_spacing, button_outline = button_outline, primary_color = LOUTISH_COLOR,
                    font = font, mouse = mouse)