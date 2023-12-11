import pygame as pg


def main():
    pg.init()
    size = W, H = 1200, 700  # list(map(int, input().split()))
    window = pg.display.set_mode(size)
    screen = pg.display.set_mode(size)
    screen.fill('black')
    FPS = 20
    clock = pg.time.Clock()

    running = True

    while running:
        screen.fill('black')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
