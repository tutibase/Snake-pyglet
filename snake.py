import pyglet
from constants import square_size


class SnakeHead:
    def __init__(self, batch):
        self.x = 200
        self.y = 200
        self.dx = 0
        self.dy = 0
        self.square = pyglet.shapes.Rectangle(x=self.x, y=self.y, width=square_size,
                                              height=square_size, color=(0, 0, 0), batch=batch)


class SnakeTail:
    def __init__(self):
        self.coordinates = []
        self.squares = []
