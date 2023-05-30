import pygame

IMG_AGENT = './assets/spaceship.png'
SPACESHIP_WIDTH = 40
SPACESHIP_HEIGHT = 60
SPACESHIP_SPEED = 7


class Spaceship(pygame.sprite.Sprite):

    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, col=(255, 255, 255)):
        super(Spaceship, self).__init__()
        self.ww = WINDOW_WIDTH
        self.wh = WINDOW_HEIGHT
        self.startx = WINDOW_WIDTH * .45
        self.starty = WINDOW_HEIGHT * .75
        self.image = pygame.image.load(IMG_AGENT).convert()
        self.image = pygame.transform.scale(
            self.image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.startx
        self.rect.y = self.starty

    def update(self, keys):
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -SPACESHIP_SPEED)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, SPACESHIP_SPEED)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-SPACESHIP_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(SPACESHIP_SPEED, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.ww:
            self.rect.right = self.ww
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.wh:
            self.rect.bottom = self.wh