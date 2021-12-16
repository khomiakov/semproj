import pygame
import numpy as np
from skymodel import *

pygame.init()

def main():
    screen_length = 1000
    screen_width = 500
    screen = pygame.display.set_mode((screen_length, screen_width))
    FPS = 30
    clock = pygame.time.Clock()
    finished = False
    obs = Observer()
    a = generate_sky()
    draw_sky(a, obs, screen, screen_length, screen_width)
    while not finished:
        #print('a')
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    obs.y += 2*np.pi/360
                if event.key == pygame.K_s:
                    obs.y -= 2*np.pi/360
                if event.key == pygame.K_d:
                    obs.x += 2*np.pi/360
                if event.key == pygame.K_a:
                    obs.x -= 2*np.pi/360
                #obs.update_coords()
                draw_sky(a, obs, screen, screen_length, screen_width)

main()
    