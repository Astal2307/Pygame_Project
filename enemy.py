import pygame as pg
from random import *
import time


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y, colors, scr, *args):
        super().__init__(*args)
        possible_colors = ['blue', 'green', 'red', 'yellow']
        if colors['blue'] >= 5:
            possible_colors.remove('blue')

        if colors['green'] >= 10:
            possible_colors.remove('green')

        self.screen = scr
        self.color = choice(possible_colors)
        self.file_name = 'images/' + self.color + '.png'
        self.image = pg.transform.scale((load_image(self.file_name)), (40, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bullet_rect = None
        # self.direction = 1

    def update(self, all_direction, *args):
        FPS = 30
        self.rect.x += 100 / FPS * all_direction
        """if self.rect.x < 0 or self.rect.x > width - self.image.get_width():
            self.direction *= -1
            self.image = pg.transform.flip(self.image, True, False)"""
        # pg.draw.rect(screen, 'white', self.rect, 1)

    def create_bullet(self):
        self.bullet_rect = pg.rect.Rect(self.rect.x + 21, self.rect.y + 24, 6, 10)

    def update_bullet(self):
        if self.bullet_rect is not None:
            pg.draw.rect(self.screen, 'white', self.bullet_rect)
            self.bullet_rect.y += 2

    def check_collide(self, player):
        if self.bullet_rect is not None:
            return self.bullet_rect.colliderect(player.rect)
        return False

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
