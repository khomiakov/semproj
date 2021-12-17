import pygame
pygame.init()
info = pygame.display.Info()


class Constants:
    def __init__(self):
        """
        Все физические величины в СИ.
        """
        self.m = 1.989 * (10 ** 30) * 500   # масса чёрной дыры, 500 масс Солнца
        self.c = 299792458                  # скорость света
        self.g = 6.67408 * 10 ** (-11)      # гравитационная постоянная
        self.d = 149597870700 * 10              # расстояние до чёрной дыры
        self.r_bh = 696340000               # радиус чёрной дыры
        self.r_bh_screen = 35  # радиус чёрной дыры в экранных координатах
        self.width = info.current_w         # ширина экрана
        self.x0 = int(self.width / 2)       # координата x центра чёрной дыры на экране
        self.height = info.current_h        # высота экрана
        self.y0 = int(self.height / 2)      # координата y центра чёрной дыры на экране
        self.fps = 60
        self.white = (255, 255, 255)
        self.sky_color = (2, 8, 19)


c = Constants()
