"""Модуль отвечающий за камеру наблюдателя и ее вращение в пространстве"""

import pygame as pg
from matrix_functions import *


class Camera:
    """класс камеры зрителя
    """
    def __init__(self, render, position):
        """
        self.position - позиция камеры в пространстве
        self.forward - направление оси z собственных координат камеры
        self.up  - направление оси y собственных координат камеры
        self.right  - направление оси x собственных координат камеры
        self.h_fov - угол обзора по горизонтали
        self.v_fov - угол обзора по вертикали
        self.near_plane - расстояние до ближней плоскости осечения
        self.far_plane - расстояние до дальней плоскости осечения
        self.moving_speed - скорость перемещения камеры
        self.rotation_speed - скорость поворота камеры
        """
        self.render = render
        self.position = np.array([*position, 1.0])
        self.forward = np.array([0, 0, 1, 1])   # z
        self.up = np.array([0, 1, 0, 1])        # y
        self.right = np.array([1, 0, 0, 1])     # x
        self.h_fov = math.pi / 3
        self.v_fov = self.h_fov * (render.HEIGHT / render.WIDTH)
        self.near_plane = 0.1
        self.far_plane = 100
        self.moving_speed = 0.2
        self.rotation_speed = 0.003

    def control(self):
        """управление камерой
        """
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.camera_yaw(-self.rotation_speed)
        if key[pg.K_RIGHT]:
            self.camera_yaw(self.rotation_speed)
        if key[pg.K_UP] and not self.near_north():
            self.camera_pitch(-self.rotation_speed) 
        if key[pg.K_DOWN] and not self.near_south():
            self.camera_pitch(self.rotation_speed)

    def camera_yaw(self, angle):
        """вращение камеры вокруг абсолютной оси y
        """
        rotate = rotate_y(angle)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def camera_pitch(self, angle):
        """вращение камеры вокруг собственной оси х
        """
        rotate = rotate_x(angle)
        a = rotate @ transpose(self.rotate_matrix())
        self.forward = a[2][0], a[2][1], a[2][2], 1
        self.right = a[0][0], a[0][1], a[0][2], 1
        self.up = a[1][0], a[1][1], a[1][2], 1

    def translate_matrix(self):
        """матрица перемещения"""
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],   # [0, 1, 0, 1]
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()

    def near_north(self):
        fx, fy, fz, e = self.forward
        return fx**2 + (fy-1)**2 + fz**2 <= self.rotation_speed**2

    def near_south(self):
        fx, fy, fz, e = self.forward
        return fx**2 + (fy+1)**2 + fz**2 <= self.rotation_speed**2
