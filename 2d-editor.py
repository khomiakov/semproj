"""Данный модуль отвечает за пиксельный формат реализуемой визуализации.
На входе первого этапа экран pygame. Задача: обработка изображения,
получение координат объектов в пикселях, запись информации о цвете.
Выдача информации объктов, который оказались подвергнуты эффекту
для модуля model(область определяется в модуле model).
Второй этап: model возвращает новые координаты цветных пикселей,
2d-editor отображает изменения на экране.
"""

WHITE = 16777215

def input1():
        """"В зоне действия эффекта ищет светящиеся объекты.
        Из массива всех пикселей оставляет только их.""""
        global glowing_dots
        ar = pygame.PixelArray(zone_of_influence)
        glowing_dots = []
        for i in range(len(ar)):
            for j in range(len(ar[0])): 
                if ar[i,j] == WHITE:
                glowing_dots.append([i,j])
                
def output():
    """Отрисовывает обновленный участок."""
    ar = pygame.PixelArray(zone_of_influence)
    ar[:] = 0
    for k in range(len(glowing_dots)):
        ar[glowing_dots[k][0], glowing_dots[k][1]] = (255, 255, 255)
    del ar
    screen.blit(zone_of_influence, (,))
    circle(screen, (0,0,0), (LENGTH/2, HEIGHT/2), black_hole_R)
    pygame.display.flip()
    

