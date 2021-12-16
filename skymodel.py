import numpy as np
import random
import pygame

pygame.init()

class Observer:
    def __init__(self):
        self.xangl = 0
        self.yangl = 0
        self.x = 0
        self.y = 0
    
    def update_coords(self):        
        self.x -= 2*np.pi*(self.x//(2*np.pi))+np.pi
        self.y -= np.pi*(self.y//(np.pi))-np.pi/2
        print(self.x//(2*np.pi))
        #print(self.x, ' ', self.y)


class 3DObserver:
    def __init__(self):
        self.x = 0
        self.y = 1
        self.z = 0

    def rotate_z(self):
        
        
    def 
def generate_sky():
    a = np.random.sample((np.random.randint(2000, 3000), 2)) # all stars
    print(a)
    for i in range(len(a)):
        a[i][0] = (a[i][0]-0.5)*2*np.pi
        a[i][1] = (a[i][1]-0.5)*np.pi
    return a

def draw_sky(a, obs, screen, screen_length, screen_width):
    m = [] #stars that we see
    screen.fill((0, 0, 0))
    s = 1500 #расстояние от зрителя до экрана в пикселях 1500
    obs.xangle = 2*np.arctan(screen_length/2/s)
    obs.yangle = 2*np.arctan(screen_width/2/s)
    
    for i in range(len(a)):
        if (abs(a[i][0] - obs.x) < obs.xangl/2) and (abs(a[i][1] - obs.y) < obs.yangl/2):
            m.append(a[i])
    for i in range(len(m)):
        pygame.draw.circle(screen, (255, 255, 255), (screen_length/2 + round(s*np.tan(m[i][0] - obs.x)), screen_width/2-round(s*np.tan(m[i][1] - obs.y))), 1)
    pygame.display.update()


def generate_2D_sky(screen_length, screen_width):
    a = np.random.sample((np.random.randint(2000, 3000), 2))
    for i in range(len(a)):
        a[i, 0] = (a[i, 0]-0.5)*2*np.pi
        a[i, 1] = (a[i, 1]-0.5)*np.pi
    return a

def generate_3D_sky():
    a = np.random.sample((3000, 3))
    for i in range(len(a)):
        a[i][2] = a[i][0] * 2 - 1
        a[i][0] = (1 - a[i][2]**2)**0.5 * np.cos(a[i][0] * 2*np.pi)
        a[i][1] = (1 - a[i][2]**2)**0.5 * np.sin(a[i][0] * 2*np.pi)
    return a
        
