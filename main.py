from functions import *
from home import *
from game import *
from options import *
from endscreen import *

# First launch
if not os.path.isfile("statistics.csv"):
    statistics = pd.DataFrame(columns=[
        "Date",
        "Image Count"
    ])
    statistics.to_csv('statistics.csv', index=False)

# Initialize PyGame
screen = initializeGame()
homeScreen, gameScreen, optionScreen, endScreen = initializeScreenState()

# Generating first Loutish image
number_images = len(next(os.walk("Loutish_Images"))[2]) - 1
LoutishImageID = random.randint(0, number_images)
image_counter = 1

# Primary Buttons
button_width, button_height = ButtonDimension.dimensions

# Defining a font
font = pygame.font.SysFont(MAIN_FONT, 35)

# Loading music
loadMusic()

# Set up the clock for frame rate control  
clock = pygame.time.Clock()  
  
# Main game loop  
while True: 
    screen.fill(BACKGROUND_COLOR) 
    mouse = pygame.mouse.get_pos()

    if homeScreen:
        
        # Home Screen
        createHome(screen = screen, button_width = button_width, button_height = button_height,
                   font = font, mouse = mouse)
        
    if gameScreen:

        # Game Screen
        createGame(screen = screen, button_width = button_width, button_height = button_height,
                   font = font, mouse = mouse, image_id = LoutishImageID)
        
    if endScreen:

        # End Screen
        createEnd(screen = screen, button_width = button_width, button_height = button_height,
                   font = font, mouse = mouse, image_id = LoutishImageID, image_counter = image_counter)

    # Handle events  
    for event in pygame.event.get():  
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check in what screen we are in

            if homeScreen:
                homeScreen, gameScreen, optionScreen = checkHomeButtonClick(screen = screen, button_width = button_width,
                            button_height = button_height, mouse = mouse)
                
            elif gameScreen:
                gameScreen, endScreen, LoutishImageID, image_counter = checkGameButtonClick(screen = screen, button_width = button_width,
                            button_height = button_height, mouse = mouse, image_id = LoutishImageID, image_counter = image_counter)
                
            elif endScreen:
                homeScreen, endScreen = checkEndButtonClick(screen = screen, button_width = button_width,
                            button_height = button_height, mouse = mouse, image_counter = image_counter)
                
        # elif event.type == pygame.VIDEORESIZE:
        #     image_resized_x, image_resized_y = screen.get_size()
        #     image = pygame.transform.scale(image, (image_resized_x/2, image_resized_y/2))
        #     image_position = (image.get_rect(center=screen.get_rect().center).left, 0) # Center Title Logo
        #     screen.blit(image, dest= image_position)
        #     pygame.display.update()

        elif event.type == pygame.QUIT:  
            # Exit game

            pygame.quit()  
            sys.exit()

    # Update the display  
    pygame.display.flip()  
  
    # Limit the frame rate  
    clock.tick(60)