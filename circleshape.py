import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def udpate(self, dt):
        pass

    def hasCollided(self, target):
        distance = self.position.distance_to(target.position)
        totalRadius = self.radius + target.radius
        return totalRadius > distance
