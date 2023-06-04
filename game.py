import pygame
import time

from obstacle import Obstacle
from spaceship import Spaceship

COL_BLACK = (0, 0, 0)
COL_WHITE = (255, 255, 255)

OBSTACLE_SPEED = 7


class Game(object):
    bullets = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.w = WINDOW_WIDTH
        self.h = WINDOW_HEIGHT

        self.score = 0
        self.is_game_over = False
        self.waitSecs = 2
        self.obstacle_speed = OBSTACLE_SPEED

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

        if self.obstacles:
            for obstacle in self.obstacles:
                obstacle.update()
                if obstacle.rect.top > self.h:
                    obstacle.kill()
                    self.score += 1
                    self.obstacle_speed += .05
        
        keys = pygame.key.get_pressed()
        self.spaceship.update(keys)

    def check_state(self):
        if pygame.sprite.spritecollide(self.spaceship, self.obstacles, False):
            return True

    def obstacle_check_state(self):
        if pygame.sprite.groupcollide(self.obstacles, self.bullets, True, True):
            self.score += 1

    def disp_frame(self):
        self.bullets.draw(self.display)
        self.obstacles.draw(self.display)
        self.display.blit(self.spaceship.image, self.spaceship.rect)
        self.disp_score()
        pygame.display.update()

    def disp_score(self):
        score_txt = 'avoided asteroids: ' + str(self.score)
        self.render_text(score_txt, 18, 0.8 * self.w, 0.1 * self.h)

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
        self.score = 0
        self.obstacle_speed = OBSTACLE_SPEED
        self.obstacles.empty()
        self.bullets.empty()
        self.spaceship.reset_pos()

    def run(self):
        self.is_game_over = self.check_state()
        events = pygame.event.get()
        game_state = self.process_events(events)

        if self.obstacles.sprites().__len__() < 8:
            obstacle = Obstacle(self.w, self.h, self.obstacle_speed)
            self.obstacles.add(obstacle)

        self.shoot_events(events)
        self.update_state()
        self.obstacle_check_state()
        self.disp_frame()

        if self.is_game_over:
            self.disp_game_over()
            self.reset_state()

        return game_state
