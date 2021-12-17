import pygame
pygame.init()
info = pygame.display.Info()


class Constants:
    def __init__(self):
        """
        Все физические величины в СИ.
        """
        self.m = 1.989 * (10 ** 32)     # масса чёрной дыры, 100 масс Солнца
        self.c = 299792458              # скорость света
        self.g = 6.67408 * 10 ** (-11)  # гравитационная постоянная
        self.d = 149597870700           # расстояние до чёрной дыры
        self.width = info.current_w     # ширина экрана
        self.x0 = self.width / 2        # координата x центра чёрной дыры на экране
        self.height = info.current_h    # высота экрана
        self.y0 = self.height / 2       # координата y центра чёрной дыры на экране
        self.s = 1500                   # абстрактное расстояние до экрана
        self.r_bh_screen = 50           # радиус чёрной дыры в экранных координатах
        self.fps = 60


c = Constants()
