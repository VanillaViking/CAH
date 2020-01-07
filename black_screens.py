import pygame
from button import *
import new_button

pygame.font.init()
arial = pygame.font.SysFont('Arial', 40)
class black_screens():
    def __init__(self):
        self.button_pressed = False
    
    def draw(self, DISPLAY, text):
        self.button_pressed = False
        player_text = arial.render(text, True, (255,255,255))
        cont_button = button((255, 255, 255), 200, 75, ((1920/2) - 100, 800), "continue")
        exit_btn = new_button.button((255,255,255),(65,65,65),(DISPLAY.get_width() * 19/20) -25, 50,50,50,"X", (0,0,0))
        exit_btn.anim = False

        while not self.button_pressed:
            pygame.display.update()
            DISPLAY.fill((0,0,0))
            DISPLAY.blit(player_text, ((DISPLAY.get_width() / 2) - (player_text.get_width() / 2),(200) - (player_text.get_height() / 2)))
            cont_button.draw_button(DISPLAY)
            exit_btn.draw(DISPLAY)

            if exit_btn.pressed:
                pygame.QUIT
                quit()

            for event in pygame.event.get():
                exit_btn.update(event)
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()

                if event.type == pygame.MOUSEMOTION:
                    if cont_button.isOver(pygame.mouse.get_pos()):
                        cont_button.colour = (200, 200, 200)
                    else:
                        cont_button.colour = (255, 255, 255)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cont_button.isOver(pygame.mouse.get_pos()):
                        self.button_pressed = True
