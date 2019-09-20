# Drawing Text

- [pygame.font](https://www.pygame.org/docs/ref/font.html)

We've previously been printing text to the standard Python output window
using the `print()` function.  However, it would be better to be able to
draw text within our game window to make it more obvious to players.

To draw text using pygame, we need to use the [font module](https://www.pygame.org/docs/ref/font.html)
provided by pygame.  A "font" defines what characters in text will look like when drawn to the screen.
While the `font` module can be used to load other font files, we'll just use the default font in pygame
for now.  Somewhere near the top of our program, we'd need to get the filename of the default font
and then create a font at a particular size:

```
FONT_HEIGHT_IN_PIXELS = 16
font_filename = pygame.font.get_default_font()
font = pygame.font.Font(font_filename, FONT_HEIGHT_IN_PIXELS)
```

Now, drawing text with a font is a little complicated, involving multiple steps.
First, we need to draw our text in a particular color to a new drawing surface
(anti-aliasing is an advanced topic we won't cover now):
```
NO_ANTI_ALIASING = False
FONT_COLOR = pygame.Color(255, 255, 255)
text_surface = font.render("Some text", NO_ANTI_ALIASING, FONT_COLOR)
```

Next, we need to copy the text that has been drawn (rendered) to this other
drawing surface to our main game screen.  We'll need to define an (x, y)
position where we want it drawn.  And this copying is down using what
is known as [blitting](https://en.wikipedia.org/wiki/Bit_blit) using the
[pygame.Surface.blit() function](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit).
The example below draws text right in the top-left corner of the screen:
```
TEXT_LEFT_X_TOP_Y_SCREEN_POSITION = (0, 0)
screen.blit(text_surface, TEXT_LEFT_X_TOP_Y_SCREEN_POSITION)
```

So now if we want to draw the player's score or number of lives on screen,
we'd need to repeat the above twice but change a few things:
- Change the text we're passing to `font.render()` to be a string holding the score/lives
    (basically the same string we were previously passing to `print()`).
- Change the position in which we draw text to our screen with the `screen.blit()` call
    so that the score and lives strings are drawn in separate places on the screen
    (rather than on top of each other).

Alternatively, you could combine the score and lives text into a single string
and draw just that single string.
