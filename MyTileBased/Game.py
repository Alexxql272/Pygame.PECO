import pygame as pg
import sys
from os import path
import Constants
from Sprite import *
from Cam import *
from Map import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.showFPS = False
        self.showGRID = False

    def load_data(self):
        game_folder = path.dirname(__file__)
        ass_foder = path.join(game_folder, 'assets')
        map_folder = path.join(ass_foder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'testmap1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img_front = pg.image.load(PLAYER_IMG_FRONT).convert_alpha()
        self.player_img_back = pg.image.load(PLAYER_IMG_BACK).convert_alpha()
        self.player_img_right = pg.image.load(PLAYER_IMG_RIGHT).convert_alpha()
        self.player_img_left = pg.image.load(PLAYER_IMG_LEFT).convert_alpha()
    # initialize all variables and setup a new game
    def new(self):
        self.sprite_list = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.npcs = pg.sprite.Group()
        # self.player = Player(self, 10, 10)
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                        tile_object.width, tile_object.height)
            if tile_object.name == 'npc':
                NPC(self, tile_object.x, tile_object.y)
        self.camera = Camera(self.map.width, self.map.height)

    # Game main loop
    def run(self):
        self.isRunning = True
        while self.isRunning:
            pg.time.delay(10)
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    # Quit method, to quit pygame
    def quit(self):
        pg.quit()
        sys.exit()

    # Events method to deal with all kinds of events
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.KEYUP:
                # press F1 to draw grid on the screen
                if event.key == pg.K_F1:
                    self.showGRID = not self.showGRID
                # show the FPS on the title
                if event.key == pg.K_F5:
                    self.showFPS = not self.showFPS

    # Update the screen
    def update(self):
        # pg.display.update()
        keys = pg.key.get_pressed()
        self.sprite_list.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    # Draw method
    def draw(self):
        if self.showFPS:
            pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        else:
            pg.display.set_caption(TITLE)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.sprite_list:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.showGRID:
                pg.draw.rect(self.screen, BLACK, self.camera.apply_rect(sprite.hit_rect), 1)
                for wall in self.walls:
                    pg.draw.rect(self.screen, BLACK, self.camera.apply_rect(wall.rect), 1)
        pg.display.flip()
