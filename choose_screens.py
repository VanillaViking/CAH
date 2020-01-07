import pygame
from button import *
import cli_socket
import time

class choose_screens():
    def __init__(self):
        self.bgcolour = (240,240,255)
        self.selected_card = None

    def player_choose(self, DISPLAY, player_cards, black_card):
        self.selected_card = None
        black_button = button((0,0,0), 300, 400, ((1920/2) - 150, 200), black_card, (255,255,255), 20,28, False)
        button_pressed = False
        card_buttons = []
        x_pos = 50
        for cards in player_cards:
            card_buttons.append(button((255,255,255), 200, 300, (x_pos,800), cards, (0,0,0), 15, 28, False))
            x_pos += 250
        bg_image = pygame.transform.scale(pygame.image.load("choose.png"), (DISPLAY.get_width(),DISPLAY.get_height()))
        DISPLAY.blit(bg_image, (0,0))
        while not button_pressed:
            pygame.display.update()
            black_button.draw_button(DISPLAY)
            for n in card_buttons:
                n.draw_button(DISPLAY)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()
                
                if event.type == pygame.MOUSEMOTION:
                    
                    for n in card_buttons:
                        if n.isOver(pygame.mouse.get_pos()):
                            n.colour = (240,240,240)
                        else:
                            n.colour = (255,255,255)
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for c,n in enumerate(card_buttons):
                        if n.isOver(pygame.mouse.get_pos()):
                            self.selected_card = c
                            button_pressed = True
        
    def czar_choose(self, DISPLAY, black_card, player_picks):
        self.selected_card = None
        button_pressed = False
        card_buttons = []
        xpos = 75

        black_button = button((0,0,0), 300, 400, (xpos, (1080/2) - 200), black_card, (255,255,255), 20,28, False)
        xpos += 350

        for pick in player_picks:
            card_buttons.append(button((255,255,255), 200, 300, (xpos,(1080/2) - 150), pick, (0,0,0), 15, 28, False))
            xpos += 250
        
        while not button_pressed:
            pygame.display.update()
            DISPLAY.fill(self.bgcolour)
            black_button.draw_button(DISPLAY)
            for n in card_buttons:
                n.draw_button(DISPLAY)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()
                
                if event.type == pygame.MOUSEMOTION:
                    
                    for n in card_buttons:
                        if n.isOver(pygame.mouse.get_pos()):
                            n.colour = (240,240,240)
                        else:
                            n.colour = (255,255,255)
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for n in card_buttons:
                        if n.isOver(pygame.mouse.get_pos()):
                            self.selected_card = n.plain_text
                            button_pressed = True


    def player_look(self, DISPLAY, server, black_card, player_picks):
        self.selected_card = None
        button_pressed = False
        card_buttons = []
        xpos = 75

        black_button = button((0,0,0), 300, 400, (xpos, (1080/2) - 200), black_card, (255,255,255), 20,28, False)
        xpos += 350

        for pick in player_picks:
            card_buttons.append(button((255,255,255), 200, 300, (xpos,(1080/2) - 150), pick, (0,0,0), 15, 28, False))
            xpos += 250
        
        while not button_pressed:
            DISPLAY.fill(self.bgcolour)
            black_button.draw_button(DISPLAY)
            for n in card_buttons:
                n.draw_button(DISPLAY)
            
            
            pygame.display.update()
            msg = server.recv() 
            print(msg) 
                
            for n in card_buttons:
                if n.plain_text == msg:
                    n.colour = (0,200,0)
                    pygame.display.update()
                    time.sleep(3)
                    button_pressed = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()
                
                if event.type == pygame.MOUSEMOTION:
                    
                    '''for n in card_buttons:
                        if n.isOver(pygame.mouse.get_pos()):
                            n.colour = (240,240,240)
                        else:
                            n.colour = (255,255,255)'''
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for n in card_buttons:
                        if n.isOver(pygame.mouse.get_pos()):
                            self.selected_card = n.plain_text
                            #button_pressed = True


