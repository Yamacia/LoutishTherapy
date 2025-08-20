import pygame
import sys
import os
import random
import time
import pandas as pd
import datetime

from dimensions import *
from colors import *

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

def checkMouseInButton(mouse, button_x, y, button_width, button_height):
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
    return mouse[0] > button_x and mouse[0] < button_x + button_width and mouse[1] > y and mouse[1] < y + button_height


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

    button_x = (screen_width - button_width)/2
    button_y = screen_height/2

    # First Button
    first_button_x = button_x
    first_button_y = button_y
    first_button_text_pos = screen_width/2, screen_height/2 + 0.5*button_height

    if checkMouseInButton(mouse=mouse, x = button_x, width= button_width,y = button_y, height= button_height):
        createButton(screen=screen, color_bg = WHITE, color_outline=primary_color, 
                     position_x=first_button_x, position_y= first_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="I need Therapy !", 
                     text_pos = first_button_text_pos)
    else:
        createButton(screen=screen, color_bg = primary_color, color_outline= OUTLINE, 
                     position_x=first_button_x, position_y= first_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="I need Therapy !", 
                     text_pos = first_button_text_pos)       

    # Second Button
    second_button_x = button_x
    second_button_y = button_y + button_height + BUTTON_SPACING
    second_button_text_pos = screen_width/2, screen_height/2 + 1.5*button_height + 1*BUTTON_SPACING

    if checkMouseInButton(mouse=mouse, x = second_button_x, width= button_width, y = second_button_y, height= button_height):
        createButton(screen=screen, color_bg = WHITE, color_outline=primary_color, 
                     position_x=second_button_x, position_y= second_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Settings", 
                     text_pos = second_button_text_pos)
    else:
        createButton(screen=screen, color_bg = primary_color, color_outline= OUTLINE, 
                     position_x=second_button_x, position_y= second_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Settings",
                     text_pos= second_button_text_pos)         
        
    # Third Button
    third_button_x = button_x
    third_button_y = button_y + 2*(button_height + BUTTON_SPACING)
    third_button_text_pos = screen_width/2, screen_height/2 + 2.5*button_height + 2*BUTTON_SPACING
    
    if checkMouseInButton(mouse=mouse, x = third_button_x, width= button_width, y = third_button_y, height= button_height):
        createButton(screen=screen, color_bg = WHITE, color_outline=primary_color, 
                     position_x=third_button_x, position_y= third_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Exit Application", 
                     text_pos = third_button_text_pos)
    else:
        createButton(screen=screen, color_bg = primary_color, color_outline= OUTLINE, 
                     position_x=third_button_x, position_y= third_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Exit Application",
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

    button_x = (screen_width - button_width)/2
    button_y = screen_height/2

    # First Button
    first_button_x = button_x
    first_button_y = button_y

    # Second Button
    second_button_x = button_x
    second_button_y = button_y + button_height + BUTTON_SPACING

    # Third Button
    third_button_x = button_x
    third_button_y = button_y + 2*(button_height + BUTTON_SPACING)

    if checkMouseInButton(mouse=mouse, x = first_button_x, width= button_width,y = first_button_y, height= button_height):
        gameScreen = True     

    elif checkMouseInButton(mouse=mouse, x = second_button_x, width= button_width, y = second_button_y, height= button_height):
        optionScreen = True
    
    elif checkMouseInButton(mouse=mouse, x = third_button_x, width= button_width, y = third_button_y, height= button_height):
        pygame.quit()  
        sys.exit()
    else:
        homeScreen = True
    return homeScreen, gameScreen, optionScreen       

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

def createGameButtons(screen, button_width, button_height, color, font, mouse):
    """
    Generates the main game screen buttons, that gets highlighted if hovered by the user's mouse cursor.

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

    button_x = screen_width/4
    button_y = screen_height - button_height - BUTTON_SPACING

    # Left Button
    left_button_x = button_x - button_width/2
    left_button_y = button_y
    left_button_text_pos = button_x, button_y + 0.5*button_height

    if checkMouseInButton(mouse=mouse, x = left_button_x, width= button_width,y = left_button_y, height= button_height):
        createButton(screen=screen, color_bg = WHITE, color_outline=color, 
                     position_x=left_button_x, position_y= left_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="I need another !", 
                     text_pos = left_button_text_pos)
    else:
        createButton(screen=screen, color_bg = color, color_outline= OUTLINE, 
                     position_x=left_button_x, position_y= left_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="I need another !", 
                     text_pos = left_button_text_pos)    
    
    # Right Button
    right_button_x = 3*button_x - button_width/2
    right_button_y = button_y
    right_button_text_pos = 3*button_x, button_y + 0.5*button_height

    if checkMouseInButton(mouse=mouse, x = right_button_x, width= button_width,y = right_button_y, height= button_height):
        createButton(screen=screen, color_bg = WHITE, color_outline=color, 
                     position_x=right_button_x, position_y= right_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="I am good !", 
                     text_pos = right_button_text_pos)
    else:
        createButton(screen=screen, color_bg = color, color_outline= OUTLINE, 
                     position_x=right_button_x, position_y= right_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="I am good !", 
                     text_pos = right_button_text_pos)  
        
def checkGameButtonClick(screen, button_width, button_height, mouse, image_id, image_counter):
    """
    Verifies if one of the main game buttons has been clicked by the user.

    Keyword arguments: 
        screen: Surface 
            Surface resolution used for image representation      
        button_width: float
            The width of the button
        button_height: float
            The height of the button  
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

    button_x = screen_width/4
    button_y = screen_height - button_height - BUTTON_SPACING

    # Left Button
    left_button_x = button_x - button_width/2
    left_button_y = button_y

    # Image Generation button

    if checkMouseInButton(mouse=mouse, x = left_button_x, width= button_width,y = left_button_y, height= button_height):
        # Generates another image and updates the image counter
        for i in range(0,10):
            screen.fill(BACKGROUND_COLOR, (0, 0, screen_width, screen_height*0.75)) 

            number_images = len(next(os.walk("Loutish_Images"))[2]) - 1
            image_id = random.randint(0, number_images)
            image = selectLoutishImage(image_id)
            image = pygame.transform.scale(image, LoutishImageDimension.dimensions)

            centered_image_x, centered_image_y = image.get_rect(center=screen.get_rect().center).left, image.get_rect(center=screen.get_rect().center).top
            image_position = (centered_image_x, 0) # Center Image
            screen.blit(image, dest = image_position)
            pygame.display.update()
            time.sleep(0.05)
        image_counter += 1
    
    # Right Button
    right_button_x = 3*button_x - button_width/2
    right_button_y = button_y

    # Exit button

    if checkMouseInButton(mouse=mouse, x = right_button_x, width= button_width,y = right_button_y, height= button_height):
        gameScreen = False
        endScreen = True

    return gameScreen, endScreen, image_id, image_counter

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
    endgame_card_width = 2*screen_width/3
    endgame_card_height = 0.6*screen_height
    endgame_card_x = screen_width/2 - endgame_card_width/2
    endgame_card_y = 0.69*screen_height - endgame_card_height/2

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

    screen.blit(conclusion_message_stat, conclusion_message_stat.get_rect(center=(screen_width/2, screen_height*0.62)))
    screen.blit(conclusion_message_quote, conclusion_message_quote.get_rect(center=(screen_width/2, screen_height*0.67)))

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

    createEndScreenCard(screen=screen, screen_width=screen_width, screen_height=screen_height)

    big_font = pygame.font.SysFont('Comic Sans',60)
    title_message = big_font.render("You are cured !", True, OUTLINE)
    screen.blit(title_message, title_message.get_rect(center=(screen_width/2, screen_height*0.43)))

    counter_message = font.render(f"It only took you {image_counter} image{"s" if image_counter > 1 else ""} !", True, OUTLINE)
    screen.blit(counter_message, counter_message.get_rect(center=(screen_width/2, screen_height*0.5)))

    # Generates the final conclusion
    createEndScreenConclusion(screen=screen, font=font, screen_width=screen_width,
                              screen_height=screen_height, image_counter=image_counter)

    buttons_x = screen_width/2
    buttons_y = screen_height - button_height - BUTTON_SPACING

    # End Button
    end_button_x = buttons_x - button_width/2
    end_button_y = buttons_y
    end_button_text_pos = buttons_x, buttons_y + 0.5*button_height

    if checkMouseInButton(mouse=mouse, x = end_button_x, width= button_width,y = end_button_y, height= button_height):
        createButton(screen=screen, color_bg = WHITE, color_outline=primary_color, 
                     position_x=end_button_x, position_y= end_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Back to Home", 
                     text_pos = end_button_text_pos)
    else:
        createButton(screen=screen, color_bg = primary_color, color_outline= OUTLINE, 
                     position_x=end_button_x, position_y= end_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Back to Home", 
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
    button_x = screen_width/2
    button_y = screen_height - button_height - BUTTON_SPACING

    # End Button
    end_button_x = button_x - button_width/2
    end_button_y = button_y

    # Clicked End button
    if checkMouseInButton(mouse=mouse, x = end_button_x, width= button_width,y = end_button_y, height= button_height):

        # Saving Statistics
        statistics = pd.read_csv("statistics.csv")
        statistics.loc[len(statistics)] = [datetime.datetime.now(), image_counter]
        statistics.to_csv("statistics.csv", index=False)

        homeScreen = True,
        EndScreen = False

    return homeScreen, EndScreen