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
    visualization = VisualEngine(screen)
    mapping = create_mapping()
    initiate_buttons()
    draw_buttons_and_stuff(screen)
    while not finished:
        pygame.display.update()
        clock.tick(c.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                visualization.go = False
                finished = True
            elif event.type == MOUSEBUTTONDOWN:
                if buttons_array[0].pressed(pygame.mouse.get_pos()) and visualization.go is False:
                    visualization.go = True
                elif buttons_array[4].pressed(pygame.mouse.get_pos()) and visualization.go is False:
                    give_information()
                elif buttons_array[0].pressed(pygame.mouse.get_pos()) and visualization.go is True:
                    if visualization.draw_black_hole is False:
                        visualization.draw_black_hole = True
                    else:
                        visualization.draw_black_hole = False
                elif buttons_array[1].pressed(pygame.mouse.get_pos()):
                    plot1()
                elif buttons_array[2].pressed(pygame.mouse.get_pos()):
                    plot2()
                elif buttons_array[3].pressed(pygame.mouse.get_pos()):
                    plot3()
        if visualization.go is True:
            visualization.run()
            if visualization.draw_black_hole is False:
                draw_buttons_and_stuff_1(screen)
            else:
                draw_buttons_and_stuff_2(screen)
                model(screen, mapping)
                draw_black_hole(screen)


main()
pygame.quit()
