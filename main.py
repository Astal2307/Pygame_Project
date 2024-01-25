import sys
import pygame as pg
import time
from random import *
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
    colors = {'blue': 0,
              'green': 0,
              'red': 0,
              'yellow': 0}
    for i in range(8):
        for j in range(9):
            sprite = Enemy(j * 75 + 1, i * 31, colors, screen)
            colors[sprite.color] += 1
            all_sprites.add(sprite)
            enemies.append(sprite)
    timer = time.time()
    a = 1
    b = 1
    iteration = 0
    ##################################
    explosion = pg.mixer.Sound('audio/boom.wav')
    shoot = pg.mixer.Sound('audio/shoot.wav')
    """it1 = pg.mixer.Sound('audio/1.wav')
    it2 = pg.mixer.Sound('audio/2.wav')
    it3 = pg.mixer.Sound('audio/3.wav')
    it4 = pg.mixer.Sound('audio/4.wav')"""
    bg = pg.mixer.Sound('audio/bg.mp3')
    bg.play()
    ###################################
    bullet = None

    value = {'red': 10,
             'yellow': 15,
             'green': 50,
             'blue': 100}
    score = 0

    font = pg.font.Font('ARCADECLASSIC.TTF', 30)
    rendered = font.render(f'SCORE   {score}', 1, pg.Color('green'))
    rect = rendered.get_rect()
    rect.x = 1000 - rect.width
    rect.y = 630
    screen.blit(rendered, rect)

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
                        shoot.play()
                        bullet = Bullet(screen, player)
                    # bullets.append(bullet)
            if event.type == pg.KEYUP:
                move = 0
                moving = False

        screen.blit(pg.transform.scale(pg.image.load('images/bg.png'), (1000, 750)), (0, 0))
        if randint(1, 100) == 7:
            rnd = randint(0, len(enemies))
            for i in enemies:
                if enemies.index(i) == rnd:
                    i.create_bullet()
        [i.update_bullet() for i in enemies]
        if any([i.check_collide(player) for i in enemies]):
            bg.stop()
            end_screen('game over', score)
        if bullet is not None:
            bullet.update()
            for enm in enemies:
                if bullet.rect.colliderect(enm.rect):
                    bullet = None
                    enemies.remove(enm)
                    all_sprites.remove(enm)
                    explosion.play()
                    score += value[enm.color]
                    break
                elif bullet.y < 0:
                    bullet = None
                    break
        if moving:
            player.update(move=move)
        else:
            player.update()

        if any([i.rect.y > player.rect.y for i in enemies]):
            bg.stop()
            end_screen('game over', score)
            # break

        ########################################
        coords = [0 < i.rect.x < W - i.image.get_width() for i in enemies]

        if not all(coords):
            all_direction *= -1

        if (int(time.time() - timer) + 1) % (20 * a) == 0:
            a += 1
            for i in enemies:
                i.down()
            iteration += 1
        all_sprites.update(all_direction)
        all_sprites.draw(screen)
        #########################################
        if len(enemies) == 0:
            bg.stop()
            end_screen('', score)

        # remove_bullets(bullets)
        rendered = font.render(f'SCORE   {score}', 1, pg.Color('green'))
        rect = rendered.get_rect()
        rect.x = 1000 - rect.width
        rect.y = 650
        screen.blit(rendered, rect)
        #########################################
        pg.display.flip()
        clock.tick(FPS)


"""def remove_bullets(bullets):
    for i in bullets.copy():
        if i.rect.bottom <= 0:
            bullets.remove(i)"""


def create_enemies(screen, ino):
    """Creating enemies (will need Alien class)"""
    pass


def start_screen():
    intro_text = ["SPACE INVADERS",
                  "PRESS  ANY  KEY  TO  CONTINUE"]
    pg.font.init()
    size = W, H = 1000, 700  # list(map(int, input().split()))
    window = pg.display.set_mode(size)
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    fon = pg.transform.scale(pg.image.load('images/bg.png'), (W, H))
    screen.blit(fon, (0, 0))
    font1 = pg.font.Font('ARCADECLASSIC.TTF', 50)
    font2 = pg.font.Font('ARCADECLASSIC.TTF', 30)
    equal = pg.font.Font(None, 75)
    text_coord = 50
    for line in intro_text:
        if 'SPACE' in line:
            string_rendered = font1.render(line, 1, pg.Color('white'))
        else:
            string_rendered = font2.render(line, 1, pg.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = (W // 2) - intro_rect.width // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    y = 180
    a = [' 10   PTS', ' 15   PTS', ' 50   PTS', ' 100   PTS']
    for i in ['red', 'yellow', 'green', 'blue']:
        screen.blit(pg.image.load(f'images/{i}.png'), (280, y))
        r_eq = equal.render(' =', 1, pg.Color('white'))
        rect_eq = r_eq.get_rect()
        rect_eq.x = 430
        rect_eq.y = y + 25
        screen.blit(r_eq, rect_eq)

        rendered = font1.render(a[['red', 'yellow', 'green', 'blue'].index(i)], 1, pg.Color('white'))
        rect = rendered.get_rect()
        rect.x = 500
        rect.y = y + 27
        screen.blit(rendered, rect)
        y += 100

    with open('high_score.txt') as file:
        high_score = int(file.readlines()[-1])

    hs_rendered = font1.render('HIGH SCORE   ' + str(high_score), 1, pg.Color('yellow'))
    rect = hs_rendered.get_rect()
    rect.x = 500 - rect.width // 2
    rect.y = 620
    screen.blit(hs_rendered, rect)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN or \
                    event.type == pg.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pg.display.flip()
        clock.tick(60)


def end_screen(event, score):
    if event == 'game over':
        intro_text = ['GAME       OVER',
                      'PRESS    ENTER    TO    RESTART']
    else:
        intro_text = ['YOU       WON',
                      'PRESS    ENTER    TO    RESTART']
    pg.font.init()
    size = W, H = 1000, 700  # list(map(int, input().split()))
    window = pg.display.set_mode(size)
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    fon = pg.transform.scale(pg.image.load('images/bg.png'), (W, H))
    screen.blit(fon, (0, 0))
    font1 = pg.font.Font('ARCADECLASSIC.TTF', 50)
    font2 = pg.font.Font('ARCADECLASSIC.TTF', 30)
    text_coord = 50
    for line in intro_text:
        if 'OVER' in line:
            string_rendered = font1.render(line, 1, pg.Color('white'))
        else:
            string_rendered = font2.render(line, 1, pg.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 40
        intro_rect.top = text_coord
        intro_rect.x = (W // 2) - intro_rect.width // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    with open('high_score.txt', 'r') as file:
        hs = int(file.readlines()[-1])
    if score > hs:
        with open('high_score.txt', 'a') as file:
            file.write('\n' + str(score))
            rendered = font1.render(f'NEW    HIGH    SCORE      {score}', 1, pg.Color('green'))
            rect = rendered.get_rect()
            rect.x = W // 2 - rect.width // 2
            rect.y = 500
            screen.blit(rendered, rect)
    else:
        rendered = font1.render(f'YOUR      SCORE      {score}', 1, pg.Color('green'))
        rect = rendered.get_rect()
        rect.x = W // 2 - rect.width // 2
        rect.y = 500
        screen.blit(rendered, rect)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    start()
        pg.display.flip()
        clock.tick(60)


def start():
    start_screen()
    main()


if __name__ == '__main__':
    start()
