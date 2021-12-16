import pygame
from object_3d import *
from camera import *
from projection import *
from Constants import *
from plots import *
import pygame as pg


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()
        self.finished = False

    def create_objects(self):
        self.camera = Camera(self, [-5, 6, -55])
        self.projection = Projection(self)
        self.object = self.get_object_from_file('resources/t_34_obj.obj')
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

    def plot1(self):
        p = Plot1()
        p.draw_plot()

    def plot2(self):
        p = Plot2()
        p.draw_plot()

    def plot3(self):
        p = Plot3()
        p.draw_plot()

    def run(self):
        while not self.finished:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.finished = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                    self.plot1()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
                    self.plot2()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
                    self.plot3()


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()