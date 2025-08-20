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
button_spacing = BUTTON_SPACING
button_outline = BUTTON_OUTLINE

# Defining a font
font = pygame.font.SysFont(MAIN_FONT, FONT_SIZE)

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
        createHome(screen = screen, button_width = button_width, button_height = button_height, button_spacing = button_spacing,
                   button_outline = button_outline, font = font, mouse = mouse)
        
    if gameScreen:

        # Game Screen
        createGame(screen = screen, button_width = button_width, button_height = button_height, button_spacing = button_spacing,
                   button_outline = button_outline, font = font, mouse = mouse, image_id = LoutishImageID)
        
    if endScreen:

        # End Screen
        createEnd(screen = screen, button_width = button_width, button_height = button_height, button_spacing = button_spacing,
                   button_outline = button_outline, font = font, mouse = mouse, image_id = LoutishImageID, image_counter = image_counter)

    # Handle events  
    for event in pygame.event.get():  
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == MouseAction.LEFT_CLICK.value:

            # Check in what screen we are in
            if homeScreen:
                homeScreen, gameScreen, optionScreen = checkHomeButtonClick(screen = screen, button_width = button_width,
                            button_height = button_height, button_spacing = button_spacing, mouse = mouse)
                
            elif gameScreen:
                gameScreen, endScreen, LoutishImageID, image_counter = checkGameButtonClick(screen = screen, button_width = button_width,
                            button_height = button_height, button_spacing = button_spacing, mouse = mouse, image_id = LoutishImageID, image_counter = image_counter)
                
            elif endScreen:
                homeScreen, endScreen = checkEndButtonClick(screen = screen, button_width = button_width,
                            button_height = button_height, button_spacing = button_spacing, mouse = mouse, image_counter = image_counter)
                
        elif event.type == pygame.VIDEORESIZE:
            button_width, button_height = getButtonDimensions(screen = screen)
            button_spacing = getButtonSpacing(screen = screen)
            button_outline = getButtonOutlineDimensions(screen = screen)
            font = pygame.font.SysFont(MAIN_FONT, getFontDimensions(screen = screen))
            pygame.display.update()

        elif event.type == pygame.QUIT:  
            # Exit game

            pygame.quit()  
            sys.exit()

    # Update the display  
    pygame.display.flip()  
  
    # Limit the frame rate  
    clock.tick(60)