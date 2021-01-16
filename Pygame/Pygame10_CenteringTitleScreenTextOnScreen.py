import pygame
import random
import sys

TITLE_SCREEN_STATE = "Title Screen"
MAIN_GAMEPLAY_STATE = "Main Gameplay State"
current_game_state = TITLE_SCREEN_STATE

def UpdateAndDrawTitleScreen():
    NO_ANTI_ALIASING = False
    FONT_COLOR = pygame.Color(255, 255, 255)
    text_surface = font.render(
        "Title Screen",
        NO_ANTI_ALIASING,
        FONT_COLOR)

    screen_center_x_position = SCREEN_WIDTH_IN_PIXELS / 2
    screen_center_y_position = SCREEN_HEIGHT_IN_PIXELS / 2
    (text_width_in_pixels, text_height_in_pixels) = text_surface.get_size()
    text_half_width_in_pixels = text_width_in_pixels / 2
    text_half_height_in_pixels = text_height_in_pixels / 2
    text_center_x_screen_position = screen_center_x_position - text_half_width_in_pixels
    text_center_y_screen_position = screen_center_y_position - text_half_height_in_pixels
    text_left_x_top_y_screen_position = (text_center_x_screen_position, text_center_y_screen_position)
    screen.blit(text_surface, text_left_x_top_y_screen_position)

def UpdateAndDrawMainGameplayState():
    NO_ANTI_ALIASING = False
    FONT_COLOR = pygame.Color(255, 255, 255)
    text_surface = font.render(
        "Main Gameplay State",
        NO_ANTI_ALIASING,
        FONT_COLOR)
    TEXT_LEFT_X_TOP_Y_SCREEN_POSITION = (0, 0)
    screen.blit(text_surface, TEXT_LEFT_X_TOP_Y_SCREEN_POSITION)

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
            sys.exit(0)

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
