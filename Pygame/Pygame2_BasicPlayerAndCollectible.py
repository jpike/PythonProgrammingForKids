import pygame
import sys

# INITIALIZE PYGAME.
pygame.init()

# CREATE THE GAME SCREEN.
SCREEN_WIDTH_IN_PIXELS = 400
SCREEN_HEIGHT_IN_PIXELS = 400
screen = pygame.display.set_mode((SCREEN_WIDTH_IN_PIXELS, SCREEN_HEIGHT_IN_PIXELS))

# DEFINE THE PLAYER'S POSITION.
player_x = 200
player_y = 200

# DEFINE THE COLLECTIBLE'S POSITION.
collectible_x = 100
collectible_y = 100

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
            if pygame.K_RIGHT == event.key:
                player_x += PLAYER_MOVEMENT_AMOUNT_IN_PIXELS

    # CLEAR THE SCREEN FOR THE NEW FRAME.
    BACKGROUND_COLOR = pygame.Color(0, 0, 0)
    screen.fill(BACKGROUND_COLOR)

    # DRAW THE PLAYER.
    PLAYER_COLOR = pygame.Color(255, 255, 255)
    PLAYER_SIZE_IN_PIXELS = 20
    player_rectangle = pygame.Rect(player_x, player_y, PLAYER_SIZE_IN_PIXELS, PLAYER_SIZE_IN_PIXELS)
    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        player_rectangle)

    # DRAW THE COLLECTIBLE.
    COLLECTIBLE_COLOR = pygame.Color(255, 0, 0)
    COLLECTIBLE_SIZE_IN_PIXELS = 20
    collectible_rectangle = pygame.Rect(
        collectible_x, 
        collectible_y, 
        COLLECTIBLE_SIZE_IN_PIXELS, 
        COLLECTIBLE_SIZE_IN_PIXELS)
    pygame.draw.rect(
        screen,
        COLLECTIBLE_COLOR,
        collectible_rectangle)

    # DISPLAY THE UPDATED FRAME.
    pygame.display.update()
