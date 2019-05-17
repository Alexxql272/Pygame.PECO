import pygame as pg
from Constants import *
from Map import collide_hit_rect
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.group = game.sprite_list
        pg.sprite.Sprite.__init__(self, self.group)
        self.game = game
        # load image
        self.back_img = game.player_img_back
        self.front_img = game.player_img_front
        self.left_img = game.player_img_left
        self.right_img = game.player_img_right

        self.image = self.front_img

        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def move(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.image = self.back_img
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.image = self.front_img
            self.vel.y = PLAYER_SPEED
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.image = self.left_img
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.image = self.right_img
            self.vel.x = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def collide(self, type):
        if type == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2.0
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2.0
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if type == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2.0
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2.0
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y

    def update(self):
        self.move()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        self.collide('x')
        self.hit_rect.centery = self.pos.y
        self.collide('y')
        self.rect.center = self.hit_rect.center

class NPC(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.group = game.sprite_list, game.npcs
        pg.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.image = pg.Surface((TILESIZE/2,TILESIZE/2))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.hit_rect = self.rect

    def update(self):
        pass



class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.group = game.sprite_list, game.mobs
        pg.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.image = pg.Surface((TILESIZE*0.8, TILESIZE*0.8))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.startX = x * TILESIZE
        self.startY = y * TILESIZE
        self.destX = self.startX
        self.destY = self.startY
        self.initTime = pg.time.get_ticks()
        self.rect.center = (self.startX, self.startY)

    def update(self):
        # randomly walk
        self.presentTick = pg.time.get_ticks()
        self.tick = self.presentTick - self.initTime
        # 如何让这个记住上次的位置，再移动到新的位置？
        # 如果现在的时间差/1000的余数小于等于8就移动
        if self.tick % 1000 <= 10:
            self.destX = rand(range(self.startX-2, self.startX+3))
            self.destY = rand(range(self.startY-2, self.startY+3))
            print(self.destX, self.destY)
            self.move((self.nowX,self.nowY), (self.destX, self.destY))

    def move(self, startPos, destPos):
        pass

class Wall(pg.sprite.Sprite):
    def __init__(self, game, xPos, yPos):
        self.group = game.sprite_list, game.walls
        pg.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.xPos = xPos
        self.yPos = yPos
        self.rect.x = xPos * TILESIZE
        self.rect.y = yPos * TILESIZE

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, xPos, yPos, w, h):
        self.group = game.walls
        pg.sprite.Sprite.__init__(self, self.group)
        self.game = game
        self.rect = pg.Rect(xPos, yPos,w, h)
        self.xPos = xPos
        self.yPos = yPos
        self.rect.x = xPos
        self.rect.y = yPos
