import pygame
import sys

# INITIALIZE PYGAME.
pygame.init()

# CREATE THE GAME SCREEN.
SCREEN_WIDTH_IN_PIXELS = 400
SCREEN_HEIGHT_IN_PIXELS = 400
screen = pygame.display.set_mode(
    (SCREEN_WIDTH_IN_PIXELS, SCREEN_HEIGHT_IN_PIXELS))

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

    # CLEAR THE SCREEN FOR THE NEW FRAME.
    BACKGROUND_COLOR = pygame.Color(0, 0, 0)
    screen.fill(BACKGROUND_COLOR)

    # DRAW THE TOP-LEFT RECTANGLE.
    top_left_rectangle_left_x_position = 0
    top_left_rectangle_top_y_position = 0
    RECTANGLE_SIZE_IN_PIXELS = 20
    top_left_rectangle = pygame.Rect(
        top_left_rectangle_left_x_position,
        top_left_rectangle_top_y_position,
        RECTANGLE_SIZE_IN_PIXELS,
        RECTANGLE_SIZE_IN_PIXELS)
    TOP_LEFT_RECTANGLE_COLOR = pygame.Color(0, 255, 0)
    pygame.draw.rect(
        screen,
        TOP_LEFT_RECTANGLE_COLOR,
        top_left_rectangle)

    # DRAW THE TOP-RIGHT RECTANGLE.
    top_right_rectangle_left_x_position = (
        SCREEN_WIDTH_IN_PIXELS - RECTANGLE_SIZE_IN_PIXELS)
    top_right_rectangle_top_y_position = 0
    top_right_rectangle = pygame.Rect(
        top_right_rectangle_left_x_position,
        top_right_rectangle_top_y_position,
        RECTANGLE_SIZE_IN_PIXELS,
        RECTANGLE_SIZE_IN_PIXELS)
    TOP_RIGHT_RECTANGLE_COLOR = pygame.Color(0, 0, 255)
    pygame.draw.rect(
        screen,
        TOP_RIGHT_RECTANGLE_COLOR,
        top_right_rectangle)

    # DRAW THE BOTTOM-LEFT RECTANGLE.
    bottom_left_rectangle_left_x_position = 0
    bottom_left_rectangle_top_y_position = (
        SCREEN_HEIGHT_IN_PIXELS - RECTANGLE_SIZE_IN_PIXELS)
    bottom_left_rectangle = pygame.Rect(
        bottom_left_rectangle_left_x_position,
        bottom_left_rectangle_top_y_position,
        RECTANGLE_SIZE_IN_PIXELS,
        RECTANGLE_SIZE_IN_PIXELS)
    BOTTOM_LEFT_RECTANGLE_COLOR = pygame.Color(255, 255, 0)
    pygame.draw.rect(
        screen,
        BOTTOM_LEFT_RECTANGLE_COLOR,
        bottom_left_rectangle)

    # DRAW THE BOTTOM-RIGHT RECTANGLE.
    bottom_right_rectangle_left_x_position = (
        SCREEN_WIDTH_IN_PIXELS - RECTANGLE_SIZE_IN_PIXELS)
    bottom_right_rectangle_top_y_position = (
        SCREEN_HEIGHT_IN_PIXELS - RECTANGLE_SIZE_IN_PIXELS)
    bottom_right_rectangle = pygame.Rect(
        bottom_right_rectangle_left_x_position,
        bottom_right_rectangle_top_y_position,
        RECTANGLE_SIZE_IN_PIXELS,
        RECTANGLE_SIZE_IN_PIXELS)
    BOTTOM_RIGHT_RECTANGLE_COLOR = pygame.Color(255, 0, 255)
    pygame.draw.rect(
        screen,
        BOTTOM_RIGHT_RECTANGLE_COLOR,
        bottom_right_rectangle)

    # DRAW THE CENTER RECTANGLE.
    screen_center_x_position = SCREEN_WIDTH_IN_PIXELS / 2
    screen_center_y_position = SCREEN_HEIGHT_IN_PIXELS / 2
    rectangle_half_size_in_pixels = RECTANGLE_SIZE_IN_PIXELS / 2
    center_rectangle_left_x_position = (
        screen_center_x_position - rectangle_half_size_in_pixels)
    center_rectangle_top_y_position = (
        screen_center_y_position - rectangle_half_size_in_pixels)
    center_rectangle = pygame.Rect(
        center_rectangle_left_x_position,
        center_rectangle_top_y_position,
        RECTANGLE_SIZE_IN_PIXELS,
        RECTANGLE_SIZE_IN_PIXELS)
    CENTER_RECTANGLE_COLOR = pygame.Color(255, 0, 0)
    pygame.draw.rect(
        screen,
        CENTER_RECTANGLE_COLOR,
        center_rectangle)

    # DISPLAY THE UPDATED FRAME.
    pygame.display.update()
