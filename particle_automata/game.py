
from hashlib import md5

import pygame
import numpy as np

from .matrix import GameMatrix
from .particle import Particle, A, B, C
from .settings import width, height

def bulk_create_random_particles(particle_type, number):
    for i in range(number):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        particle = particle_type(x, y)
        yield particle


def start_game(): 
    loop = 0
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Particle Automaton")
    game_matrix = GameMatrix(width=width, height=height)

    # Creating particles
    a_particles = {
        part.id: part for part in bulk_create_random_particles(A, 400)
    }
    b_particles = {
        part.id: part for part in bulk_create_random_particles(B, 1000)
    }
    c_particles = {
        part.id: part for part in bulk_create_random_particles(C, 1000)
    }


    particles = {**a_particles, **b_particles, **c_particles}
    for particle in particles.values():
        game_matrix.add_particle(particle)

    # Game loop
    running = True
    while running:
        print("loop number:", loop)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game logic
        game_matrix.compute_all_attractions()        

        # Render the game
        screen.fill((0, 0, 0))  # Fill the screen with black color
        # Draw objects based on the matrix particles using the .draw() method
        game_matrix.draw_particles(screen)
        pygame.display.flip()  # Update the display
        loop += 1
    # Quit the game
    pygame.quit()




