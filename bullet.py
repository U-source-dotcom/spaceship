import pygame

COL_YELLOW = (255, 255, 0)
BULLET_WIDTH = 5
BULLET_HEIGHT = 10


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        self.image.fill(COL_YELLOW)
        
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()