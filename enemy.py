import pygame
from random import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, *args):
        super().__init__(*args)
        self.image = load_image('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = randrange(-1, 2, 2)

    def update(self, *args):
        self.rect.x += 200 / FPS * self.direction
        if self.rect.x < 0 or self.rect.x > width - self.image.get_width():
            self.direction *= -1
            self.image = pygame.transform.flip(self.image, True, False)


def load_image(filename):
    return pygame.image.load(filename).convert_alpha()


pygame.init()
size = width, height = 500, 500

screen = pygame.display.set_mode(size)
FPS = 30
clock = pygame.time.Clock()
running = True
all_sprites = pygame.sprite.Group()

for i in range(2):
    sprite = Enemy(randint(0, 400), randint(10, 100))
    all_sprites.add(sprite)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill((49, 51, 53))
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
