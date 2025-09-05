from functions import *

def createHomeButtons(screen, button_width, button_height, button_spacing, button_outline, primary_color, font, mouse):
    """
    Generates the home screen buttons, that gets highlighted if hovered by the user's mouse cursor.

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
                     button_outline = button_outline, font = font, text = "I need Therapy !", 
                     text_pos = first_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = first_button_x, position_y = first_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "I need Therapy !", 
                     text_pos = first_button_text_pos)       

    # Second Button
    second_button_x = button_x
    second_button_y = button_y + button_height + button_spacing
    second_button_text_pos = screen_width / 2, screen_height / 2 + 1.5 * button_height + button_spacing

    if checkMouseInButton(mouse = mouse, button_x = second_button_x, button_width = button_width, 
                          button_y = second_button_y, button_height= button_height):
        
        createButton(screen = screen, color_bg = WHITE, color_outline = primary_color, 
                     position_x = second_button_x, position_y = second_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "Settings", 
                     text_pos = second_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = second_button_x, position_y = second_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "Settings",
                     text_pos = second_button_text_pos)         
        
    # Third Button
    third_button_x = button_x
    third_button_y = button_y + 2 * (button_height + button_spacing)
    third_button_text_pos = screen_width / 2, screen_height / 2 + 2.5 * button_height + 2 * button_spacing
    
    if checkMouseInButton(mouse = mouse, button_x = third_button_x, button_width = button_width, 
                          button_y = third_button_y, button_height = button_height):
        
        createButton(screen = screen, color_bg = WHITE, color_outline = primary_color, 
                     position_x = third_button_x, position_y = third_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "Exit Application", 
                     text_pos = third_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = third_button_x, position_y = third_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "Exit Application",
                     text_pos = third_button_text_pos)      
        
def checkHomeButtonClick(screen, button_width, button_height, button_spacing, mouse, current_screen_state, image_id, image_counter):
    """
    Verifies if one of the home buttons has been clicked by the user.

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
        current_screen_state: int
            The current screen the user is on
    """

    # Center Button
    screen_left, screen_top, screen_width, screen_height = screen.get_rect()

    button_x = (screen_width - button_width) / 2
    button_y = screen_height / 2

    # First Button
    first_button_x = button_x
    first_button_y = button_y

    # Second Button
    second_button_x = button_x
    second_button_y = button_y + button_height + button_spacing

    # Third Button
    third_button_x = button_x
    third_button_y = button_y + 2 * (button_height + button_spacing)

    if checkMouseInButton(mouse = mouse, button_x = first_button_x, button_width = button_width, 
                          button_y = first_button_y, button_height = button_height):
        current_screen_state.set_value(ScreenValue.GAME.value)
        
        # Generating first Loutish image
        number_images = len(next(os.walk("Loutish_Images"))[2]) - 1
        image_id = random.randint(0, number_images)
        image_counter = 1     

    elif checkMouseInButton(mouse = mouse, button_x = second_button_x, button_width = button_width,
                            button_y = second_button_y, button_height = button_height):
        current_screen_state.set_value(ScreenValue.OPTION.value)     
    
    elif checkMouseInButton(mouse = mouse, button_x = third_button_x, button_width = button_width, 
                            button_y = third_button_y, button_height = button_height):
        pygame.quit()  
        sys.exit()
    return current_screen_state, image_id, image_counter

def createHome(screen, button_width, button_height, button_spacing, button_outline, font, mouse):
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
        image_counter: int
            The number of Loutish images that have been generated so far
    """
    # Get Title logo with corresponding dimensions
    image = pygame.image.load("Game_Images/title_screen.png")
    title_logo_dimensions = getLoutishLogoDimensions(screen = screen)
    image = pygame.transform.scale(image, title_logo_dimensions)

    # Center Title Logo
    centered_image_x, centered_image_y = image.get_rect(center=screen.get_rect().center).left, image.get_rect(center=screen.get_rect().center).top
    image_position = (centered_image_x, 0) 
    screen.blit(image, dest = image_position)

    createHomeButtons(screen = screen, button_width = button_width, button_height = button_height, 
                    button_spacing = button_spacing, button_outline = button_outline, primary_color = LOUTISH_COLOR,
                    font = font, mouse = mouse)
    
