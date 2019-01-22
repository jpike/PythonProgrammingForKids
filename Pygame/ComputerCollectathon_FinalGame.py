import pygame
import random
import sys

# DEFINE CLASSES.
## A 2D mathematical vector.
## The type of the components depends on what's given to the vector.
class Vector2(object):
    ## Creates a scaled version of a vector.
    ## @param[in]   scale_factor - The amount to scale the vector.
    ## @param[in]   vector - The Vector2 to scale.
    ## @return The scaled Vector2.
    def Scale(scale_factor, vector):
        scaled_x = scale_factor * vector.X
        scaled_y = scale_factor * vector.Y
        return Vector2(scaled_x, scaled_y)

    ## Negates a vector.
    ## @param[in]   vector - The Vector2 to negate.
    ## @return The negated Vector2.
    def Negate(vector):
        negated_vector = Vector2.Scale(-1, vector)
        return negated_vector

    ## Adds two vectors.
    ## @param[in]   vector1 - One Vector2 to add.
    ## @param[in]   vector2 - The other Vector2 to add.
    ## @return The Vector2 addition of the provided vectors.
    def Add(vector1, vector2):
        added_x = vector1.X + vector2.X
        added_y = vector1.Y + vector2.Y
        return Vector2(added_x, added_y)
    
    ## Initializes the vector's components.
    ## @param[in]   x - The x component.
    ## @param[in]   y - The y component.
    def __init__(self, x, y):
        ## The x (horizontal) component.
        self.X = x
        ## The y (horizontal) component.
        self.Y = y

class Player(object):
    def __init__(self, screen_position):
        self.ScreenPosition = screen_position
        self.SizeInPixels = 20
        self.Color = pygame.Color(255, 255, 255)
        self.Score = 0
        self.Lives = 10

class Collectible(object):
    def __init__(self, screen_position, size_in_pixels, color):
        self.ScreenPosition = screen_position
        self.SizeInPixels = size_in_pixels
        self.Color = color

class Enemy(object):
    def __init__(self, screen_position, size_in_pixels, move_speed_in_pixels_per_second, color):
        self.ScreenPosition = screen_position
        self.SizeInPixels = size_in_pixels
        self.MoveSpeedInPixelsPerSecond = move_speed_in_pixels_per_second
        self.Color = color

        MAX_VELOCITY_COMPONENT_IN_PIXELS = 1
        x_screen_velocity = random.randrange(
            -MAX_VELOCITY_COMPONENT_IN_PIXELS,
            MAX_VELOCITY_COMPONENT_IN_PIXELS)
        y_screen_velocity = random.randrange(
            -MAX_VELOCITY_COMPONENT_IN_PIXELS,
            MAX_VELOCITY_COMPONENT_IN_PIXELS)
        if x_screen_velocity == 0:
            x_screen_velocity = 0.5
        if y_screen_velocity == 0:
            y_screen_velocity = 0.5
        self.MoveDirection = Vector2(x_screen_velocity, y_screen_velocity)

class Level(object):
    def __init__(
        self,
        background_color,
        collectible_count,
        collectible_size_in_pixels,
        collectible_color, 
        enemy_count,
        enemy_size_in_pixels,
        enemy_move_speed_in_pixels_per_second,
        enemy_color):

        self.BackgroundColor = background_color
        self.CollectibleCount = collectible_count
        self.EnemyCount = enemy_count
        self.EnemyMoveSpeedInPixelsPerSecond = enemy_move_speed_in_pixels_per_second
        
        # GENERATE THE APPROPRIATE NUMBER OF COLLECTIBLES.
        self.Collectibles = []
        for collectibe_index in range(collectible_count):
            random_x = random.randrange(SCREEN_WIDTH_IN_PIXELS - collectible_size_in_pixels)
            random_y = random.randrange(SCREEN_HEIGHT_IN_PIXELS - collectible_size_in_pixels)
            screen_position = Vector2(random_x, random_y)
            collectible = Collectible(screen_position, collectible_size_in_pixels, collectible_color)
            self.Collectibles.append(collectible)

        # GENERATE THE APPROPRIATE NUMBER OF ENEMIES.
        self.Enemies = []
        for enemy_index in range(enemy_count):
            random_x = random.randrange(SCREEN_WIDTH_IN_PIXELS - enemy_size_in_pixels)
            random_y = random.randrange(SCREEN_HEIGHT_IN_PIXELS - enemy_size_in_pixels)
            screen_position = Vector2(random_x, random_y)
            enemy = Enemy(screen_position, enemy_size_in_pixels, enemy_move_speed_in_pixels_per_second, enemy_color)
            self.Enemies.append(enemy)
        

# INITIALIZE PYGAME.
pygame.init()

