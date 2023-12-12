import pygame
import pygame as pg


class Bullet(pg.sprite.Sprite):
    def __init__(self, scr, player):
        super().__init__()
        self.screen = scr
        self.rect = pygame.Rect(0, 0, 2, 10)
        self.color = (168, 230, 29)
        self.speed = 10
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        self.y = self.rect.y