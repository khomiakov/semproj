import numpy as np
import random
import pygame

pygame.init()

class Observer:
    def __init__(self):
        self.xangl = np.pi*2/3
        self.yangl = np.pi/3
        self.x = 0
        self.y = 0

def generate_sky():
    a = np.random.sample((np.random.randint(2000, 3000), 2)) # all stars
    #print(a)
    for i in range(len(a)):
        a[i, 0] = (a[i, 0]-0.5)*2*np.pi
        a[i, 1] = (a[i, 1]-0.5)*np.pi
    return a

def draw_sky(a, obs):
    m = [] #stars that we see
    screen_length = 1000
    screen_width = 500
    screen = pygame.display.set_mode((screen_length, screen_width))
    screen.fill((0, 0, 0))
    s = 1500 #расстояние от зрителя до экрана в пикселях
    obs.xangle = 2*np.arctan(screen_length/2/s)
    obs.yangle = 2*np.arctan(screen_width/2/s)
    for i in range(len(a)):
        if (abs(a[i][0] - obs.x) < obs.xangl/2) and (abs(a[i][1] - obs.y) < obs.yangl/2):
            m.append(a[i])
    for i in range(len(m)):
        pygame.draw.circle(screen, (255, 255, 255), (screen_length/2 + round(s*np.tan(m[i][0] - obs.x)), screen_width/2-round(s*np.tan(m[i][1] - obs.y))), 1)
    pygame.display.update()
    
        
