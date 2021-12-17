from object_3d import *
from camera import *
from projection import *
import pygame as pg
  

class SoftwareRender:
    def __init__(self, screen):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 800, 400
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = screen
        self.clock = pg.time.Clock()
        self.create_objects()
        self.camera = Camera(self, [0, 0, 0])
        self.projection = Projection(self)
        self.object = Object3D(self, generate_3D_sky())

    def create_objects(self):
        self.camera = Camera(self, [0, 0, 0])
        self.projection = Projection(self)
        self.object = Object3D(self, generate_3D_sky())
        self.object.rotate_y(-math.pi / 4)

    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertex, faces)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.object.draw()

    def run(self, finished):
        while not finished:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    finished = True
