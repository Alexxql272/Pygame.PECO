import pygame as pg

class Test:
    def __init__(self):
        pg.init()
        self.isRunning = True
        self.screen = pg.display.set_mode((512, 512))
        pg.display.set_caption('Test')

    def run(self)
        while self.isRunning:
            pg.time.delay(10)
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0,0,0))

if __name__ == '__main__':
    t1 = Test()
    ti.run()
