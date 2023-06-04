import pygame
import random

IMG_OBSTACLE = './assets/asteroid.png'
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50


class Obstacle(pygame.sprite.Sprite):    

    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, OBSTACLE_SPEED):
        super(Obstacle, self).__init__()
        self.ww = WINDOW_WIDTH
        self.wh = WINDOW_HEIGHT
        
        self.image = pygame.image.load(IMG_OBSTACLE).convert()
        self.image = pygame.transform.scale(self.image,
                            (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WINDOW_WIDTH-OBSTACLE_WIDTH)
        self.rect.y = random.randrange(-2000, -OBSTACLE_HEIGHT)
        
        self.speed = OBSTACLE_SPEED

    def update(self):
        self.rect.y += self.speed