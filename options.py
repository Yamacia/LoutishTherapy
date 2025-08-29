from functions import *

def createOptionCard(screen, screen_width, screen_height, card_outline):
    """
    Generates the option card and statistics.

    Keyword arguments:
        screen: Surface 
            Surface resolution used for image representation      
        screen_width: float
            The width of the screen
        screen_height: float
            The height of the screen 
        card_outline: float
            The outline width of the created card
    """
    endgame_card_width = 2 * screen_width / 3
    endgame_card_height = 0.6 * screen_height
    endgame_card_x = screen_width / 2 - endgame_card_width / 2
    endgame_card_y = 0.69 * screen_height - endgame_card_height / 2

    pygame.draw.rect(screen, ENDSCREEN, [endgame_card_x, endgame_card_y, endgame_card_width, endgame_card_height], border_radius = 30)
    pygame.draw.rect(screen, OUTLINE, [endgame_card_x, endgame_card_y, endgame_card_width, endgame_card_height], 
                    card_outline, border_radius = 30)
    
def createOptionStatistics(screen, font, screen_width, screen_height):
    """
    Generates the option statistics (from all past sessions).

    Keyword arugments:
        screen: Surface 
            Surface resolution used for image representation      
        font: sysFont
            System Font loading all characteristics of the desired font for the message
        screen_width: float
            The width of the screen
        screen_height: float
            The height of the screen 
    """
    statistics = pd.read_csv("statistics.csv")
    total_count = statistics.loc[:, "Image Count"].sum()
    small_font = pygame.font.SysFont(MAIN_FONT, getSmallFontDimensions(screen=screen))

    # Position Texts
    screen_left, screen_top, screen_width, screen_height = screen.get_rect()
    endgame_card_width = 2 * screen_width / 3
    endgame_card_height = 0.6 * screen_height

    # Total Counter
    total_message_x = endgame_card_width / 2
    total_message_y =  screen_height - endgame_card_height + BUTTON_SPACING

    total_message = small_font.render("Total Image Generated :", True, OUTLINE)
    screen.blit(total_message, total_message.get_rect(center = (total_message_x, total_message_y)))

    total_count_message_x = endgame_card_width / 2
    total_count_message_y =  screen_height - endgame_card_height + 3 * BUTTON_SPACING

    total_count_message = font.render(f"{total_count}", True, OUTLINE)
    screen.blit(total_count_message, total_count_message.get_rect(center = (total_count_message_x, total_count_message_y)))

    # Favourite Image
    favourite_message_x = endgame_card_width / 2
    favourite_message_y =  screen_height - endgame_card_height * 0.75 + BUTTON_SPACING

    favourite_message = small_font.render("Favourite Image :", True, OUTLINE) 
    screen.blit(favourite_message, favourite_message.get_rect(center = (favourite_message_x, favourite_message_y)))

    favourite_image_x = endgame_card_width / 2
    favourite_image_y =  screen_height - endgame_card_height * 0.75 + IMAGE_SPACING

    favourite_image = selectFavouriteLoutishImage()
    endscreen_loutish_dimensions = favouriteImageDimension.dimensions
    favourite_image = pygame.transform.scale(favourite_image, endscreen_loutish_dimensions)
    screen.blit(favourite_image, favourite_image.get_rect(center = (favourite_image_x, favourite_image_y)))
    
    # Images per day
    images_daily_x =  endgame_card_width
    images_daily_y =  screen_height - endgame_card_height + BUTTON_SPACING

    images_daily = small_font.render("Images per day :", True, OUTLINE)
    screen.blit(images_daily, images_daily.get_rect(center = (images_daily_x, images_daily_y)))

