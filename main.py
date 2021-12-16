import pygame
from plots import *
from pygame.locals import *

pygame.init()


def plot1():
    p = Plot1()
    p.draw_plot()


def plot2():
    p = Plot2()
    p.draw_plot()


def plot3():
    p = Plot3()
    p.draw_plot()



class Button:
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x, y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = int(length//len(text)) + 6
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):           
        for i in range(1, 10):
            s = pygame.Surface((length+(i*2), height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i, y-i, length+i, height+i), width)
            surface.blit(s, (x-i, y-i))
        pygame.draw.rect(surface, color, (x, y, length,height), 0)
        pygame.draw.rect(surface, (190, 190, 190), (x, y, length, height), 1)
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Гравитационное линзирование")
Button1 = Button()
Button2 = Button()
Button3 = Button()
Button4 = Button()
Button.create_button(Button1, screen, (40, 40, 40), 600, 300, 200, 100, 0, "Визуализация эффекта", (255, 255, 255))
Button.create_button(Button2, screen, (40, 40, 40), 0, 350, 70, 50, 0, "f(m)", (255, 255, 255))
Button.create_button(Button3, screen, (40, 40, 40), 70, 350, 70, 50, 0, "f(a)", (255, 255, 255))
Button.create_button(Button4, screen, (40, 40, 40), 140, 350, 70, 50, 0, "f(d)", (255, 255, 255))
pygame.display.flip()


fontObj = pygame.font.Font('freesansbold.ttf', 10)
textSurfaceObj = fontObj.render('Нажмите для построения графиков:', True, (255,255,255))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (105, 330)    
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
                print("pass")
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_F1) or Button2.pressed(pygame.mouse.get_pos()):
                plot1()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_F2) or Button3.pressed(pygame.mouse.get_pos()):
                plot2()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_F3) or Button4.pressed(pygame.mouse.get_pos()):
                plot3()

    
pygame.quit()


    

