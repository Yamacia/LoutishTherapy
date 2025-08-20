from functions import *

def createEndScreenCard(screen, screen_width, screen_height):
    """
    Generates the end game card and statistics.

    Keyword arguments:
        screen: Surface 
            Surface resolution used for image representation      
        screen_width: float
            The width of the screen
        screen_height: float
            The height of the screen 
    """
    endgame_card_width = 2 * screen_width / 3
    endgame_card_height = 0.6 * screen_height
    endgame_card_x = screen_width / 2 - endgame_card_width / 2
    endgame_card_y = 0.69 * screen_height - endgame_card_height / 2

    pygame.draw.rect(screen, ENDSCREEN, [endgame_card_x, endgame_card_y, endgame_card_width, endgame_card_height], border_radius = 30)
    pygame.draw.rect(screen, OUTLINE, [endgame_card_x, endgame_card_y, endgame_card_width, endgame_card_height], width=5, border_radius = 30)

def createEndScreenConclusion(screen, font, screen_width, screen_height, image_counter):
    """
    Generates the end screen conclusion (based on session's statistics).

    Keyword arugments:
        screen: Surface 
            Surface resolution used for image representation      
        font: sysFont
            System Font loading all characteristics of the desired font for the message
        screen_width: float
            The width of the screen
        screen_height: float
            The height of the screen 
        image_counter: int
            The number of Loutish images that have been generated so far
    """
    statistics = pd.read_csv("statistics.csv")
    average_count = statistics.loc[:, "Image Count"].mean()
    count_ratio = (image_counter / average_count)*100

    if count_ratio < 100:
        conclusion_message_stat = textOutline(font, f"That's {round(100 - count_ratio, 2)}% less than usual !", GREEN, OUTLINE)
        conclusion_message_quote = textOutline(font, "Keep up the good work !", GREEN, OUTLINE)

    elif count_ratio > 100:
        conclusion_message_stat = textOutline(font, f"That's {round(count_ratio - 100, 2)}% more than usual !", RED, OUTLINE)
        conclusion_message_quote = textOutline(font, "Don't give up ! You got this !", RED, OUTLINE)

    else:
        conclusion_message_stat = textOutline(font, f"You are exactly on average !", OUTLINE, OUTLINE)
        conclusion_message_quote = textOutline(font, "That's impressive, good job !", OUTLINE, OUTLINE)

    screen.blit(conclusion_message_stat, conclusion_message_stat.get_rect(center = (screen_width / 2, screen_height * 0.62)))
    screen.blit(conclusion_message_quote, conclusion_message_quote.get_rect(center = (screen_width / 2, screen_height * 0.67)))

def createEndScreen(screen, button_width, button_height, primary_color, font, mouse, image_counter):
    """
    Generates the end screen buttons, that gets highlighted if hovered by the user's mouse cursor
    as well as the end screen card and conclusions.

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
        image_counter: int
            The number of Loutish images that have been generated so far
    """
    screen_left, screen_top, screen_width, screen_height = screen.get_rect()

    createEndScreenCard(screen = screen, screen_width = screen_width, screen_height = screen_height)

    big_font = pygame.font.SysFont('Comic Sans',60)
    title_message = big_font.render("You are cured !", True, OUTLINE)
    screen.blit(title_message, title_message.get_rect(center = (screen_width / 2, screen_height * 0.43)))

    counter_message = font.render(f"It only took you {image_counter} image{"s" if image_counter > 1 else ""} !", True, OUTLINE)
    screen.blit(counter_message, counter_message.get_rect(center = (screen_width / 2, screen_height * 0.5)))

    # Generates the final conclusion
    createEndScreenConclusion(screen = screen, font = font, screen_width = screen_width,
                              screen_height = screen_height, image_counter = image_counter)

    buttons_x = screen_width / 2
    buttons_y = screen_height - button_height - BUTTON_SPACING

    # End Button
    end_button_x = buttons_x - button_width / 2
    end_button_y = buttons_y
    end_button_text_pos = buttons_x, buttons_y + 0.5 * button_height

    if checkMouseInButton(mouse = mouse, button_x = end_button_x, button_width = button_width, 
                          button_y = end_button_y, button_height = button_height):
        createButton(screen = screen, color_bg = WHITE, color_outline = primary_color, 
                     position_x = end_button_x, position_y = end_button_y,
                     button_width = button_width, button_height = button_height,
                     font = font, text = "Back to Home", 
                     text_pos = end_button_text_pos)
    else:
        createButton(screen = screen, color_bg = primary_color, color_outline = OUTLINE, 
                     position_x = end_button_x, position_y = end_button_y,
                     button_width = button_width, button_height = button_height,
                     font = font, text = "Back to Home", 
                     text_pos = end_button_text_pos)        

def checkEndButtonClick(screen, button_width, button_height, mouse, image_counter):
    """
    Verifies if one of the end game buttons has been clicked by the user.
    Saves the image counter in a statistic CSV if user exits the game.

    Keyword arguments: 
        screen: Surface 
            Surface resolution used for image representation      
        button_width: float
            The width of the button
        button_height: float
            The height of the button  
        mouse: tuple[int, int]
            The cursor position of the mouse
        image_counter: int
            The number of Loutish images that have been generated so far
    """
    homeScreen = False
    EndScreen = True

    screen_left, screen_top, screen_width, screen_height = screen.get_rect()
    button_x = screen_width / 2
    button_y = screen_height - button_height - BUTTON_SPACING

    # End Button
    end_button_x = button_x - button_width / 2
    end_button_y = button_y

    # Clicked End button
    if checkMouseInButton(mouse = mouse, button_x = end_button_x, button_width = button_width, 
                          button_y = end_button_y, button_height = button_height):

        # Saving Statistics
        statistics = pd.read_csv("statistics.csv")
        statistics.loc[len(statistics)] = [datetime.datetime.now(), image_counter]
        statistics.to_csv("statistics.csv", index=False)

        homeScreen = True,
        EndScreen = False

    return homeScreen, EndScreen