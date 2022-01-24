from setting import *
from random import randrange
import pygame


class Apple:
    count = 0

    def __init__(self, size):
        self.x = randrange(1, COL_COUNT - 1)  # начальная random x
        self.y = randrange(1, ROW_COUNT - 1)  # начальная random y
        self.size = size
        self.rect = pygame.Rect(self.x * cells, self.y * cells, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)  # яблочко

    def set_random_xy(self):  # смена позиции
        self.x = randrange(1, COL_COUNT - 1)
        self.y = randrange(1, ROW_COUNT - 1)

        self.rect.x = self.x * cells
        self.rect.y = self.y * cells

        if Apple.count % 3 == 0:  # бонус каждое 3ье яблоко
            self.size = cells + 6
            self.rect.x -= 3
            self.rect.y -= 3
        else:
            self.size = cells
        self.rect.width = self.size
        self.rect.height = self.size
