import pygame
import circleshape


class Asteroid(circleshape.CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen,
                                  "white", self.position, self.radius, 2)

    def udpate(self, dt):
        return self.velocity * dt
