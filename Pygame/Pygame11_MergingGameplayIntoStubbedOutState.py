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

# CREATE THE FONT USED FOR DRAWING TEXT.
FONT_HEIGHT_IN_PIXELS = 16
font_filename = pygame.font.get_default_font()
font = pygame.font.Font(font_filename, FONT_HEIGHT_IN_PIXELS)

# DEFINE INITIAL PLAYER PARAMETERS.
score = 0
player_lives = 10
enemy_previously_touching_player = False
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

# DEFINE THE GAME STATES.
TITLE_SCREEN_STATE = "Title Screen"
MAIN_GAMEPLAY_STATE = "Main Gameplay State"
current_game_state = TITLE_SCREEN_STATE

time_elapsed_since_last_frame_in_seconds = 0

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
    global player_x, player_y
    global enemy_x, enemy_y
    global enemy_movement_x_velocity_in_pixels_per_second, enemy_movement_y_velocity_in_pixels_per_second
    global collectible_x, collectible_y
    global player_lives, score
    global enemy_previously_touching_player

    # KEEP THE PLAYER ON SCREEN.
    player_moved_off_left_side_of_screen = (player_x < 0)
    if player_moved_off_left_side_of_screen:
        player_x = 0

    PLAYER_SIZE_IN_PIXELS = 20
    MAX_PLAYER_X = SCREEN_WIDTH_IN_PIXELS - PLAYER_SIZE_IN_PIXELS
    player_moved_off_right_side_of_screen = (player_x > MAX_PLAYER_X)
    if player_moved_off_right_side_of_screen:
        player_x = MAX_PLAYER_X

    player_moved_off_top_side_of_screen = (player_y < 0)
    if player_moved_off_top_side_of_screen:
        player_y = 0

    MAX_PLAYER_Y = SCREEN_HEIGHT_IN_PIXELS - PLAYER_SIZE_IN_PIXELS
    player_moved_off_bottom_side_of_screen = (player_y > MAX_PLAYER_Y)
    if player_moved_off_bottom_side_of_screen:
        player_y = MAX_PLAYER_Y

    # MOVE THE ENEMY.
    # If the enemy moves off of one of the edges of the screen,
    # have the enemy bounce back in the opposite direction.
    enemy_moved_off_left_side_of_screen = (enemy_x < 0)
    ENEMY_SIZE_IN_PIXELS = 20
    MAX_ENEMY_X = SCREEN_WIDTH_IN_PIXELS - ENEMY_SIZE_IN_PIXELS
    enemy_moved_off_right_side_of_screen = (enemy_x > MAX_ENEMY_X)
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
    MAX_ENEMY_Y = SCREEN_HEIGHT_IN_PIXELS - ENEMY_SIZE_IN_PIXELS
    enemy_moved_off_bottom_side_of_screen = (enemy_y > MAX_ENEMY_Y)
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

        # CREATE A COLLECTIBLE IN A NEW POSITION.
        MAX_COLLECTIBLE_X = SCREEN_WIDTH_IN_PIXELS - COLLECTIBLE_SIZE_IN_PIXELS
        collectible_x = random.randrange(MAX_COLLECTIBLE_X + 1)
        MAX_COLLECTIBLE_Y = SCREEN_HEIGHT_IN_PIXELS - COLLECTIBLE_SIZE_IN_PIXELS
        collectible_y = random.randrange(MAX_COLLECTIBLE_Y + 1)

    # REMOVE A LIFE FROM THE PLAYER IF THE PLAYER IS TOUCHED BY THE ENEMY.
    enemy_touched_player = player_rectangle.colliderect(enemy_rectangle)
    if enemy_touched_player:
        # ONLY SUBTRACT A LIFE IF THE ENEMY WAS NOT ALREADY TOUCHING THE PLAYER.
        # The enemy may be touching the player for several frames as it moves
        # across the player.  For each "new" time the enemy starts touching
        # the player, only a maximum of one life should be lost.  By tracking
        # whether or not the enemy is touching the player or not, we can
        # keep too many lives from being subtracted at once.
        if not enemy_previously_touching_player:
            # SUBTRACT A LIFE FROM THE PLAYER.
            player_lives -= 1

            # TRACK THAT THE ENEMY IS NOW PREVIOUSLY TOUCHING THE PLAYER.
            enemy_previously_touching_player = True
    else:
        # TRACK THAT THE ENEMY IS HAS STOPPED TOUCHING THE PLAYER.
        enemy_previously_touching_player = False

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

    # DRAW THE PLAYER'S LIVES AND SCORE.
    NO_ANTI_ALIASING = False
    FONT_COLOR = pygame.Color(255, 255, 255)
    text_surface = font.render(
        "Lives: " + str(player_lives) + " Score: " + str(score),
        NO_ANTI_ALIASING,
        FONT_COLOR)
    TEXT_LEFT_X_TOP_Y_SCREEN_POSITION = (0, 0)
    screen.blit(text_surface, TEXT_LEFT_X_TOP_Y_SCREEN_POSITION)

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

        # RESPOND TO KEY PRESSES.
        if pygame.KEYDOWN == event.type:
            # MOVE THE PLAYER BASED ON KEYBOARD INPUT.
            # This only needs to happen if the game is in the main
            # gameplay state.
            if current_game_state == MAIN_GAMEPLAY_STATE:
                PLAYER_MOVEMENT_AMOUNT_IN_PIXELS = 10
                if pygame.K_UP == event.key:
                    player_y -= PLAYER_MOVEMENT_AMOUNT_IN_PIXELS
                if pygame.K_DOWN == event.key:
                    player_y += PLAYER_MOVEMENT_AMOUNT_IN_PIXELS
                if pygame.K_LEFT == event.key:
                    player_x -= PLAYER_MOVEMENT_AMOUNT_IN_PIXELS
                if pygame.K_RIGHT == event.key:
                    player_x += PLAYER_MOVEMENT_AMOUNT_IN_PIXELS

            # SWITCH GAME STATES BASED ON KEYBOARD INPUT.
            if pygame.K_RETURN == event.key:
                current_game_state = MAIN_GAMEPLAY_STATE
            elif pygame.K_ESCAPE == event.key:
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
