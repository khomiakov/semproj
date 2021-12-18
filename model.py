from Constants import *


"""Модуль отвечает за функцию преобразования координат"""


def lensing(array):
    for dot in array:
        r0 = np.power((c.x0 - dot[0]) ** 2 + (c.y0 - dot[1]) ** 2, 1 / 2)
        alpha = r0 / c.s
        if alpha > 0:
            angle_ratio = 1 / 2 + np.power(1 / 4 + 4 * c.m * c.g / c.d / (c.c ** 2) / (alpha ** 2), 1 / 2)
            dot[0] = int(c.x0 + (dot[0] - c.x0) * angle_ratio)
            dot[1] = int(c.y0 + (dot[1] - c.y0) * angle_ratio)


def model(screen):
    px_array = pygame.PixelArray(screen)
    white_pixels_array = []
    for i in range(c.x0 - 100, c.x0 + 100 + 1):
        for j in range(c.y0 - 100, c.y0 + 100 + 1):
            if px_array[i, j] == screen.map_rgb(c.white):
                white_pixels_array.append([i, j])
            px_array[i, j] = c.sky_color
    lensing(white_pixels_array)
    for k in range(len(white_pixels_array)):
        px_array[white_pixels_array[k][0], white_pixels_array[k][1]] = c.white
