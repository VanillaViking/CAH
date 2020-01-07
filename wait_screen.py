import pygame
import time
import new_button

pygame.font.init()
arial = pygame.font.SysFont('Arial', 69)
s_arial = pygame.font.SysFont('Arial', 30)

class wait_screen():
    def __init__(self, server_sock):
        self.bg_colour = (255,255,255)
        self.button_pressed = False
        self.heading = arial.render("Waiting for players...", True, (0,0,0))
        self.namelist = []
        self.server_sock = server_sock
        self.stopp = False

    def draw(self, DISPLAY):
        exit_btn = new_button.button((0,0,0),(65,65,65),(DISPLAY.get_width() * 19/20) -25, 50,50,50,"X", (255,255,255))
        exit_btn.anim = False

        while not self.stopp:
            pygame.display.update()
            DISPLAY.fill(self.bg_colour)
            DISPLAY.blit(self.heading, ((DISPLAY.get_width() / 2) - (self.heading.get_width() / 2),(DISPLAY.get_height() / 5) - (self.heading.get_height() / 2)))
            exit_btn.draw(DISPLAY)
            if exit_btn.pressed:
                pygame.QUIT
                quit()
            y_val = 100
            for name in self.namelist:
                rend_name = s_arial.render(name, True, (0,0,0))
                DISPLAY.blit(rend_name, (((DISPLAY.get_width()/4) - rend_name.get_width()/2),(DISPLAY.get_height()/5 + y_val)))
                y_val += 70

            for event in pygame.event.get():
                exit_btn.update(event)
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()


    def update(self, namelist):
        self.namelist = namelist

    def stop(self):
        self.stopp = True
