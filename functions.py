import pygame
import sys

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

    # Center button
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
                     font=font, text="Statistics", 
                     text_pos = second_button_text_pos)
    else:
        createButton(screen=screen, color_bg = color, color_outline= OUTLINE, 
                     position_x=second_button_x, position_y= second_button_y,
                     button_width=button_width, button_height=button_height,
                     font=font, text="Statistics",
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