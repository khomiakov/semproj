import numpy as np
import pygame
pygame.init()


class Constants:
    def __init__(self):
        """
        Здесь параметры чёрной дыры - параметра Солнца.
        """
        self.m = 1.989 * (10 ** 30)  # масса чёрной дыры
        self.c = 299792458  # скорость света
        self.g = 6.67408 * 10 ** (-11)  # гравитационная постоянная
        self.d = 149597870700  # расстояние до чёрной дыры
        self.width = 1000  # ширина экрана, условность
        self.x0 = self.width / 2  # координата x центра чёрной дыры на экране
        self.height = 500  # высота экрана, условность
        self.y0 = self.height / 2  # координата y центра чёрной дыры на экране
        self.s = 1500
        self.r_bh_screen = 50
        self.r_bh = 696340000


c = Constants()


def draw_a_normal_line(x0, y0, x1, y1, width, color, screen):
    vector_x = x1 - x0
    vector_y = y1 - y0
    vector_length = np.power(vector_x ** 2 + vector_y ** 2, 1 / 2)
    pygame.draw.polygon(screen, color, [
        (x0 - vector_y * width / vector_length, y0 + vector_x * width / vector_length),
        (x0 + vector_x - vector_y * width / vector_length, y0 + vector_y + vector_x * width / vector_length),
        (x0 + vector_x + vector_y * width / vector_length, y0 + vector_y - vector_x * width / vector_length),
        (x0 + vector_y * width / vector_length, y0 - vector_x * width / vector_length)
    ])


def f1(alpha):
    return - alpha / 2 + np.power((alpha / 2) ** 2 + 4 * c.m * c.g / c.d / (c.c ** 2), 1 / 2)


def f2(m):
    alpha = np.arctan(c.r_bh_screen / c.s)
    return - alpha / 2 + np.power((alpha / 2) ** 2 + 4 * m * c.g / c.d / (c.c ** 2), 1 / 2)


def f3(d):
    alpha = np.arctan(c.r_bh_screen / c.s)
    return - alpha / 2 + np.power((alpha / 2) ** 2 + 4 * c.m * c.g / d / (c.c ** 2), 1 / 2)


def draw_plot():
    width = 1366
    height = 768
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    fps = 30
    dark_green = (26, 94, 26)
    black = (0, 0, 0)
    white = (255, 255, 255)
    finished = False
    x_obs = 50
    y_obs = 10 + height * 3 / 20
    f1_array, f2_array, f3_array, fi1, fi2, fi3 = [], [], [], [], [], []
    ff1 = []
    ff2 = []
    ff3 = []
    for i in range(1, 1000):
        f1_array.append(30 + i * 404 / 1000)
        f2_array.append(480 + i * 404 / 1000)
        f3_array.append(930 + i * 404 / 1000)
    for i in range(len(f1_array)):
        fi1.append(height - 30 - f1(2 * (f1_array[i] - 30) * np.arctan(c.r_bh_screen / c.s) / 404) * 404 / 0.000168)
        fi2.append(height - 30 - f2(1000 * (f2_array[i] - 480) * c.m / 404) * 404 / 0.0012)
        fi3.append(height - 30 - f3(10000 * (f3_array[i] - 930) * c.d / 404) * 404 / 0.00000015)
    for i in range(len(fi1)):
        ff1.append([f1_array[i], fi1[i]])
        ff2.append([f2_array[i], fi2[i]])
        ff3.append([f3_array[i], fi3[i]])

    while not finished:
        screen.fill(white)
        draw_a_normal_line(10, 10, width - 10, 10, 1, black, screen)
        draw_a_normal_line(width - 10, 10, width - 10, height * 3 / 10, 1, black, screen)
        draw_a_normal_line(width - 10, height * 3 / 10, 10, height * 3 / 10, 1, black, screen)
        draw_a_normal_line(10, height * 3 / 10, 10, 10, 1, black, screen)
        pygame.draw.circle(screen, dark_green, (x_obs, y_obs), 5)
        pygame.draw.circle(screen, black, (800, y_obs), 15)
        draw_a_normal_line(x_obs, y_obs, width - 10, y_obs, 1, black, screen)
        draw_a_normal_line(x_obs, y_obs, width - 10, y_obs - 50, 1, black, screen)
        draw_a_normal_line(800, y_obs - (750 * 50 / (width - 60) + 30), width - 10, y_obs - 80, 1, black, screen)
        draw_a_normal_line(x_obs, y_obs, 1356, y_obs - ((800 - 50) * 50 / (width - 60) + 30) / 750 * (1356 - 50),
                           1, black, screen)
        draw_a_normal_line(30, height - 30, height / 2 + 50, height - 30, 1, black, screen)
        draw_a_normal_line(30, height - 30, 30, height / 2 - 50, 1, black, screen)
        draw_a_normal_line(30 + 450, height - 30, height / 2 + 50 + 450, height - 30, 1, black, screen)
        draw_a_normal_line(30 + 450, height - 30, 30 + 450, height / 2 - 50, 1, black, screen)
        draw_a_normal_line(30 + 900, height - 30, height / 2 + 50 + 900, height - 30, 1, black, screen)
        draw_a_normal_line(30 + 900, height - 30, 30 + 900, height / 2 - 50, 1, black, screen)
        for i in range(len(ff1) - 1):
            draw_a_normal_line(ff1[i][0], ff1[i][1], ff1[i + 1][0], ff1[i + 1][1], 1,  black, screen)
            draw_a_normal_line(ff2[i][0], ff2[i][1], ff2[i + 1][0], ff2[i + 1][1], 1, black, screen)
            draw_a_normal_line(ff3[i][0], ff3[i][1], ff3[i + 1][0], ff3[i + 1][1], 1, black, screen)
        pygame.draw.arc(screen, black, [400, y_obs - 27, 20, 15], - np.pi / 2, np.pi / 2)
        pygame.draw.arc(screen, black, [1160, y_obs - 89, 20, 15], - np.pi / 2, np.pi / 2)
        pygame.display.update()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                finished = True


draw_plot()
pygame.quit()
