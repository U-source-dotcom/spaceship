import pygame
import time

from spaceship import Spaceship

COL_BLACK = (0, 0, 0)
COL_WHITE = (255, 255, 255)


class Game(object):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.w = WINDOW_WIDTH
        self.h = WINDOW_HEIGHT
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display.fill(COL_BLACK)
        self.spaceship = Spaceship(WINDOW_WIDTH, WINDOW_HEIGHT)

    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        return False

    def update_state(self):
        self.display.fill(COL_BLACK)
        
        keys = pygame.key.get_pressed()
        self.spaceship.update(keys)

    def disp_frame(self):
        self.display.blit(self.spaceship.image, self.spaceship.rect)
        pygame.display.update()

    def run(self):
        events = pygame.event.get()
        game_state = self.process_events(events)

        self.update_state()
        self.disp_frame()

        return game_state
