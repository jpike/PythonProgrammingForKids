import pygame
import random
import sys

# INITIALIZE PYGAME.
pygame.init()

# CREATE THE GAME SCREEN.
SCREEN_WIDTH_IN_PIXELS = 400
SCREEN_HEIGHT_IN_PIXELS = 400
screen = pygame.display.set_mode(
    (SCREEN_WIDTH_IN_PIXELS, SCREEN_HEIGHT_IN_PIXELS))

# DEFINE INITIAL PLAYER PARAMETERS.
score = 0
player_lives = 10
player_invincible = False
time_player_has_been_invincible_in_seconds = 0
player_x = 200
player_y = 200

# DEFINE INFORMATION ABOUT THE COLLECTIBLE.
collectible_x = 100
collectible_y = 100

# DEFINE INITIAL ENEMY PARAMETERS.
enemy_x = 0
enemy_y = 200
enemy_movement_x_velocity_in_pixels_per_second = 100
enemy_movement_y_velocity_in_pixels_per_second = 120

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

    # UPDATE THE INVINCIBILITY STATUS OF THE PLAYER.
    if player_invincible:
        # The player is only allowed to stay invincible for a short amount of time.
        time_player_has_been_invincible_in_seconds += time_elapsed_since_last_frame_in_seconds
        MAX_TIME_PLAYER_ALLOWED_TO_BE_INVINCIBLE_IN_SECONDS = 1
        player_invincible = (
            time_player_has_been_invincible_in_seconds <= MAX_TIME_PLAYER_ALLOWED_TO_BE_INVINCIBLE_IN_SECONDS)

    # MOVE THE ENEMY.
    # If the enemy moves off of one of the edges of the screen,
    # have the enemy bounce back in the opposite direction.
    enemy_moved_off_left_side_of_screen = (enemy_x < 0)
    enemy_moved_off_right_side_of_screen = (enemy_x > SCREEN_WIDTH_IN_PIXELS)
    enemy_moved_off_left_or_right_side_of_screen = (
        enemy_moved_off_left_side_of_screen or
        enemy_moved_off_right_side_of_screen)
    if enemy_moved_off_left_or_right_side_of_screen:
        enemy_movement_x_velocity_in_pixels_per_second *= -1
    enemy_x_movement_amount_in_pixels = (
        enemy_movement_x_velocity_in_pixels_per_second
        *
        time_elapsed_since_last_frame_in_seconds)
    enemy_x += enemy_x_movement_amount_in_pixels

    enemy_moved_off_top_side_of_screen = (enemy_y < 0)
    enemy_moved_off_bottom_side_of_screen = (enemy_y > SCREEN_HEIGHT_IN_PIXELS)
    enemy_moved_off_top_or_bottom_side_of_screen = (
        enemy_moved_off_top_side_of_screen or
        enemy_moved_off_bottom_side_of_screen)
    if enemy_moved_off_top_or_bottom_side_of_screen:
        enemy_movement_y_velocity_in_pixels_per_second *= -1
    enemy_y_movement_amount_in_pixels = (
        enemy_movement_y_velocity_in_pixels_per_second
        *
        time_elapsed_since_last_frame_in_seconds)
    enemy_y += enemy_y_movement_amount_in_pixels

    # UPDATE THE POSITIONS OF OBJECTS IN THE GAME WORLD.
    # These need to be updated each frame because some objects might move.
    PLAYER_SIZE_IN_PIXELS = 20
    player_rectangle = pygame.Rect(
        player_x,
        player_y,
        PLAYER_SIZE_IN_PIXELS,
        PLAYER_SIZE_IN_PIXELS)
    COLLECTIBLE_SIZE_IN_PIXELS = 20
    collectible_rectangle = pygame.Rect(
        collectible_x, 
        collectible_y, 
        COLLECTIBLE_SIZE_IN_PIXELS, 
        COLLECTIBLE_SIZE_IN_PIXELS)
    ENEMY_SIZE_IN_PIXELS = 20
    enemy_rectangle = pygame.Rect(
        enemy_x,
        enemy_y,
        ENEMY_SIZE_IN_PIXELS,
        ENEMY_SIZE_IN_PIXELS)

    # COLLECT THE COLLECTIBLE IF THE PLAYER TOUCHES IT.
    player_touched_collectible = player_rectangle.colliderect(collectible_rectangle)
    if player_touched_collectible:
        # COUNT THE COLLECTIBLE IN THE PLAYER'S SCORE.
        score += 1
        print("Score: " + str(score))

        # CREATE A COLLECTIBLE IN A NEW POSITION.
        MAX_COLLECTIBLE_X = SCREEN_WIDTH_IN_PIXELS - COLLECTIBLE_SIZE_IN_PIXELS
        collectible_x = random.randrange(MAX_COLLECTIBLE_X + 1)
        MAX_COLLECTIBLE_Y = SCREEN_HEIGHT_IN_PIXELS - COLLECTIBLE_SIZE_IN_PIXELS
        collectible_y = random.randrange(MAX_COLLECTIBLE_Y + 1)

    # REMOVE A LIFE FROM THE PLAYER IF THE PLAYER IS TOUCHED BY THE ENEMY.
    enemy_touched_player = player_rectangle.colliderect(enemy_rectangle)
    if enemy_touched_player:
        # CHECK IF THE PLAYER IS CURRENTLY INVINCIBLE.
        # To prevent a collision of the enemy with the player from subtracting
        # more than one life per collision, the player is given a small invincibility
        # period where the player can't lose a life even if the enemy is still touching
        # the player and hasn't moved away yet.
        if not player_invincible:
            # SUBTRACT A LIFE FROM THE PLAYER.
            player_lives -= 1
            print("Lives: " + str(player_lives))

            # MARK THE PLAYER AS TEMPORARILY INVINCIBLE.
            player_invincible = True
            time_player_has_been_invincible_in_seconds = 0

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
    COLLECTIBLE_COLOR = pygame.Color(255, 0, 0)
    pygame.draw.rect(
        screen,
        COLLECTIBLE_COLOR,
        collectible_rectangle)

    # DRAW THE ENEMY.
    ENEMY_COLOR = pygame.Color(0, 0, 255)
    pygame.draw.rect(
        screen,
        ENEMY_COLOR,
        enemy_rectangle)

    # DISPLAY THE UPDATED FRAME.
    pygame.display.update()
