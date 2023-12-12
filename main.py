import sys
import pygame as pg
from player import Player
from bullet import Bullet


def main():
    pg.init()
    size = W, H = 1000, 700  # list(map(int, input().split()))
    window = pg.display.set_mode(size)
    screen = pg.display.set_mode(size)
    screen.fill('black')
    FPS = 30
    clock = pg.time.Clock()

    player = Player(screen)

    running = True
    moving = False

    move = 0
    bullet = None
    bullets = []

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
                    bullet = Bullet(screen, player)
                    bullets.append(bullet)
            if event.type == pg.KEYUP:
                move = 0
                moving = False

        screen.fill('black')
        if bullets:
            for blt in bullets:
                blt.update()
        if moving:
            player.update(move=move)
        else:
            player.update()
        remove_bullets(bullets)
        pg.display.flip()
        clock.tick(FPS)


def remove_bullets(bullets):
    for i in bullets.copy():
        if i.rect.bottom <= 0:
            bullets.remove(i)


def create_enemies(screen, ino):
    """Creating enemies (will need Alien class)"""
    pass


if __name__ == '__main__':
    main()