# CREATE THE GAME SCREEN.
SCREEN_WIDTH_IN_PIXELS = 600
SCREEN_HEIGHT_IN_PIXELS = 400
SCREEN_BOUNDARIES_IN_PIXELS = pygame.Rect(0, 0, SCREEN_WIDTH_IN_PIXELS, SCREEN_HEIGHT_IN_PIXELS)
screen = pygame.display.set_mode(
    (SCREEN_BOUNDARIES_IN_PIXELS.width, SCREEN_BOUNDARIES_IN_PIXELS.height))

# DEFINE THE LEVELS.
levels = [
    Level(
        background_color = pygame.Color(0, 0, 0),
        collectible_count = 4,
        collectible_size_in_pixels = 20,
        collectible_color = pygame.Color(0, 255, 0),
        enemy_count = 4,
        enemy_size_in_pixels = 20,
        enemy_move_speed_in_pixels_per_second = 30,
        enemy_color = pygame.Color(128, 128, 128)),
    Level(
        background_color = pygame.Color(32, 32, 32),
        collectible_count = 5,
        collectible_size_in_pixels = 20,
        collectible_color = pygame.Color(0, 0, 255),
        enemy_count = 5,
        enemy_size_in_pixels = 20,
        enemy_move_speed_in_pixels_per_second = 35,
        enemy_color = pygame.Color(255, 255, 0)),
    Level(
        background_color = pygame.Color(64, 64, 64),
        collectible_count = 6,
        collectible_size_in_pixels = 20,
        collectible_color = pygame.Color(255, 0, 0),
        enemy_count = 6,
        enemy_size_in_pixels = 20,
        enemy_move_speed_in_pixels_per_second = 40,
        enemy_color = pygame.Color(0, 255, 255)),
]
current_level_index = 0

# DEFINE THE PLAYER.
player = Player(Vector2(200, 200))

# LOAD A FONT.
FONT_HEIGHT_IN_PIXELS = 16
font_filename = pygame.font.get_default_font()
font = pygame.font.Font(font_filename, FONT_HEIGHT_IN_PIXELS)

