import pygame as pg
# Color constant in (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Game basic settings
TITLE = 'My First Game'
FPS = 60
WIDTH = 1024
HEIGHT = 720
TILESIZE = 64


# Player settings
PLAYER_IMG_FRONT = 'assets/player/player_front.png'
PLAYER_IMG_BACK = 'assets/player/player_back.png'
PLAYER_IMG_LEFT = 'assets/player/player_left.png'
PLAYER_IMG_RIGHT = 'assets/player/player_right.png'
PLAYER_ROT_SPEED = 250
PLAYER_SPEED = 150
PLAYER_HIT_RECT = pg.Rect(0, 0, 25, 45)

# Mob settings
MOB_SPEED = 125
