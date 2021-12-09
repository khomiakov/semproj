"""Файл для тренировки работы с оператором pygame.PixelArray"""

import pygame
from pygame.draw import *
from random import randint


pygame.init()
screen = pygame.display.set_mode((801, 400))


"""surface = pygame.Surface ((1, 2))

ar = pygame.PixelArray (surface)
r, g, b = 5, 255, 255
ar[0,0] = (r, g, b)
del ar
screen.blit (surface, (0,0))
pygame.display.flip()"""

surface1 = pygame.Surface((400, 400))
surface2 = pygame.Surface((400, 400))
line(screen, (255, 255, 255), [400, 0], [400, 400], 1)
pygame.display.flip()

for i in range(10):
    circle(surface1, (255,255,255),(randint(0,400), randint(0,400)),2)
screen.blit (surface1, (0,0))
pygame.display.flip()

ar = pygame.PixelArray(surface1)
glowing_dots = []
for i in range(400):
    for j in range(400): 
        if ar[i,j] == 16777215:
            glowing_dots.append([i,j])
print(glowing_dots[0][1])

for k in range(len(glowing_dots)):
    if glowing_dots[k][0] < 50:
        glowing_dots[k][0] += 50 
    elif glowing_dots[k][0] < 100:
        glowing_dots[k][0] += 30
    elif glowing_dots[k][0] < 150:
        glowing_dots[k][0] += 10
    elif glowing_dots[k][0] > 250:
        glowing_dots[k][0] += -10
    elif glowing_dots[k][0] < 300:
        glowing_dots[k][0] += -30
    elif glowing_dots[k][0] < 350:
        glowing_dots[k][0] += - 50

ar = pygame.PixelArray (surface2)
for k in range(len(glowing_dots)):
    ar[glowing_dots[k][0], glowing_dots[k][1]] = (255, 255, 255)
del ar
screen.blit(surface2, (401,0))
pygame.display.flip()


finished = False
clock = pygame.time.Clock()
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    
pygame.quit()

#ar хранит данные о цвете пикселя в формате r*256^2 + g*256 + b.
