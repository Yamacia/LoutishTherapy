import pygame
import sys
import os
import random
import time
from dimensions import *
from colors import *

def createButton(screen, position_x, position_y, button_width, button_height,
                  color_bg, color_outline, font, text, text_pos):
    """
    """
    pygame.draw.rect(screen, color_bg, [position_x, position_y, button_width, button_height])
    pygame.draw.rect(screen, color_outline, [position_x, position_y, button_width, button_height], 5)
    message = font.render(text, True, (OUTLINE))
    screen.blit(message, message.get_rect(center=text_pos))

def checkMouseInButton(mouse, x, y, width, height):
    """
    """
    return mouse[0] > x and mouse[0] < x + width and mouse[1] > y and mouse[1] < y + height


def createHomeButtons(screen, button_width, button_height, color, font, mouse):
    """
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
        createButton(screen=screen, color_bg = WHITE, color_outline=color, 
                     position_x=first_button_x, position_y= first_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="I need Therapy !", 
                     text_pos = first_button_text_pos)
    else:
        createButton(screen=screen, color_bg = color, color_outline= OUTLINE, 
                     position_x=first_button_x, position_y= first_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="I need Therapy !", 
                     text_pos = first_button_text_pos)       

    # Second Button
    second_button_x = button_x
    second_button_y = button_y + button_height + BUTTON_SPACING
    second_button_text_pos = screen_width/2, screen_height/2 + 1.5*button_height + 1*BUTTON_SPACING

    if checkMouseInButton(mouse=mouse, x = second_button_x, width= button_width, y = second_button_y, height= button_height):
        createButton(screen=screen, color_bg = WHITE, color_outline=color, 
                     position_x=second_button_x, position_y= second_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Settings", 
                     text_pos = second_button_text_pos)
    else:
        createButton(screen=screen, color_bg = color, color_outline= OUTLINE, 
                     position_x=second_button_x, position_y= second_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Settings",
                     text_pos= second_button_text_pos)         
        
    # Third Button
    third_button_x = button_x
    third_button_y = button_y + 2*(button_height + BUTTON_SPACING)
    third_button_text_pos = screen_width/2, screen_height/2 + 2.5*button_height + 2*BUTTON_SPACING
    
    if checkMouseInButton(mouse=mouse, x = third_button_x, width= button_width, y = third_button_y, height= button_height):
        createButton(screen=screen, color_bg = WHITE, color_outline=color, 
                     position_x=third_button_x, position_y= third_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Quit", 
                     text_pos = third_button_text_pos)
    else:
        createButton(screen=screen, color_bg = color, color_outline= OUTLINE, 
                     position_x=third_button_x, position_y= third_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Quit",
                     text_pos = third_button_text_pos)      
        
def checkHomeButtonClick(screen, button_width, button_height, mouse):
    """
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

    if checkMouseInButton(mouse=mouse, x = first_button_x, width= button_width,y = first_button_y, height= button_height):
        gameScreen = True     

    elif checkMouseInButton(mouse=mouse, x = second_button_x, width= button_width, y = second_button_y, height= button_height):
        optionScreen = True

    else:
        homeScreen = True
    return homeScreen, gameScreen, optionScreen       

def selectLoutishImage(image_id):
    """
    """
    images = next(os.walk("Loutish_Images"))[2]
    image = pygame.image.load(f"Loutish_Images/{images[image_id]}")
    return image

def createGameButtons(screen, button_width, button_height, color, font, mouse):
    """
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
        
def checkGameButtonClick(screen, button_width, button_height, mouse, image_id):
    """
    """
    gameScreen, endScreen = True, False

    # Center Button
    screen_left, screen_top, screen_width, screen_height = screen.get_rect()

    button_x = screen_width/4
    button_y = screen_height - button_height - BUTTON_SPACING

    # Left Button
    left_button_x = button_x - button_width/2
    left_button_y = button_y
    left_button_text_pos = button_x, button_y + 0.5*button_height

    if checkMouseInButton(mouse=mouse, x = left_button_x, width= button_width,y = left_button_y, height= button_height):
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
            print(image_id)
    
    # Right Button
    right_button_x = 3*button_x - button_width/2
    right_button_y = button_y
    right_button_text_pos = 3*button_x, button_y + 0.5*button_height

    # if checkMouseInButton(mouse=mouse, x = right_button_x, width= button_width,y = right_button_y, height= button_height):
    #     createButton(screen=screen, color_bg = WHITE, color_outline=color, 
    #                  position_x=right_button_x, position_y= right_button_y,
    #                  button_width=button_width, button_height=button_height,
    #                  font=font, text="I am good !", 
    #                  text_pos = right_button_text_pos)
    # else:
    #     createButton(screen=screen, color_bg = color, color_outline= OUTLINE, 
    #                  position_x=right_button_x, position_y= right_button_y,
    #                  button_width=button_width, button_height=button_height,
    #                  font=font, text="I am good !", 
    #                  text_pos = right_button_text_pos)  

    return gameScreen, endScreen, image_id
