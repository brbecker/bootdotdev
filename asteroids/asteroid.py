import random

import pygame

from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(*self.position, new_radius)
        a2 = Asteroid(*self.position, new_radius)

        angle = random.uniform(20, 50)
        a1.velocity = self.velocity.rotate(angle) * 1.2
        a2.velocity = self.velocity.rotate(-angle) * 1.2
