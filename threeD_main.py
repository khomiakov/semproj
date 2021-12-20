from object_3d import *
from camera import *
from projection import *
import pygame as pg
from Constants import *
pg.init()


class VisualEngine:
    def __init__(self, screen):
        self.RES = self.WIDTH, self.HEIGHT = c.width, c.height
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.screen = screen
        self.create_objects()
        self.camera = Camera(self, [0, 0, 0])
        self.projection = Projection(self)
        self.go = False
        self.draw_black_hole = False

    def create_objects(self):
        self.camera = Camera(self, [0, 0, 0])
        self.projection = Projection(self)
        self.object = Object3D(self, generate_3d_sky())
        self.axes = Axes(self)

    def draw(self):
        self.screen.fill(c.sky_color)
        self.object.draw()
        self.axes.draw()

    def run(self):
        self.draw()
        self.camera.control()
