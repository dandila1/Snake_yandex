import pygame
W = 480
H = 320

CELL_SIZE = 10
COL_COUNT = W // CELL_SIZE
ROW_COUNT = H // CELL_SIZE

image = r'images\part.png'


RED = (255, 50, 30)
BLUE = (50, 80, 255)
BLACK = (0, 0, 0)
TURQUOISE = (0, 230, 230)


class Walls(object):
    def createList(self, size):
        walls = []

        walls.append(pygame.Rect((0, 0), (W, size)))
        walls.append(pygame.Rect((0, H - size), (W, size)))
        return walls
