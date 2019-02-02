import pygame
import random
import sys

# INITIALIZE PYGAME.
pygame.init()

# CREATE THE GAME SCREEN.
SCREEN_WIDTH_IN_PIXELS = 400
SCREEN_HEIGHT_IN_PIXELS = 400
screen = pygame.display.set_mode((SCREEN_WIDTH_IN_PIXELS, SCREEN_HEIGHT_IN_PIXELS))

# DEFINE THE PLAYER'S INITIAL SCORE.
score = 0

# DEFINE THE PLAYER'S POSITION.
player_x = 200
player_y = 200

# DEFINE INFORMATION ABOUT THE COLLECTIBLE.
collectible_x = 100
collectible_y = 100
collectible_width_in_pixels = 20
collectible_height_in_pixels = 20
collectible_color = pygame.Color(255, 0, 0)

# RUN THE GAME UNTIL THE USER CHOOSES TO EXIT.
while True:
    # HANDLE ANY EVENTS SENT TO THE GAME PROGRAM.
    for event in pygame.event.get():
        # EXIT THE GAME IF THE USER CHOSE TO QUIT.
        if pygame.QUIT == event.type:
            # pygame.quit() may still leave the window up,
            # so sys.exit() is needed to fully close the program.
            pygame.quit()
            sys.exit()

        # MOVE THE PLAYER BASED ON KEYBOARD INPUT.
        PLAYER_MOVEMENT_AMOUNT_IN_PIXELS = 10
        if pygame.KEYDOWN == event.type:
            if pygame.K_UP == event.key:
                player_y -= PLAYER_MOVEMENT_AMOUNT_IN_PIXELS
            if pygame.K_DOWN == event.key:
                player_y += PLAYER_MOVEMENT_AMOUNT_IN_PIXELS
            if pygame.K_LEFT == event.key:
                player_x -= PLAYER_MOVEMENT_AMOUNT_IN_PIXELS
            if pygame.K_RIGHT == event.key:
                player_x += PLAYER_MOVEMENT_AMOUNT_IN_PIXELS

    # UPDATE THE POSITIONS OF OBJECTS IN THE GAME WORLD.
    # These need to be updated each frame because some objects might move.
    PLAYER_SIZE_IN_PIXELS = 20
    player_rectangle = pygame.Rect(
        player_x,
        player_y,
        PLAYER_SIZE_IN_PIXELS,
        PLAYER_SIZE_IN_PIXELS)
    collectible_rectangle = pygame.Rect(
        collectible_x, 
        collectible_y, 
        collectible_width_in_pixels, 
        collectible_height_in_pixels)

    # COLLECT THE COLLECTIBLE IF THE PLAYER TOUCHES IT.
    player_touched_collectible = player_rectangle.colliderect(collectible_rectangle)
    if player_touched_collectible:
        # COUNT THE COLLECTIBLE IN THE PLAYER'S SCORE.
        score += 1
        print("Score: " + str(score))

        # RANDOMLY GENERATE A NEW COLLECTIBLE.
        MIN_COLLECTIBLE_SIZE_IN_PIXELS = 5
        MAX_COLLECTIBLE_SIZE_IN_PIXELS = 50
        collectible_width_in_pixels = random.randrange(
            MIN_COLLECTIBLE_SIZE_IN_PIXELS,
            MAX_COLLECTIBLE_SIZE_IN_PIXELS)
        collectible_height_in_pixels = random.randrange(
            MIN_COLLECTIBLE_SIZE_IN_PIXELS,
            MAX_COLLECTIBLE_SIZE_IN_PIXELS)
        
        MAX_COLLECTIBLE_X = SCREEN_WIDTH_IN_PIXELS - collectible_width_in_pixels
        collectible_x = random.randrange(MAX_COLLECTIBLE_X + 1)
        MAX_COLLECTIBLE_Y = SCREEN_HEIGHT_IN_PIXELS - collectible_height_in_pixels
        collectible_y = random.randrange(MAX_COLLECTIBLE_Y + 1)

        MAX_COLOR_COMPONENT = 255
        collectible_color.r = random.randrange(MAX_COLOR_COMPONENT + 1)
        collectible_color.g = random.randrange(MAX_COLOR_COMPONENT + 1)
        collectible_color.b = random.randrange(MAX_COLOR_COMPONENT + 1)

    # CLEAR THE SCREEN FOR THE NEW FRAME.
    BACKGROUND_COLOR = pygame.Color(0, 0, 0)
    screen.fill(BACKGROUND_COLOR)

    # DRAW THE PLAYER.
    PLAYER_COLOR = pygame.Color(255, 255, 255)
    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        player_rectangle)

    # DRAW THE COLLECTIBLE.
    pygame.draw.rect(
        screen,
        collectible_color,
        collectible_rectangle)

    # DISPLAY THE UPDATED FRAME.
    pygame.display.update()
