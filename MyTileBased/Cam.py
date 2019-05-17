import pygame as pg
from Constants import *

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = int(WIDTH / 2) - target.rect.centerx
        y = int(HEIGHT / 2) - target.rect.centery

        # limit the camera withing the map
        x = min(0, x) # left
        y = min(0, y) # top
        x = max((WIDTH - self.width), x) # right
        y = max((HEIGHT - self.height), y) # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
