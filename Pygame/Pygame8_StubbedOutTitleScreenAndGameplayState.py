import pygame
import random
import sys

TITLE_SCREEN_STATE = "Title Screen"
MAIN_GAMEPLAY_STATE = "Main Gameplay State"
current_game_state = TITLE_SCREEN_STATE

def UpdateAndDrawTitleScreen():
    print("Title screen")

def UpdateAndDrawMainGameplayState():
    print("Main gameplay state")

# INITIALIZE PYGAME.
pygame.init()

# CREATE THE GAME SCREEN.
SCREEN_WIDTH_IN_PIXELS = 400
SCREEN_HEIGHT_IN_PIXELS = 400
screen = pygame.display.set_mode(
    (SCREEN_WIDTH_IN_PIXELS, SCREEN_HEIGHT_IN_PIXELS))

# CREATE THE FONT USED FOR DRAWING TEXT.
FONT_HEIGHT_IN_PIXELS = 16
font_filename = pygame.font.get_default_font()
font = pygame.font.Font(font_filename, FONT_HEIGHT_IN_PIXELS)

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

        # CHANGE THE GAME STATE IF THE USER PRESSES A KEY.
        if pygame.KEYDOWN == event.type:
            if current_game_state == TITLE_SCREEN_STATE:
                current_game_state = MAIN_GAMEPLAY_STATE
            else:
                current_game_state = TITLE_SCREEN_STATE

    # UPDATE THE GAME CLOCK.
    # This will pause our game loop temporarily to try and hit
    # the target framerate.
    FRAMES_PER_SECOND = 60
    time_elapsed_since_last_frame_in_ms = clock.tick(FRAMES_PER_SECOND)
    MILLISECONDS_PER_SECOND = 1000
    time_elapsed_since_last_frame_in_seconds = (
        time_elapsed_since_last_frame_in_ms
        /
        MILLISECONDS_PER_SECOND)       

    # CLEAR THE SCREEN FOR THE NEW FRAME.
    BACKGROUND_COLOR = pygame.Color(0, 0, 0)
    screen.fill(BACKGROUND_COLOR)

    # DRAW THE CURRENT GAME STATE.
    if current_game_state == TITLE_SCREEN_STATE:
        UpdateAndDrawTitleScreen()
    elif current_game_state == MAIN_GAMEPLAY_STATE:
        UpdateAndDrawMainGameplayState()

    # DISPLAY THE UPDATED FRAME.
    pygame.display.update()
