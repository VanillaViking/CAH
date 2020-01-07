import pygame
from button import *

pygame.font.init()
arial = pygame.font.SysFont('Arial', 69)
cont_button = button((228, 159, 15), 200, 75, ((1920/2) - 100, 660), "continue")

class starting_screen():
    def __init__(self):
        self.bgcolour = (0,0,0)
        self.buttonPressed = False
        #self.text = arial.render("Cards Against Humanity", True,(255,255,255))
    
    def draw(self, DISPLAY):
        
        exit_button = button((255, 255, 255), 50, 50, ((DISPLAY.get_width()* 9/10) - 25, 50), "X")
        bg_image = pygame.transform.scale(pygame.image.load("start.png"), (DISPLAY.get_width(),DISPLAY.get_height()))

        DISPLAY.blit(bg_image, (0,0))
        while not self.buttonPressed: #game loop
            pygame.display.update()
           # DISPLAY.blit(self.text, ((1920 / 2) - (self.text.get_width() / 2),(200) - (self.text.get_height() / 2)))
            cont_button.draw_button(DISPLAY)
            exit_button.draw_button(DISPLAY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()
                if event.type == pygame.MOUSEMOTION:
                    if cont_button.isOver(pygame.mouse.get_pos()):
                        cont_button.colour = (248, 179, 35)
                    else:
                        cont_button.colour = (228, 159, 15) 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cont_button.isOver(pygame.mouse.get_pos()):
                        self.buttonPressed = True
                    elif exit_button.isOver(pygame.mouse.get_pos()):
                        pygame.QUIT
                        quit()
                
