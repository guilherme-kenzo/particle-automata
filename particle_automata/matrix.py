import pygame
import numpy as np
from .particle import Particle
from .settings import attraction_rules
from joblib import Parallel, delayed


class GameMatrix:
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.matrix = np.zeros((self.height, self.width), dtype=np.int64)
        self.particles = {}

    def slice_square_around(self, x: int, y: int, radius: int):
        left_limit = max(0, min(x - radius, self.width))
        right_limit = min(self.matrix.shape[1], x + radius + 1)
        down_limit = max(0, y - radius)
        up_limit = min(self.matrix.shape[0], y + radius + 1)
        return self.matrix[down_limit:up_limit, left_limit:right_limit]

    def add_particle(self, particle: Particle):
        self.particles[particle.id] = particle
        self.matrix[particle.y, particle.x] = particle.id

    def update_particle_position(self, particle: Particle, new_x: int, new_y: int):
        new_x = min(max(new_x, 0), self.width-1)
        new_y = min(max(new_y, 0), self.height-1)
        self.matrix[particle.y, particle.x] = 0
        self.matrix[new_y, new_x] = particle.id
        particle.move(new_x, new_y)

    def remove_particle(self, particle: Particle):
        del self.particles[(particle.x, particle.y)]
        self.matrix[particle.y, particle.x] = 0


    def compute_attractions(self, particle: Particle):
        particles_around = self.slice_square_around(particle.x, particle.y, 1)
        force_acc = np.array([0.0, 0.0])

        for dy in range(particles_around.shape[0]):
            for dx in range(particles_around.shape[1]):
                if dy == 1 and dx == 1:
                    continue  # Skip the particle itself
                other_particle_id = particles_around[dy, dx]
                if other_particle_id == 0:
                    continue
                other_particle = self.particles[other_particle_id]
                rule = attraction_rules[particle.type][other_particle.type]
                offset = np.array([dy - 1, dx - 1])  # Calculate offset
                force_acc += rule * offset


        if np.all(force_acc == 0):
            # If there is no force, move randomly
            force_acc = np.random.randint(-1, 2, size=2)

        new_x, new_y = particle.x + int(force_acc[1]), particle.y + int(force_acc[0])
        self.update_particle_position(particle, new_x, new_y)

    def compute_all_attractions(self):
        for particle in self.particles.values():
            self.compute_attractions(particle)

    def draw_particles(self, screen: pygame.Surface):
        for particle in self.particles.values():
            particle.draw(screen)
