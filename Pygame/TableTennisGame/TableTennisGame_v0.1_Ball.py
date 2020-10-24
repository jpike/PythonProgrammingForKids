## Version 0.1 of a video game version of "table tennis"
## (https://en.wikipedia.org/wiki/Table_tennis).
## This version builds upon the previous version by adding a moving ball.

# IMPORT MODULES.
import pygame
import random
import sys

# INITIALIZE PYGAME.
pygame.init()

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

## The ball in the game.
class Ball(object):
    ## Generates a random screen velocity for the ball.
    ## @return A random Vector2 velocity for the ball.
    def RandomVelocity():
        MAX_VELOCITY_COMPONENT_IN_PIXELS = 128
        x_screen_velocity = random.randrange(-MAX_VELOCITY_COMPONENT_IN_PIXELS, MAX_VELOCITY_COMPONENT_IN_PIXELS)
        y_screen_velocity = random.randrange(-MAX_VELOCITY_COMPONENT_IN_PIXELS, MAX_VELOCITY_COMPONENT_IN_PIXELS)
        return Vector2(x_screen_velocity, y_screen_velocity)
    
    ## Initializes the ball.
    ## @param[in]   screen_position - The Vector2 position of the ball's center on screen (in pixels).
    def __init__(self, screen_position):
        ## The Vector2 screen position of the ball.
        self.ScreenPosition = screen_position
        ## The radius of the ball (in pixels)
        self.RadiusInPixels = 8
        ## The Vector2 screen velocity of the ball.
        self.VelocityInPixelsPerSecond = Ball.RandomVelocity()
        ## The color of the ball.
        self.Color = pygame.Color(255, 255, 255)

    ## Moves the ball based on elapsed time.
    ## @param[in]   time_in_seconds_to_move - The time (in seconds) for which to move the ball.
    def Move(self, time_in_seconds_to_move):
        # MOVE THE BALL BASED ON THE TIME AND VELOCITY.
        screen_vector_to_move = Vector2.Scale(time_in_seconds_to_move, self.VelocityInPixelsPerSecond)
        self.ScreenPosition = Vector2.Add(self.ScreenPosition, screen_vector_to_move)

# CREATE THE GAME SCREEN.
SCREEN_BOUNDARIES_IN_PIXELS = pygame.Rect(0, 0, 600, 400)
screen = pygame.display.set_mode((SCREEN_BOUNDARIES_IN_PIXELS.width, SCREEN_BOUNDARIES_IN_PIXELS.height))
pygame.display.set_caption("Table Tennis Game")

# INITIALIZE THE MAIN GAME OBJECTS.
INITIAL_BALL_SCREEN_POSITION = Vector2(SCREEN_BOUNDARIES_IN_PIXELS.centerx, SCREEN_BOUNDARIES_IN_PIXELS.centery)
ball = Ball(INITIAL_BALL_SCREEN_POSITION)

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

    # MOVE THE BALL.
    ball.Move(time_elapsed_since_last_frame_in_seconds)

    # CHECK FOR SCREEN COLLISIONS WITH THE BALL.
    ball_outside_of_screen_left_boundary = (ball.ScreenPosition.X < SCREEN_BOUNDARIES_IN_PIXELS.left)
    ball_outside_of_screen_right_boundary = (ball.ScreenPosition.X > SCREEN_BOUNDARIES_IN_PIXELS.right)
    ball_outside_of_screen_top_boundary = (ball.ScreenPosition.Y < SCREEN_BOUNDARIES_IN_PIXELS.top)
    ball_outside_of_screen_bottom_boundary = (ball.ScreenPosition.Y > SCREEN_BOUNDARIES_IN_PIXELS.bottom)
    if ball_outside_of_screen_left_boundary:
        # RESET THE BALL.
        ball = Ball(INITIAL_BALL_SCREEN_POSITION)
    elif ball_outside_of_screen_right_boundary:
        # RESET THE BALL.
        ball = Ball(INITIAL_BALL_SCREEN_POSITION)
    elif ball_outside_of_screen_top_boundary:
        # REFLECT THE BALL'S VELOCITY ACROSS THE Y AXIS.
        ball.VelocityInPixelsPerSecond.Y *= -1
    elif ball_outside_of_screen_bottom_boundary:
        # REFLECT THE BALL'S VELOCITY ACROSS THE Y AXIS.
        ball.VelocityInPixelsPerSecond.Y *= -1

    # CLEAR THE SCREEN FOR THE NEW FRAME.
    BACKGROUND_COLOR = pygame.Color(0, 0, 0)
    screen.fill(BACKGROUND_COLOR)

    # DRAW THE BALL.
    pygame.draw.circle(
        screen,
        ball.Color,
        (int(ball.ScreenPosition.X), int(ball.ScreenPosition.Y)),
        ball.RadiusInPixels)

    # DISPLAY THE UPDATED FRAME.
    pygame.display.update()
