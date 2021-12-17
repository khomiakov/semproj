import numpy as np
from Constants import *


"""Модуль отвечает за функцию преобразования координат"""


def lensing(array):
    for dot in array:
        r0 = np.power((c.x0 - dot[0]) ** 2 + (c.y0 - dot[1]) ** 2, 1 / 2)
        alpha = np.arctan(r0 / c.s)
        angle_ratio = 1 / 2 + np.power(1 / 4 + 4 * c.m * c.g / c.d / (c.c ** 2) / (alpha ** 2), 1 / 2)
        dot[0] = int(c.x0 + (dot[0] - c.x0) * angle_ratio)
        dot[1] = int(c.y0 + (dot[1] - c.y0) * angle_ratio)
