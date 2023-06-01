import pygame
import time

from spaceship import Spaceship

COL_BLACK = (0, 0, 0)
COL_WHITE = (255, 255, 255)


class Game(object):
    bullets = pygame.sprite.Group()

    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.w = WINDOW_WIDTH
        self.h = WINDOW_HEIGHT

        self.is_game_over = False
        self.waitSecs = 2

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

    def shoot_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bullets.add(self.spaceship.shoot())

    def update_state(self):
        self.display.fill(COL_BLACK)
        
        self.bullets.update()
        
        keys = pygame.key.get_pressed()
        self.spaceship.update(keys)

    def disp_frame(self):
        self.bullets.draw(self.display)
        self.display.blit(self.spaceship.image, self.spaceship.rect)
        pygame.display.update()

    def disp_game_over(self):
        self.render_text('game over :(', 28, self.w / 2, self.h / 2)
        time.sleep(self.waitSecs)

    def render_text(self, messageText, font_size, x, y):
        textFont = pygame.font.Font('freesansbold.ttf', font_size)
        textSurface = textFont.render(messageText, True, COL_WHITE)
        textRect = textSurface.get_rect()
        textRect.center = ((x, y))

        self.display.blit(textSurface, textRect)
        pygame.display.update()

    def reset_state(self):
        self.bullets.empty()
        self.spaceship.reset_pos()

    def run(self):
        events = pygame.event.get()
        game_state = self.process_events(events)

        self.shoot_events(events)
        self.update_state()
        self.disp_frame()

        if self.is_game_over:
            self.disp_game_over()
            self.reset_state()

        return game_state
