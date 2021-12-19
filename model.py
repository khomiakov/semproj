from Constants import *


"""Модуль отвечает за функцию преобразования координат"""


def create_mapping():
    initial_array = []
    new_array = []
    for i in range(c.x0 - 150, c.x0 + 150 + 1):
        for j in range(c.y0 - 150, c.y0 + 150 + 1):
            initial_array.append([i, j])
    for dot in initial_array:
        r0 = np.power((c.x0 - dot[0]) ** 2 + (c.y0 - dot[1]) ** 2, 1 / 2)
        alpha = r0 / c.s
        if alpha > 0:
            angle_ratio = 1 / 2 + np.power(1 / 4 + 4 * c.m * c.g / c.d / (c.c ** 2) / (alpha ** 2), 1 / 2)
            new_array.append([int(c.x0 + (dot[0] - c.x0) * angle_ratio), int(c.y0 + (dot[1] - c.y0) * angle_ratio)])
        else:
            new_array.append([0, 0])
    b = [initial_array, new_array]
    return {(b[0][i][0], b[0][i][1]): (b[1][i][0], b[1][i][1]) for i in range(len(initial_array))}


def model(screen, b):
    px_array = pygame.PixelArray(screen)
    px = []
    for i in range(c.x0 - 150, c.x0 + 150 + 1):
        for j in range(c.y0 - 150, c.y0 + 150 + 1):
            if px_array[i, j] == screen.map_rgb(c.white):
                px.append(b[i, j])
    px_array[c.x0 - 150: c.x0 + 150, c.y0 - 150: c.y0 + 150] = \
        c.sky_color
    for i in px:
        px_array[i] = c.white
