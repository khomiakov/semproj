import numpy as np


class Constants:
    def __init__(self):
        """
        Здесь параметры чёрной дыры - параметра Солнца.
        """
        self.m = 1.989 * (10 ** 30)  # масса чёрной дыры
        self.c = 299792458  # скорость света
        self.g = 6.67408 * 10 ** (-11)  # гравитационная постоянная
        self.d = 149597870700  # расстояние до чёрной дыры
        self.r_sc = 50  # радиус чёрной дыры в экранных координатах
        self.r_bh = 696340000  # радиус чёрной дыры
        self.width = 1000  # ширина экрана, условность
        self.x0 = self.width / 2  # координата x центра чёрной дыры на экране
        self.height = 500  # высота экрана, условность
        self.y0 = self.height / 2  # координата y центра чёрной дыры на экране


c = Constants()


def lensing(array):
    for dot in array:
        r0 = np.power((c.x0 - dot[0]) ** 2 + (c.y0 - dot[1]) ** 2, 1 / 2)
        alpha = r0 * c.r_bh / c.d / c.r_sc
        angle_ratio = 1 / 2 + np.power(1 / 4 + 4 * c.m * c.g / c.d / (c.c ** 2) / (alpha ** 2), 1 / 2)
        dot[0] = int(c.x0 + (dot[0] - c.x0) * angle_ratio)
        dot[1] = int(c.y0 + (dot[1] - c.y0) * angle_ratio)
        # print(angle_ratio, (angle_ratio * alpha - alpha) * 180 / np.pi * 3600) # в угловых секундах
