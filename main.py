import pygame
import numpy as np
from skymodel import *

def testsky():
    obs = Observer()
    a = generate_sky()
    draw_sky(a, obs) 

def main():
    FPS = 30
    clock = pygame.time.Clock()
    finished = False
    testsky()
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    

main()
    