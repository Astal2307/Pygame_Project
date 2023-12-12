import pygame as pg


class Player:
    def __init__(self, scr):
        self.screen = scr
        self.image = pg.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen.get_height()
        self.rect.centerx = self.screen.get_width() // 2

    def update(self, move=0):
        if self.rect.right + move < self.screen.get_width() and self.rect.left + move > 0:
            self.rect.x += move
        self.screen.blit(self.image, self.rect)
