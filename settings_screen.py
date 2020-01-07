import pygame
from button import *
import new_button
from text_input import *
import time

pygame.font.init()
class settings_screen():
    def __init__(self):
        self.bg_colour = (255,255,255)
        self.button_pressed = False
        self.text1 = FONT.render("Max points to win:",True, (200,200,200))
        self.text2 = FONT.render("Player Name:", True, (200,200,200))
        self.text3 = FONT.render("No. of Bots", True, (200,200,200))
        self.maximum_pts = 0
        self.player_names = ''
        self.number_of_bots = 0
        
    
    def draw(self, DISPLAY):
        count = 181
        clr_val = 0
        max_points = text_input(DISPLAY, (1920/2), 200, 200, 70)
        plyr_names = text_input(DISPLAY, (1920/2), 300, 400,70)
        num_bots = text_input(DISPLAY, (1920/2), 400,200, 70)
        submit_btn = button((0,0,0), 200, 75, ((1920/2) -100, 800),"SUBMIT", (255,255,255)) 
        
        exit_btn = new_button.button((0,0,0),(65,65,65),(DISPLAY.get_width() * 19/20) -25, 50,50,50,"X", (255,255,255)) 
        exit_btn.anim = False

        while not self.button_pressed:      #game loop
            pygame.display.update() 
            DISPLAY.fill(self.bg_colour)
            #DISPLAY.blit(self.text1, ((1920/2)-10 - self.text2.get_rect().width, 235 - (self.text1.get_rect().height/2)))
            DISPLAY.blit(self.text2, ((1920/2)-10 - self.text2.get_rect().width, 335 - (self.text1.get_rect().height/2)))
            #DISPLAY.blit(self.text3, ((1920/2)-10 - self.text2.get_rect().width, 435 - (self.text1.get_rect().height/2)))
            #num_bots.draw()
            #max_points.draw()
            plyr_names.draw()
            exit_btn.draw(DISPLAY)
            submit_btn.draw_button(DISPLAY)
            
            if exit_btn.pressed:
                pygame.QUIT
                quit()

            for event in pygame.event.get():
                #max_points.activate(event)
                plyr_names.activate(event)
                #num_bots.activate(event)
                exit_btn.update(event)
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()
                if event.type == pygame.MOUSEMOTION:
                    if submit_btn.isOver(pygame.mouse.get_pos()):
                        submit_btn.colour = (65, 65, 65)
                    else:
                        submit_btn.colour = (0, 0, 0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if submit_btn.isOver(pygame.mouse.get_pos()):
                        try:
                            #self.maximum_pts = int(max_points.text)
                            self.player_names = str(plyr_names.text)
                           # self.number_of_bots = int(num_bots.text)
                            self.button_pressed = True
                        except ValueError:
                            count = 0
                            clr_val = 0
            
            if count < 180:
                DISPLAY.blit(SFONT.render("Enter valid inputs", True, (255,clr_val,clr_val)),((1920/2) -(149/2), 750))
                if count > 60:
                    clr_val += 2
                    if clr_val > 255:
                        clr_val = 255

                count += 1
                
    
