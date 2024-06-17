import pygame
from hashlib import md5
import numpy as np

ids = []

class Particle:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.type = None
        self.color = None
        self._id = None
        self._has_changed_this_loop = False
        self._acc_forces = []

    @property
    def id(self):
        if self._id:
            return self._id
        while self._id is None:
            _id = np.random.randint(0, 100000)
            if _id not in ids:
                ids.append(_id)
                self._id = _id
                return self._id

    def move(self, x: int=None, y: int=None):
        if x is None and y is None:
            raise ValueError("You must provide x or y to move the particle")
        if x:
            self.x = x
        if y:
            self.y = y
        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 1, 1))

    def move_up(self, movement):
        self.move(y=self.y + movement)
    
    def move_down(self, movement):
        self.move(y=movement - self.y)

    def move_left(self, movement):
        self.move(x=self.x - movement)

    def move_right(self, movement):
        self.move(x=self.x + movement)


class A(Particle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'A'
        self.color = (255, 255, 255)

class B(Particle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'B'
        self.color = (200, 0, 0)

class C(Particle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'C'
        self.color = (0, 200, 0)

