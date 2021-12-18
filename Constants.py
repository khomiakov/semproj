import pygame
import numpy as np
pygame.init()
info = pygame.display.Info()


class Constants:
    def __init__(self):
        """
        Все физические величины в СИ.
        """
        self.m = 1.989 * (10 ** 30) * 50   # масса чёрной дыры, масс Солнца
        self.c = 299792458                  # скорость света
        self.g = 6.67408 * 10 ** (-11)      # гравитационная постоянная
        self.d = 149597870700               # расстояние до чёрной дыры
        self.s = 20000                      # абстрактное расстояние до экрана
        self.width = info.current_w         # ширина экрана
        self.x0 = int(self.width / 2)       # координата x центра чёрной дыры на экране
        self.height = info.current_h        # высота экрана
        self.y0 = int(self.height / 2)      # координата y центра чёрной дыры на экране
        self.r_bh_screen = int(self.s * np.power(4 * self.m * self.g / self.d / (self.c ** 2), 1 / 2))
        self.fps = 60
        self.white = (255, 255, 255)
        self.sky_color = (2, 8, 19)


c = Constants()