def createOptionButtons(screen, button_width, button_height, button_spacing, button_outline, primary_color, font, mouse):
    """
    Generates the option screen buttons, that gets highlighted if hovered by the user's mouse cursor.

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
    # Position Buttons
    screen_left, screen_top, screen_width, screen_height = screen.get_rect()
    endgame_card_width = 2 * screen_width / 3

    buttons_x = endgame_card_width / 2
    buttons_y = screen_height - button_height - button_spacing

    # More Stats Button
    stats_button_x = buttons_x - button_width / 2
    stats_button_y = buttons_y
    stats_button_text_pos = buttons_x, buttons_y + 0.5 * button_height

    if checkMouseInButton(mouse = mouse, button_x = stats_button_x, button_width = button_width, 
                          button_y = stats_button_y, button_height = button_height):
        createButton(screen = screen, color_bg = WHITE, color_outline = primary_color, 
                     position_x = stats_button_x, position_y = stats_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "More Statistics", 
                     text_pos = stats_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = stats_button_x, position_y = stats_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "More Statistics", 
                     text_pos = stats_button_text_pos)    

    buttons_x = endgame_card_width
    buttons_y = screen_height - button_height - button_spacing

    # Back to Home Button
    home_button_x = buttons_x - button_width / 2
    home_button_y = buttons_y
    home_button_text_pos = buttons_x, buttons_y + 0.5 * button_height

    if checkMouseInButton(mouse = mouse, button_x = home_button_x, button_width = button_width, 
                          button_y = home_button_y, button_height = button_height):
        createButton(screen = screen, color_bg = WHITE, color_outline = primary_color, 
                     position_x = home_button_x, position_y = home_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "Back to Home", 
                     text_pos = home_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = home_button_x, position_y = home_button_y,
                     button_width = button_width, button_height = button_height,
                     button_outline = button_outline, font = font, text = "Back to Home", 
                     text_pos = home_button_text_pos)           
        
def checkOptionButtonClick(screen, button_width, button_height, button_spacing, mouse, current_screen_state):
    """
    Verifies if one of the option buttons has been clicked by the user.

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

    # Position Buttons
    screen_left, screen_top, screen_width, screen_height = screen.get_rect()
    endgame_card_width = 2 * screen_width / 3

    buttons_x = endgame_card_width / 2
    buttons_y = screen_height - button_height - button_spacing

    # More Stats Button
    # stats_button_x = buttons_x - button_width / 2
    # stats_button_y = buttons_y
    # stats_button_text_pos = buttons_x, buttons_y + 0.5 * button_height

    # if checkMouseInButton(mouse = mouse, button_x = stats_button_x, button_width = button_width, 
    #                       button_y = stats_button_y, button_height = button_height):
    # else:

    buttons_x = endgame_card_width
    buttons_y = screen_height - button_height - button_spacing

    # Back to Home Button
    home_button_x = buttons_x - button_width / 2
    home_button_y = buttons_y

    if checkMouseInButton(mouse = mouse, button_x = home_button_x, button_width = button_width, 
                          button_y = home_button_y, button_height = button_height):
        current_screen_state.set_value(ScreenValue.HOME.value)

    return current_screen_state

def createOption(screen, button_width, button_height, button_spacing, button_outline, font, mouse):
    """
    Generates the Option Screen.

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
    """
    # Get Title logo with corresponding dimensions
    image = pygame.image.load("Game_Images/title_screen.png")
    title_logo_dimensions = getOptionLoutishDimensions(screen = screen)
    image = pygame.transform.scale(image, title_logo_dimensions)

    # Center Title Logo
    centered_image_x, centered_image_y = image.get_rect(center=screen.get_rect().center).left, image.get_rect(center=screen.get_rect().center).top
    image_position = (centered_image_x, 0) 
    screen.blit(image, dest = image_position)

    screen_left, screen_top, screen_width, screen_height = screen.get_rect()

    createOptionCard(screen = screen, screen_width = screen_width, screen_height = screen_height, card_outline = button_outline)
    createOptionStatistics(screen = screen, font = font, screen_width = screen_width,
                              screen_height = screen_height)

    createOptionButtons(screen = screen, button_width = button_width, button_height = button_height, 
                    button_spacing = button_spacing, button_outline = button_outline, primary_color = LOUTISH_COLOR,
                    font = font, mouse = mouse)