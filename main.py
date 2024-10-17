import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.hasCollided(player):
                sys.exit("Game over!")

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.hasCollided(bullet):
                    asteroid.kill()
                    bullet.kill()

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)


if __name__ == "__main__":
    main()