time_since_player_last_hit_in_seconds = 0

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
    MAX_FRAMES_PER_SECOND = 60
    time_since_last_update_in_ms = clock.tick(MAX_FRAMES_PER_SECOND)
    MILLISECONDS_PER_SECOND = 1000
    time_since_last_update_in_seconds = (
        time_since_last_update_in_ms / MILLISECONDS_PER_SECOND)
    
    time_since_player_last_hit_in_seconds += time_since_last_update_in_seconds

    # MOVE TO THE NEXT LEVEL IF THE CURRENT LEVEL HAS NO MORE COLLECTIBLES.
    current_level = levels[current_level_index]
    level_completed = (len(current_level.Collectibles) <= 0)
    if level_completed:
        current_level_index += 1
        if current_level_index >= len(levels):
            # GENERATE A RANDOM NEW LEVEL.
            new_level = Level(
                background_color = pygame.Color(random.randrange(255), random.randrange(255), random.randrange(255)),
                collectible_count = current_level.CollectibleCount + 1,
                collectible_size_in_pixels = random.randrange(10, 40),
                collectible_color = pygame.Color(random.randrange(255), random.randrange(255), random.randrange(255)),
                enemy_count = current_level.EnemyCount + 1,
                enemy_size_in_pixels = random.randrange(10, 40),
                enemy_move_speed_in_pixels_per_second = current_level.EnemyMoveSpeedInPixelsPerSecond * 1.1,
                enemy_color = pygame.Color(random.randrange(255), random.randrange(255), random.randrange(255)))
            levels.append(new_level)
            current_level = new_level
    ## @todo Player death!

    # MOVE THE PLAYER BASED ON KEYBOARD INPUT.
    PLAYER_MOVEMENT_AMOUNT_IN_PIXELS_PER_SECOND = 60
    player_movement_amount_in_pixels = PLAYER_MOVEMENT_AMOUNT_IN_PIXELS_PER_SECOND * time_since_last_update_in_seconds
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        player.ScreenPosition.X -= player_movement_amount_in_pixels
    if pressed_keys[pygame.K_RIGHT]:
        player.ScreenPosition.X += player_movement_amount_in_pixels
    if pressed_keys[pygame.K_UP]:
        player.ScreenPosition.Y -= player_movement_amount_in_pixels
    if pressed_keys[pygame.K_DOWN]:
        player.ScreenPosition.Y += player_movement_amount_in_pixels

    # POSITION THE PLAYER AT THE MOUSE POSITION (BOUNDED BY THE SCREEN).
    mouse_x, mouse_y = pygame.mouse.get_pos()
    max_player_x = SCREEN_WIDTH_IN_PIXELS - player.SizeInPixels
    if mouse_x > max_player_x:
        mouse_x = max_player_x
    max_player_y = SCREEN_HEIGHT_IN_PIXELS - player.SizeInPixels
    if mouse_y > max_player_y:
        mouse_y = max_player_y
    player.ScreenPosition = Vector2(mouse_x, mouse_y)

    player_rectangle = pygame.Rect(
        player.ScreenPosition.X,
        player.ScreenPosition.Y,
        player.SizeInPixels,
        player.SizeInPixels)

    # MOVE THE ENEMIES.
    for enemy in current_level.Enemies:
        enemy_movement_amount_in_pixels = enemy.MoveSpeedInPixelsPerSecond * time_since_last_update_in_seconds
        enemy_movement_vector = Vector2.Scale(enemy_movement_amount_in_pixels, enemy.MoveDirection)
        enemy.ScreenPosition = Vector2.Add(enemy.ScreenPosition, enemy_movement_vector)

        enemy_rectangle = pygame.Rect(
            enemy.ScreenPosition.X,
            enemy.ScreenPosition.Y,
            enemy.SizeInPixels,
            enemy.SizeInPixels)
        #enemy_on_screen = SCREEN_BOUNDARIES_IN_PIXELS.contains(enemy_rectangle)
        #if not enemy_on_screen:
        enemy_hit_left_or_right_side = (enemy.ScreenPosition.X < 0) or (enemy.ScreenPosition.X > SCREEN_WIDTH_IN_PIXELS - enemy.SizeInPixels)
        if enemy_hit_left_or_right_side:
            enemy.MoveDirection.X *= -1
        enemy_hit_top_or_bottom_side = (enemy.ScreenPosition.Y < 0) or (enemy.ScreenPosition.Y > SCREEN_HEIGHT_IN_PIXELS - enemy.SizeInPixels)
        if enemy_hit_top_or_bottom_side:
            enemy.MoveDirection.Y *= -1

    # CHECK FOR PLAYER COLLISIONS WITH COLLECTIBLES.
    for collectible in current_level.Collectibles:
        collectible_rectangle = pygame.Rect(
            collectible.ScreenPosition.X,
            collectible.ScreenPosition.Y,
            collectible.SizeInPixels,
            collectible.SizeInPixels)
        player_touched_collectible = player_rectangle.colliderect(collectible_rectangle)
        if player_touched_collectible:
            player.Score += 1
            current_level.Collectibles.remove(collectible)

    # CHECK FOR PLAYER COLLISIONS WITH ENEMIES.
    for enemy in current_level.Enemies:
        enemy_rectangle = pygame.Rect(
            enemy.ScreenPosition.X,
            enemy.ScreenPosition.Y,
            enemy.SizeInPixels,
            enemy.SizeInPixels)
        player_touched_enemy = player_rectangle.colliderect(enemy_rectangle)
        if player_touched_enemy:
            if time_since_player_last_hit_in_seconds > 1:
                player.Lives -= 1
                time_since_player_last_hit_in_seconds = 0

    # CLEAR THE SCREEN FOR THE NEW FRAME.
    screen.fill(current_level.BackgroundColor)

    # DRAW THE CURRENT LEVEL'S COLLECTIBLES.
    for collectible in current_level.Collectibles:
        collectible_rectangle = pygame.Rect(
            collectible.ScreenPosition.X,
            collectible.ScreenPosition.Y,
            collectible.SizeInPixels,
            collectible.SizeInPixels)
        pygame.draw.rect(screen, collectible.Color, collectible_rectangle)

    # DRAW THE CURRENT LEVEL'S ENEMIES.
    for enemy in current_level.Enemies:
        enemy_rectangle = pygame.Rect(
            enemy.ScreenPosition.X,
            enemy.ScreenPosition.Y,
            enemy.SizeInPixels,
            enemy.SizeInPixels)
        pygame.draw.rect(screen, enemy.Color, enemy_rectangle)

    # DRAW THE PLAYER.
    pygame.draw.rect(screen, player.Color, player_rectangle)

    # DRAW THE SCORE.
    NO_ANTI_ALIASING = False
    FONT_COLOR = pygame.Color(255, 255, 255)
    score_surface = font.render(
        "Score: " + str(player.Score),
        NO_ANTI_ALIASING,
        FONT_COLOR)
    SCORE_LEFT_TOP_SCREEN_POSITION = (
        SCREEN_BOUNDARIES_IN_PIXELS.left + 8,
        SCREEN_BOUNDARIES_IN_PIXELS.top + 8)
    screen.blit(
        score_surface,
        SCORE_LEFT_TOP_SCREEN_POSITION)

    # DRAW THE LIVES.
    lives_surface = font.render(
        "Lives: " + str(player.Lives),
        NO_ANTI_ALIASING,
        FONT_COLOR)
    LIVES_LEFT_TOP_SCREEN_POSITION = (
        SCREEN_BOUNDARIES_IN_PIXELS.right - 96,
        SCREEN_BOUNDARIES_IN_PIXELS.top + 8)
    screen.blit(
        lives_surface,
        LIVES_LEFT_TOP_SCREEN_POSITION)

    # DISPLAY THE UPDATED FRAME.
    pygame.display.update()
