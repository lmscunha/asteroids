import pygame
import circleshape
from constants import SHOT_RADIUS


class Shot(circleshape.CircleShape):
    containers = None

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        return pygame.draw.circle(screen,
                                  "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
