import os
import sys
import pygame as pg 

CAPTION = "Punching a Hole"
SCREEN_SIZE = (1000,650)
COLOR_KEY = (255, 0, 255)
ELLIPSE_SIZE = (400, 400)

class Control(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.keys = pg.key.get_pressed()
        self.background = FRACTAL
        self.ellipse_rect = pg.Rect((0,0), ELLIPSE_SIZE)

    def event_loop(self):
        for event in pg.event.get():
            self.keys = pg.key.get_pressed()
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True
    def make_hole(self):
        hole = pg.Surface(self.screen_rect.size).convert()
        hole.set_colorkey(COLOR_KEY)
        hole.fill((0,0,0))
        pg.draw.ellipse(hole, COLOR_KEY, self.ellipse_rect)
        return hole
    def make_hole_alpha(self):
        hole = pg.Surface(self.screen_rect.size).convert_alpha()
        hole.fill((255,255,200))
        pg.draw.ellipse(hole,(0,0,0), self.ellipse_rect)
        return hole
    def update(self):
        self.ellipse_rect.center = pg.mouse.get_pos()
        self.hole = self.make_hole()
    def draw(self):
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.hole, (0,0))
    def display_fps(self):
        caption = "{} - FPS: {:.2f} ".format(CAPTION, self.clock.get_fps())
        pg.display.set_caption(caption)
    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)
            self.display_fps()
if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_mode(SCREEN_SIZE)
    FRACTAL = pg.image.load('frac.jpeg').convert()
    run_it = Control()
    run_it.main_loop()
    pg.quit()
    pg.exit()





