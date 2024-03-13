import game
import pyglet
from constants import game_speed, window, cell_size
from pyglet.window import key

game = game.Game()


@window.event
def on_draw():
    window.clear()
    game.batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    if game.over:
        if symbol == key.SPACE:
            game.__init__()

    if symbol == key.A:
        if game.head.dx == 0:
            game.head.dx = -cell_size  # Left is the negative x direction.
            game.head.dy = 0  # Stop moving up/down.
    elif symbol == key.D:
        if game.head.dx == 0:
            game.head.dx = cell_size  # Right is the positive x direction.
            game.head.dy = 0  # Stop moving up/down.
    elif symbol == key.W:
        if game.head.dy == 0:
            game.head.dx = 0  # Up is the positive y direction.
            game.head.dy = cell_size  # Stop moving left/right.
    elif symbol == key.S:
        if game.head.dy == 0:
            game.head.dx = 0  # Down is the negative y direction.
            game.head.dy = -cell_size  # Stop moving left/right.


# Set how often the update function is called.
pyglet.clock.schedule_interval(game.update, 1 / game_speed)

pyglet.app.run()
