import sys
import pygame as pg
import time

from player import Player
from bullet import Bullet
from enemy import Enemy


def main():
    pg.init()
    size = W, H = 1000, 700  # list(map(int, input().split()))
    window = pg.display.set_mode(size)
    screen = pg.display.set_mode(size)
    screen.blit(pg.transform.scale(pg.image.load('images/bg.png'), (1000, 750)), (0, 0))
    FPS = 30
    clock = pg.time.Clock()

    player = Player(screen)

    running = True
    moving = False

    move = 0
    bullet = None
    bullets = []

    ##################################
    all_sprites = pg.sprite.Group()

    all_direction = 1

    enemies = []

    for i in range(8):
        for j in range(9):
            sprite = Enemy(j * 75 + 1, i * 31)
            all_sprites.add(sprite)
            enemies.append(sprite)
    timer = time.time()
    a = 1
    ##################################
    bullet = None
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                moving = True
                if event.key == pg.K_LEFT:
                    move = -10
                if event.key == pg.K_RIGHT:
                    move = 10
                if event.key == pg.K_SPACE:
                    if bullet is None:
                        bullet = Bullet(screen, player)
                    # bullets.append(bullet)
            if event.type == pg.KEYUP:
                move = 0
                moving = False

        screen.blit(pg.transform.scale(pg.image.load('images/bg.png'), (1000, 750)), (0, 0))

        if bullet is not None:
            bullet.update()
            for enm in enemies:
                if bullet.rect.colliderect(enm.rect):
                    bullet = None
                    enemies.remove(enm)
                    all_sprites.remove(enm)
                    break
        if moving:
            player.update(move=move)
        else:
            player.update()

        if any([i.rect.y > player.rect.y for i in enemies]):
            print('GAME_OVER')
            break

        ########################################
        coords = [0 < i.rect.x < W - i.image.get_width() for i in enemies]

        if not all(coords):
            all_direction *= -1

        if (int(time.time() - timer) + 1) % (5 * a) == 0:
            a += 1
            for i in enemies:
                i.down()
        all_sprites.update(all_direction)
        all_sprites.draw(screen)
        #########################################

        # remove_bullets(bullets)
        pg.display.flip()
        clock.tick(FPS)


"""def remove_bullets(bullets):
    for i in bullets.copy():
        if i.rect.bottom <= 0:
            bullets.remove(i)"""


"""def create_enemies(screen, ino):
    # Creating enemies (will need Alien class)
    pass"""


if __name__ == '__main__':
    main()
