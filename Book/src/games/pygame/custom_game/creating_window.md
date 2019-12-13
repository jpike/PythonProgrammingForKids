# Creating a Basic Window

The first step to creating our game is to bring up a window that
will hold the game screen to which we will display our game.

- [Handout](https://docs.google.com/document/d/108-g5HurQSN0jg0w3xfmqPwJ_ZAgyxVSw2r5cX5g928/)
- [Video](https://www.youtube.com/watch?v=LStpWkVkzzc)
- [Code](https://github.com/jpike/PythonProgrammingForKids/blob/master/Pygame/Pygame1.0_BasicColoredWindow.py)

Key concepts:
- Importing modules
- Loops
- [pygame.display](https://www.pygame.org/docs/ref/display.html)
- [Pygame event processing](https://www.pygame.org/docs/ref/event.html)
- [Pygame colors](https://www.pygame.org/docs/ref/color.html)
- Other used functions:
    - [pygame.init()](https://www.pygame.org/docs/ref/pygame.html#pygame.init)
    - [pygame.quit()](https://www.pygame.org/docs/ref/pygame.html#pygame.quit)
    - [sys.exit()](https://docs.python.org/3/library/sys.html#sys.exit)

Display Surfaces
----------------
To draw graphics on our computer screen, we typically need to create a window with an internal drawing area or "screen".
[pygame.display.set_mode()](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode) is how we do this in Pygame.

This function returns what is known as a [Surface](https://www.pygame.org/docs/ref/surface.html) in Pygame.  You can think of
a Pygame `Surface` as a drawing surface similar to other things you could draw on in real life - a piece of paper, canvas for painting, etc.

Game Loops and Animation
------------------------
Our code so far has a `while` loop, which in game programming is sometimes referred to as a "game loop".
This loop will basically keep our game program running forever (at least until we explicitly exit the loop).

Having a loop like this is a critical concept in computer animation and games.  This is how we achieve the
illusion of movement and [animation](https://en.wikipedia.org/wiki/Animation).  To have animation, we need
to create and display a series of drawings/images (frames) at a fast enough rate.  That is one of the main goals
of our game loop - to produce and display and updated frame each iteration of the loop (each time through the loop).

Double Buffering
----------------
If our display [Surface](https://www.pygame.org/docs/ref/surface.html) that we drew to was exactly what
our computer monitors were directly showing, then we could experience issues of seeing partially drawn
frames as our game draws individual pixels on the screen.  In other words, the user might see incomplete
images that would make it hard to see exactly what's going on in our game's "world".  This is because
even though our computers are pretty fast, it still takes some time to fill our entire screen with
color or draw a rectangle.

To overcome this problem, most computer graphics relies on the concept of "double buffering".
Rather than having a single "buffer" into which we draw our frames, there's actually a second buffer.
While our computer is displaying one buffer on screen, our drawing commands actually manipulate
the other buffer.  When we're done drawing, we then tell the computer to display our final image.
This can be done either by actually switching the buffers or by quickly copying the full image
from one buffer in the computer's memory to the other buffer.

You can think of this as having two pieces of paper - while we're showing one to a person,
we're drawing to another "hidden" piece of paper in the back.  When we're done, we switch
which piece of paper we're displaying to another person.

[pygame.display.update()](https://www.pygame.org/docs/ref/display.html#pygame.display.update) is how
we do this in Pygame.  It's important to do this at the end of each iteration of our game loop - otherwise,
our game screen won't update.

For more on double buffering, see:
- <https://en.wikipedia.org/wiki/Multiple_buffering#Double_buffering_in_computer_graphics>
- <http://gameprogrammingpatterns.com/double-buffer.html>

Event Processing
----------------
In a lot of GUI (graphical user interface) programming environments (such as our's with Pygame
where we're displaying a window), we typically have to handle events that our computer's operating
system sends us.  This ensures that our program can behave correctly when asked to close, resize
our window, etc.  This is also how we can detect when the user interacts with our computer program
by pressing a key on a keyboard or mouse button on a mouse.

In Pygame, we get events for our program using the [pygame.event](https://www.pygame.org/docs/ref/event.html) module.
We can get these events and respond to them with a for loop.  It's important to process these events
each iteration of our game loop in order to keep our program responsive.

Colors
------
Colors in Pygame are represented as instances of the [pygame.Color](https://www.pygame.org/docs/ref/color.html) class.
Colors have red, green, and blue components (often referred to as 'r', 'g', and 'b' for short) that can basically
be combined to form just about any color.

(There's also an alpha component, but we'll get to that later).

Each component of a color represents the "intensity" (how strong) that component is in the overall color.
Color components in Pygame have a range of 0 (no intensity) to 255 (max intensity).

For more on RGB colors, see <https://en.wikipedia.org/wiki/RGB_color_model>.
