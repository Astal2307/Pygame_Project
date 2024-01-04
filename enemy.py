import pygame as pg
from random import *
import time


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, *args):
        super().__init__(*args)
        possible_colors = ['blue', 'green', 'red', 'yellow']
        self.file_name = 'images/' + choice(possible_colors) + '.png'
        self.image = pg.transform.scale((load_image(self.file_name)), (40, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.direction = 1

    def update(self, all_direction, *args):
        FPS = 30
        self.rect.x += 100 / FPS * all_direction
        """if self.rect.x < 0 or self.rect.x > width - self.image.get_width():
            self.direction *= -1
            self.image = pg.transform.flip(self.image, True, False)"""
        # pg.draw.rect(screen, 'white', self.rect, 1)

    def down(self):
        self.rect.y += 100


def load_image(filename):
    return pg.image.load(filename).convert_alpha()


"""pg.init()
size = width, height = 500, 500

screen = pg.display.set_mode(size)
FPS = 30
clock = pg.time.Clock()
running = True
all_sprites = pg.sprite.Group()

all_direction = 1

enemies = []

for i in range(5):
    for j in range(6):
        sprite = Enemy(j * 75 + 1, i * 31)
        all_sprites.add(sprite)
        enemies.append(sprite)

timer = time.time()
a = 1
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((49, 51, 53))

    coords = [0 < i.rect.x < width - i.image.get_width() for i in enemies]

    if not all(coords):
        all_direction *= -1

    if (int(time.time() - timer) + 1) % (30 * a) == 0:
        a += 1
        for i in enemies:
            i.down()
    all_sprites.update()
    all_sprites.draw(screen)
    clock.tick(FPS)
    pg.display.flip()

pg.quit()"""