def createHomeSideImages(screen):
    """
    Generates the user's favourite and last Loutish images to be displayed on both sides of the screen

    Keyword arguments:
        screen: Surface
            Surface resolution used for image representation
    """
    # Favourite image
    favourite_image_left = createHomeFavouriteLoutishImage(screen = screen, position = HomePosition.LEFT)
    favourite_image_right = createHomeFavouriteLoutishImage(screen = screen, position = HomePosition.RIGHT)

    # Set up last session image 
    last_image_left = selectHomeLastLoutishImage(screen = screen, position = HomePosition.LEFT)
    last_image_right = selectHomeLastLoutishImage(screen = screen, position = HomePosition.RIGHT)

    return favourite_image_left, favourite_image_right, last_image_left, last_image_right
    
def positionHomeSideImages(screen, favourite_image_left, favourite_image_right, last_image_left, last_image_right):
    """
    Gets both the user's favourite and last Loutish images
    And positions them on both sides of the screen
    Also makes them scroll down the screen over time

    Keyword arguments:
        screen: Surface
            Surface resolution used for image representation
        favourite_image_left: SideImage
            The favourite image that will be displayed on the left side of the screen
        favourite_image_right: SideImage
            The favourite image that will be displayed on the right side of the screen  
        last_image_left: SideImage
            The user's last image that will be displayed on the left side of the screen  
        last_image_right: SideImage
            The user's last image that will be displayed on the right side of the screen        
    """
    # Favourite Image
    
    if favourite_image_left.get_y() < screen.get_height() + favourite_image_left.get_image().get_height():
        favourite_image_left.set_y(favourite_image_left.get_y() + 5)
    else:
        favourite_image_left.set_y(- favourite_image_left.get_image().get_height())

    if favourite_image_right.get_y() < screen.get_height() + favourite_image_right.get_image().get_height():
        favourite_image_right.set_y(favourite_image_right.get_y() + 5)
    else:
        favourite_image_right.set_y(- favourite_image_right.get_image().get_height())

    displayHomeSideImage(screen = screen, image = favourite_image_left)
    displayHomeSideImage(screen = screen, image = favourite_image_right)

    # Last Image

    if last_image_left.get_y() < screen.get_height() + last_image_left.get_image().get_height():
        last_image_left.set_y(last_image_left.get_y() + 5)
    else:
        last_image_left.set_y(- last_image_left.get_image().get_height())

    if last_image_right.get_y() < screen.get_height() + last_image_right.get_image().get_height():
        last_image_right.set_y(last_image_right.get_y() + 5)
    else:
        last_image_right.set_y(- last_image_right.get_image().get_height())

    displayHomeSideImage(screen = screen, image = last_image_left)
    displayHomeSideImage(screen = screen, image = last_image_right)

def displayHomeSideImage(screen, image):
    """
    Displays the image and its corresponding text on 
    its desired position

    Keyword arguments:
        screen: Surface
            Surface resolution used for image representation
        image: SideImage
            Image to display
    """
    image_x, image_y = image.get_x(), image.get_y()
    image_width = image.get_image().get_width() 
    image_height = image.get_image().get_height()

    screen.blit(image.image, (image_x, image_y))
    font = pygame.font.SysFont(image.text_font, image.text_size)
    message = font.render(image.get_text(), True, OUTLINE)
    message_position = message.get_rect(center = (image_width / 2, image_height / 2))
    screen.blit(message, (message_position.x + image_x, image_y - image.text_size))

def resizeHomeSideImages(screen, favourite_image_left, favourite_image_right, last_image_left, last_image_right):
    """
    When resizing the application's window, resizes the images to correctly fit the new surface

    Keyword arguments:
        screen: Surface 
            Surface resolution used for image representation
        favourite_image_left: SideImage
            The favourite image that will be displayed on the left side of the screen
        favourite_image_right: SideImage
            The favourite image that will be displayed on the right side of the screen  
        last_image_left: SideImage
            The user's last image that will be displayed on the left side of the screen  
        last_image_right: SideImage
            The user's last image that will be displayed on the right side of the screen 
    """
    favourite_image_left.resize(screen = screen, position = HomePosition.LEFT)
    favourite_image_right.resize(screen = screen, position = HomePosition.RIGHT)
    last_image_left.resize(screen = screen, position = HomePosition.LEFT)
    last_image_right.resize(screen = screen, position = HomePosition.RIGHT)
