"""
Этот модуль отвечает за создание 3D объекта, как массива данных. Также здесь обрабатывается основной цикл прорисовки.
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
        self.draw_vertexes - переменная, отвечающая за отрисовку вершин
        self.font - шрифт надписи у полигона
        self.color_faces - цвет полигона
        self.label - надпись на полигоне
        self.blinking - переменная, отвечающая за мерцание
        """
        self.render = render
        self.vertexes = np.array([np.array(v) for v in vertexes])
        self.faces = np.array([np.array(face) for face in faces])
        self.translate([0.0001, 0.0001, 0.0001])

        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_faces = [(pg.Color('orange'), face) for face in self.faces]
        self.movement_flag, self.draw_vertexes, self.blinking = True, True, False
        self.label = ''
        self.star_size = generate_star_size()

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        """
        Основной цикл прорисовки. Функция проецирует вершины на экран зрителя.
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
            i = 0
            for vertex in vertexes:
                if not any_func(vertex, self.render.H_WIDTH, self.render.H_HEIGHT):
                    if self.blinking:
                        pg.draw.circle(self.render.screen, c.white, vertex, np.random.randint(0, 4))
                    else:
                        pg.draw.circle(self.render.screen, c.white, vertex, self.star_size[i])
                i+=1

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
    """Класс осей координат (левый верхний угол на экране)
       По сути такой же класс, как Object3D, но привязан к камере, а не пространству
    """

    def __init__(self, render):
        super().__init__(render, np.array([(0, 0, 0, 1), (1, 0, 0, 0.1), (0, 0.1, 0, 1), (0, 0, 0.1, 1)]),
                         np.array([(0, 1), (0, 2), (0, 3)]))
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertexes = False
        self.label = 'XYZ'

    def update(self):
        """метод привязки осей к местоположению камеры"""
        self.vertexes = np.array([(0, 0, 0, 1), (0.1, 0, 0, 1), (0, 0.1, 0, 1), (0, 0, 0.1, 1)])
        f = np.array(self.render.camera.forward)
        r = np.array(self.render.camera.right)
        u = np.array(self.render.camera.up)
        a = f + r * -0.45 + u * 0.2
        pos = a[0:3]
        self.translate(pos)

    def draw(self):
        self.update()
        self.screen_projection()


def generate_3d_sky():
    """Генерирует случайный массив звезд для класса Object3D"""
    a = np.random.sample((3000, 4))
    r = 1
    for i in range(len(a)):
        a[i][2] = (a[i][2] * 2 - 1) * r
        a[i][1] = (r ** 2 - a[i][2] ** 2) ** 0.5 * np.sin(a[i][0] * 2 * np.pi)
        a[i][0] = (r ** 2 - a[i][2] ** 2) ** 0.5 * np.cos(a[i][0] * 2 * np.pi)
        a[i][3] = 1
    return a

def generate_star_size():
    """Генерирует массив с размерами звезд
    """
    a = np.random.sample(3000)
    for i in range(len(a)):
        a[i] = round(a[i] * 3)
    return a


def gen_equator_vert():
    """Генерирует массив вершин экватора для класса Object3D"""
    a = []
    for i in range(500):
        a.append([1, 0, 0, 1] @ rotate_y(2 * np.pi * i / 500))
    return a


def gen_equator_face():
    """Генерирует массив полигонов экватора для класса Object3D"""
    a = []
    for i in range(0, 500, 2):
        a.append([i, i + 1])
    return a
