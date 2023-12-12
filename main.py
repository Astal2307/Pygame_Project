import sys
import pygame as pg
from player import Player


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
            if event.type == pg.KEYUP:
                moving = False

        screen.fill('black')
        if moving:
            player.update(move=move)
        else:
            player.update()
        pg.display.flip()
        clock.tick(FPS)



if __name__ == '__main__':
    main()
