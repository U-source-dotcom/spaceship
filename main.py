import pygame

from game import Game

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800


def main():

    pygame.init()
    clock = pygame.time.Clock()

    game = Game(WINDOW_WIDTH, WINDOW_HEIGHT)

    exit_game = False
    while not exit_game:
        exit_game = game.run()
        clock.tick(60)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()