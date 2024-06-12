from hashlib import md5

import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particle Automaton")

# Set up the game matrix
matrix_width, matrix_height = 40, 30
matrix = np.zeros((matrix_height, matrix_width), dtype=int)

# setup objects

class Particle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = None
        self.color = None
        self.id = int(md5.hexdigest(), 16)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 1, 1))

    def move_up(self, movement):
        self.x = self.x + movement
    
    def move_down(self, movement):
        self.x = self.x - movement

    def move_left(self, movement):
        self.y = self.y - movement

    def move_right(self, movement):
        self.y = self.y + movement

    def check_collision(self, particles):


class A(Particle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'A'
        self.color = (255, 0, 0)

class B(Particle):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'B'
        self.color = (200, 200, 0)


attraction_rules = np.array(
    [
        # A, B
        [1, 1], # A
        [-1, 1],   # B
    ]
)
    
def bulk_create_random_particles(particle_type, number):
    for i in range(number):
        x = np.random.randint(0, matrix_width)
        y = np.random.randint(0, matrix_height)
        particle = particle_type(x, y)
        yield particle

# Creating particles
a_particles = {
    part.id: part for part in bulk_create_random_particles(A, 100)
}
b_particles = {
    part.id: part for part in bulk_create_random_particles(B, 100)
}

particles = {**a_particles, **b_particles}


# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Render the game
    screen.fill((0, 0, 0))  # Fill the screen with black color

    # Draw objects based on the matrix particles using the .draw() method
    
    pygame.display.flip()  # Update the display

# Quit the game
pygame.quit()