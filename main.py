import pygame
import sys

from dimensions import ScreenDimensions, TitleLogoDimension
from colors import BackgroundColor

# Initialize PyGame
pygame.init()
pygame.display.set_caption("Loutish Therapy")
# screen = pygame.display.set_mode(ScreenDimensions.dimensions, pygame.RESIZABLE)  
screen = pygame.display.set_mode(ScreenDimensions.dimensions)  

# Home Screen
image = pygame.image.load("Game_Images/title_screen.png")
image = pygame.transform.scale(image, TitleLogoDimension.dimensions)
image_position = (image.get_rect(center=screen.get_rect().center).left, 0) # Center Title Logo
  
# Set up the clock for frame rate control  
clock = pygame.time.Clock()  
  
# Main game loop  
while True: 
    screen.fill(BackgroundColor.rgb) 
    screen.blit(image, dest = image_position)
    # Handle events  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            sys.exit()
        # elif event.type == pygame.VIDEORESIZE:
        #     image_resized_x, image_resized_y = screen.get_size()
        #     image = pygame.transform.scale(image, (image_resized_x/2, image_resized_y/2))
        #     image_position = (image.get_rect(center=screen.get_rect().center).left, 0) # Center Title Logo
        #     screen.blit(image, dest= image_position)
        #     pygame.display.update()

    # Update the display  
    pygame.display.flip()  
  
    # Limit the frame rate  
    clock.tick(60)