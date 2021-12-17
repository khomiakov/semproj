from plots import *
from pygame.locals import *
from buttons import *
from Constants import *
from TDmain import *

pygame.init()
screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Гравитационное линзирование")
Button1 = Button()
Button2 = Button()
Button3 = Button()
Button4 = Button()
Button.create_button(Button1, screen, (40, 40, 40), c.width - 200, c.height - 100, 200, 100, 0, "Визуализация эффекта",
                     (255, 255, 255))
Button.create_button(Button2, screen, (40, 40, 40), 0, c.height - 50, 70, 50, 0, "f(m)", (255, 255, 255))
Button.create_button(Button3, screen, (40, 40, 40), 70, c.height - 50, 70, 50, 0, "f(a)", (255, 255, 255))
Button.create_button(Button4, screen, (40, 40, 40), 140, c.height - 50, 70, 50, 0, "f(d)", (255, 255, 255))
pygame.display.flip()
fontObj = pygame.font.Font('freesansbold.ttf', 10)
textSurfaceObj = fontObj.render('Нажмите для построения графиков:', True, (255, 255, 255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (105, c.height - 70)
screen.blit(textSurfaceObj, textRectObj)
pygame.display.update()
finished = False
clock = pygame.time.Clock()

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            finished = True
        elif event.type == MOUSEBUTTONDOWN:
            if Button1.pressed(pygame.mouse.get_pos()):
                a = SoftwareRender(screen)
                a.run()
            if Button2.pressed(pygame.mouse.get_pos()):
                plot1()
            elif Button3.pressed(pygame.mouse.get_pos()):
                plot2()
            elif Button4.pressed(pygame.mouse.get_pos()):
                plot3()

pygame.quit()


    

