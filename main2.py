from plots import *
from pygame.locals import *
from buttons import *
# from model import *
from TDmain import *
from TwoD_editor import *
pygame.init()


def main():
    screen = pygame.display.set_mode((c.width, c.height))
    pygame.display.set_caption("Гравитационное линзирование")
    finished = False
    clock = pygame.time.Clock()
    fps = 30
    initiate_buttons()
    draw_buttons_and_stuff(screen)
    while not finished:
        clock.tick(fps)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                finished = True
            elif event.type == MOUSEBUTTONDOWN:
                if buttons_array[0].pressed(pygame.mouse.get_pos()):
                    a = SoftwareRender(screen)
                    a.run(finished)
                    # input1(screen)
                    # lensing(glowing_dots)
                    # output(screen)
                elif buttons_array[1].pressed(pygame.mouse.get_pos()):
                    plot1()
                elif buttons_array[2].pressed(pygame.mouse.get_pos()):
                    plot2()
                elif buttons_array[3].pressed(pygame.mouse.get_pos()):
                    plot3()


main()
pygame.quit()
