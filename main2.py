from plots import *
from pygame.locals import *
from buttons import *
from model import *
from TDmain import *
pygame.init()


def main():
    screen = pygame.display.set_mode((c.width, c.height))
    pygame.display.set_caption("Гравитационное линзирование")
    finished = False
    clock = pygame.time.Clock()
    a = SoftwareRender(screen)
    initiate_buttons()
    draw_buttons_and_stuff(screen)
    while not finished:
        pygame.display.update()
        clock.tick(c.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                a.go = False
                finished = True
            elif event.type == MOUSEBUTTONDOWN:
                if buttons_array[0].pressed(pygame.mouse.get_pos()) and a.go is False:
                    a.go = True                   
                elif buttons_array[0].pressed(pygame.mouse.get_pos()) and a.go is True:
                    if a.draw_black_hole is False:
                        a.draw_black_hole = True
                    else:
                        a.draw_black_hole = False
                elif buttons_array[1].pressed(pygame.mouse.get_pos()):
                    plot1()
                elif buttons_array[2].pressed(pygame.mouse.get_pos()):
                    plot2()
                elif buttons_array[3].pressed(pygame.mouse.get_pos()):
                    plot3()
        if a.go is True:
            a.run()
            if a.draw_black_hole is False:
                draw_buttons_and_stuff_1(screen)
            else:
                draw_buttons_and_stuff_2(screen)
                model(screen)
                draw_black_hole(screen)


main()
pygame.quit()
