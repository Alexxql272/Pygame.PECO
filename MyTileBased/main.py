import pygame as pg
from Constants import *
from Game import *

game = Game(TITLE)
while True:
    game.new()
    game.run()
