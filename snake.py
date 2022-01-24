import pygame
from setting import *


class Snake(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (cells, cells))
        # начальная установочка змейки
        self.body = [[COL_COUNT // 2, ROW_COUNT // 2],
                     [COL_COUNT // 2, ROW_COUNT // 2 + 1],
                     [COL_COUNT // 2, ROW_COUNT // 2 + 2]]
        self.direction = [-1, 0]
        self.old_key = ""
        self.speed = 10
        self.lives = 5
        self.points = 0

        '''движение змейки'''

    def set_direction(self, key):
        if self.old_key == key:
            self.speed = 20
        # вверх
        if key == pygame.K_UP and self.direction != [0, 1]:
            self.direction = [0, -1]
            self.old_key = key
        # лево
        elif key == pygame.K_LEFT and self.direction != [1, 0]:
            self.direction = [-1, 0]
            self.old_key = key
        # право
        elif key == pygame.K_RIGHT and self.direction != [-1, 0]:
            self.direction = [1, 0]
            self.old_key = key
        # вниз
        elif key == pygame.K_DOWN and self.direction != [0, -1]:
            self.direction = [0, 1]
            self.old_key = key

    def move(self):
        self.body.insert(0, [self.body[0][0] + self.direction[0],
                             self.body[0][1] + self.direction[1]])
        self.body[0][0] = self.body[0][0] % COL_COUNT
        self.body[0][1] = self.body[0][1] % ROW_COUNT

    def draw(self, screen):
        for elem in self.body:
            screen.blit(self.image, (elem[0] * cells, elem[1] * cells,
                                     cells, cells))  # (увеличение) змейки и ее рисование

    def after_hit(self):
        self.lives -= 1
        # в начальную позицию
        # двигаемся вверх
        self.body = [[COL_COUNT // 2, ROW_COUNT // 2],
                     [COL_COUNT // 2, ROW_COUNT // 2 + 1],
                     [COL_COUNT // 2, ROW_COUNT // 2 + 2]]

        self.direction = [0, -1]

    def hit_walls(self, walls):
        hit = False
        for wall in walls:  # встреча со стеной
            head_rect = pygame.Rect(self.body[0][0] * cells, self.body[0][1] * cells, cells, cells)
            if wall.colliderect(head_rect):
                self.after_hit()
                hit = True
            if self.body[0] in self.body[1:]:
                self.after_hit()
                hit = True
        return hit
