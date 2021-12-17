"""Данный модуль отвечает за пиксельный формат реализуемой визуализации.
На входе первого этапа экран pygame. Задача: обработка изображения,
получение координат объектов в пикселях, запись информации о цвете.
Выдача информации объктов, который оказались подвергнуты эффекту
для модуля model(область определяется в модуле model).
Второй этап: model возвращает новые координаты цветных пикселей,
2d-editor отображает изменения на экране.
"""
from model import *
# zone_of_influence = pygame.Surface((4*c.r_bh_screen, 4*c.r_bh_screen))


def input1():
    """"В зоне действия эффекта ищет светящиеся объекты.
    Из массива всех пикселей оставляет только их."""
    ar = pygame.PixelArray(zone_of_influence)
    for i in range(len(ar)):
        for j in range(len(ar[0])): 
            if ar[i,j] == c.white and (i > c.x0 - 2*c.r_bh_screen) and\
                    i < (c.x0 + 2*c.r_bh_screen) and j > (c.y0 - 2*c.r_bh_screen) and j < (c.y0 + 2*c.r_bh_screen):
                c.glowing_dots.append([i, j])


def output(screen):
    """Отрисовывает обновленный участок."""
    ar = pygame.PixelArray(zone_of_influence)
    ar[:] = 0
    for k in range(len(c.glowing_dots)):
        c.glowing_dots[k][0] += - int((c.width - 4*c.r_bh_screen)/2)
        c.glowing_dots[k][1] += - int((c.height - 4*c.r_bh_screen)/2)
        ar[c.glowing_dots[k][0], c.glowing_dots[k][1]] = (255, 255, 255)
    del ar
    # screen.blit(zone_of_influence, (c.x0 - 2*c.r_bh_screen, c.y0 - 2*c.r_bh_screen))
    # pygame.draw.rect(screen, (0, 0, 0), [c.x0 - 2 * c.r_bh_screen, c.y0 - 2 * c.r_bh_screen, 4 * c.r_bh_screen,
    #                 4 * c.r_bh_screen])
    pygame.draw.circle(screen, (0, 0, 0), (c.x0, c.y0), c.r_bh_screen)
    c.glowing_dots.clear()

    

