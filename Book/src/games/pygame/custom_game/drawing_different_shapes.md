# Drawing Different Shapes

- [pygame.draw](https://www.pygame.org/docs/ref/draw.html)

We've covered drawing rectangles previously, but pygame has built-in functions for
drawing several other kinds of shapes.  Try experimenting with drawing different
shapes (circles, polygons, lines) for different parts of your game - the player,
collectible, enemies.  Make sure to practice using all of the functions in the
[pygame.draw module](https://www.pygame.org/docs/ref/draw.html) so that you
understand what they do and can see the differences.

Below are some examples:
```
# DRAW A POLYGON.
POLYGON_COLOR = pygame.Color(255, 255, 0)
POLYGON_POINTS = [(100, 100), (0, 200), (200, 200)]
pygame.draw.polygon(screen, POLYGON_COLOR, POLYGON_POINTS)

# DRAW A CIRCLE.
CIRCLE_COLOR = pygame.Color(0, 255, 255)
CIRCLE_CENTER_POSITION = (200, 200)
CIRCLE_RADIUS = 50
pygame.draw.circle(screen, CIRCLE_COLOR, CIRCLE_CENTER_POSITION, CIRCLE_RADIUS)

# DRAW A LINE.
LINE_COLOR = pygame.Color(255, 0, 255)
LINE_START_POSITION = (200, 200)
LINE_END_POSITION = (300, 300)
pygame.draw.line(screen, LINE_COLOR, LINE_START_POSITION, LINE_END_POSITION)
```
