import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000
        for thing in updatable:
            thing.update(dt)
        # player.update(dt)

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        # player.draw(screen)


if __name__ == "__main__":
    main()
