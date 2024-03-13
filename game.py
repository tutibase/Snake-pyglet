from random import randint
from constants import *
import snake


class Food:
    def __init__(self, batch, tail, head):
        while True:
            self.x = randint(0, (window.width // cell_size) - 1) * cell_size
            self.y = randint(0, (window.width // cell_size) - 1) * cell_size
            if not ((self.x, self.y) in tail.coordinates or (self.x, self.y) == (head.x, head.y)):
                break

        self.square = pyglet.shapes.Rectangle(x=self.x, y=self.y, width=square_size,
                                              height=square_size, color=(255, 255, 0), batch=batch)


class Game:
    def __init__(self):
        self.batch = pyglet.graphics.Batch()

        self.over = False
        self.label = ''

        self.head = snake.SnakeHead(self.batch)
        self.tail = snake.SnakeTail()
        self.food = Food(self.batch, self.tail, self.head)

    def condition_check(self):
        if ((self.head.x, self.head.y) in self.tail.coordinates) or \
                (self.head.x < 0 or self.head.x > window.width - cell_size or
                 self.head.y < 0 or self.head.y > window.height - cell_size):
            self.over = True
            self.label = pyglet.text.Label('Press SPACE to restart',
                                           font_name='Times New Roman',
                                           font_size=36,
                                           x=window.width // 2, y=window.height // 2,
                                           anchor_x='center', anchor_y='center', batch=self.batch)

    def update(self, dt):
        if self.over:
            return

        self.head.x += self.head.dx
        self.head.y += self.head.dy
        self.head.square = pyglet.shapes.Rectangle(x=self.head.x, y=self.head.y, width=square_size,
                                                   height=square_size, color=(0, 255, 0), batch=self.batch)

        self.condition_check()

        self.tail.coordinates.append((self.head.x, self.head.y))

        self.tail.squares = []
        for coordinates in self.tail.coordinates:
            self.tail.squares.append(pyglet.shapes.Rectangle(x=coordinates[0], y=coordinates[1], width=square_size,
                                                             height=square_size, color=(0, 128, 0), batch=self.batch))

        if self.head.x == self.food.x and self.head.y == self.food.y:
            self.food.__init__(self.batch, self.tail, self.head)
        else:
            self.tail.coordinates.pop(0)
