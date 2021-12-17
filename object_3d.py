"""
Этот модуль отвечает за создание 3D объекта, как массива данных
"""
import pygame as pg
from matrix_functions import *
from numba import njit
from Constants import *


@njit(fastmath=True)
def any_func(arr, a, b):
    return np.any((arr == a) | (arr == b))


class Object3D:
    def __init__(self, render, vertexes='', faces=''):
        """
        self.vertexes - массив вершин в ЛСО
        self.faces - массив связей вершин (полигонов)
        self.movement_flag - переменная, отвечающая за возможность двигать объект 
        self.draw_vertexes - переменная, отвечающая за отрисовку вершин. 
        """
        self.render = render
        self.vertexes = np.array([np.array(v) for v in vertexes])
        self.faces = np.array([np.array(face) for face in faces])
        self.translate([0.0001, 0.0001, 0.0001])

        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_faces = [(pg.Color('orange'), face) for face in self.faces]
        self.movement_flag, self.draw_vertexes = True, True
        self.label = ''

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        """
        Функция проецирует вержины на экран зрителя
        """
        vertexes = self.vertexes @ self.render.camera.camera_matrix()
        vertexes = vertexes @ self.render.projection.projection_matrix
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = vertexes @ self.render.projection.to_screen_matrix
        vertexes = vertexes[:, :2]

        for index, color_face in enumerate(self.color_faces):
            color, face = color_face
            polygon = vertexes[face]
            if not any_func(polygon, self.render.H_WIDTH, self.render.H_HEIGHT):
                pg.draw.polygon(self.render.screen, color, polygon, 1)
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color('white'))
                    self.render.screen.blit(text, polygon[-1])

        if self.draw_vertexes:
            for vertex in vertexes:
                if not any_func(vertex, self.render.H_WIDTH, self.render.H_HEIGHT):
                    pg.draw.circle(self.render.screen, c.white, vertex, 2)

    def translate(self, pos):
        """
        Функция перемещения вершин в пространстве
        """
        self.vertexes = self.vertexes @ translate(pos)

    def scale(self, scale_to):
        """
        Функция выравнивания вершин в пространстве
        """
        self.vertexes = self.vertexes @ scale(scale_to)

    def rotate_x(self, angle):
        """
        Функция поворота вершин в пространстве вокруг х
        """
        self.vertexes = self.vertexes @ rotate_x(angle)

    def rotate_y(self, angle):
        """
        Функция поворота вершин в пространстве вокруг у
        """
        self.vertexes = self.vertexes @ rotate_y(angle)

    def rotate_z(self, angle):
        """
        Функция поворота вершин в пространстве вокруг z
        """
        self.vertexes = self.vertexes @ rotate_z(angle)


class Axes(Object3D):
    """
    Функция рисующая оси координат в пространстве
    """

    def __init__(self, render):
        super().__init__(render)
        self.vertexes = np.array([(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])
        self.faces = np.array([(0, 1), (0, 2), (0, 3)])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertexes = False
        self.label = 'XYZ'
