from functions import *

# Initialize PyGame
pygame.init()
pygame.display.set_caption("Loutish Therapy")
# screen = pygame.display.set_mode(ScreenDimensions.dimensions, pygame.RESIZABLE)  
screen = pygame.display.set_mode(ScreenDimensions.dimensions)
homeScreen = True
gameScreen, optionScreen, endScreen = False, False, False
number_images = len(next(os.walk("Loutish_Images"))[2]) - 1
LoutishImageID = random.randint(0, number_images)

# Defining a font
smallfont = pygame.font.SysFont('Comic Sans',35)

# Loading music
pygame.mixer.init()
pygame.mixer.music.load("Music/shelter.mp3")
pygame.mixer.music.play()

# Set up the clock for frame rate control  
clock = pygame.time.Clock()  
  
# Main game loop  
while True: 
    screen.fill(BACKGROUND_COLOR) 
    mouse = pygame.mouse.get_pos()

    # Home Buttons
    button_width, button_height = ButtonDimension.dimensions
    if homeScreen:
        
        # Home Screen
        image = pygame.image.load("Game_Images/title_screen.png")
        image = pygame.transform.scale(image, TitleLogoDimension.dimensions)

        centered_image_x, centered_image_y = image.get_rect(center=screen.get_rect().center).left, image.get_rect(center=screen.get_rect().center).top
        image_position = (centered_image_x, 0) # Center Title Logo
        screen.blit(image, dest = image_position)
        createHomeButtons(screen=screen, button_width=button_width,
                        button_height=button_height, color=LOUTISH_COLOR,
                        font=smallfont, mouse=mouse)
        
    if gameScreen:

        # Game Screen
        image = selectLoutishImage(LoutishImageID)
        image = pygame.transform.scale(image, LoutishImageDimension.dimensions)

        centered_image_x, centered_image_y = image.get_rect(center=screen.get_rect().center).left, image.get_rect(center=screen.get_rect().center).top
        image_position = (centered_image_x, 0) # Center Image
        screen.blit(image, dest = image_position)
        createGameButtons(screen=screen, button_width=button_width,
                        button_height=button_height, color=LOUTISH_COLOR,
                        font=smallfont, mouse=mouse)
        

    # Handle events  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if homeScreen:
                homeScreen, gameScreen, optionScreen = checkHomeButtonClick(screen=screen, button_width=button_width,
                            button_height=button_height, mouse=mouse)
            if gameScreen:
                gameScreen, endScreen, LoutishImageID = checkGameButtonClick(screen=screen, button_width=button_width,
                            button_height=button_height, mouse=mouse, image_id=LoutishImageID)
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