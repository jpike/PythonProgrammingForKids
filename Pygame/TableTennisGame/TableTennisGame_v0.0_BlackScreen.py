## Version 0 of a video game version of "table tennis"
## (https://en.wikipedia.org/wiki/Table_tennis).
## This initial version basically just displays a black screen.

import pygame
import sys

# INITIALIZE PYGAME.
pygame.init()

# CREATE THE GAME SCREEN.
SCREEN_WIDTH_IN_PIXELS = 600
SCREEN_HEIGHT_IN_PIXELS = 400
screen = pygame.display.set_mode((SCREEN_WIDTH_IN_PIXELS, SCREEN_HEIGHT_IN_PIXELS))
pygame.display.set_caption("Table Tennis Game")

# RUN THE GAME UNTIL THE USER CHOOSES TO EXIT.
clock = pygame.time.Clock()
while True:
    # HANDLE ANY EVENTS SENT TO THE GAME PROGRAM.
    for event in pygame.event.get():
        # EXIT THE GAME IF THE USER CHOSE TO QUIT.
        if pygame.QUIT == event.type:
            # pygame.quit() may still leave the window up,
            # so sys.exit() is needed to fully close the program.
            pygame.quit()
            sys.exit()

    # UPDATE THE GAME CLOCK.
    # This will pause our game loop temporarily to try and hit the target frame rate.
    FRAMES_PER_SECOND = 60
    time_elapsed_since_last_frame_in_ms = clock.tick(FRAMES_PER_SECOND)
    MILLISECONDS_PER_SECOND = 1000
    time_elapsed_since_last_frame_in_seconds = (time_elapsed_since_last_frame_in_ms / MILLISECONDS_PER_SECOND)

    # CLEAR THE SCREEN FOR THE NEW FRAME.
    BACKGROUND_COLOR = pygame.Color(0, 0, 0)
    screen.fill(BACKGROUND_COLOR)

    # DISPLAY THE UPDATED FRAME.
    pygame.display.update()
