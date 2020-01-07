import pygame
import textwrap
pygame.font.init()


class button():
    def __init__(self, colour, width, height, pos, text='', text_col=(0,0,0), font_size=30, wrapping=0, center=True):
        arial = pygame.font.SysFont('Arial', font_size)
        self.colour = colour
        self.height = height
        self.width = width
        self.pos = pos
        self.wrapping =False
        self.center = center
        self.plain_text = text
        if wrapping:
            self.text = []
            wrapped = textwrap.wrap(text, wrapping)
            for n in wrapped:
                self.text.append(arial.render(n, True, text_col))
            self.wrapping = True
        else:
            self.text = arial.render(text, True, text_col)

    def draw_button(self, DISPLAY):
        pygame.draw.rect(DISPLAY, self.colour, (self.pos[0], self.pos[1], self.width, self.height))

        if self.center:
            ypos = self.pos[1] + ((self.height/2) - (self.text.get_height()/2))
        else:
            ypos = self.pos[1] + 15

        if not self.wrapping:
            DISPLAY.blit(self.text, (self.pos[0] + ((self.width/2) - (self.text.get_width()/2)), ypos))
        else:
            for n in self.text:
                DISPLAY.blit(n, (self.pos[0] + ((self.width/2) - (n.get_width()/2)), ypos))
                ypos += 20
    
    def isOver(self, mouse_pos):
            if self.pos[0] < mouse_pos[0] and mouse_pos[0] < (self.pos[0] + self.width):
                if self.pos[1] < mouse_pos[1] and mouse_pos[1] < (self.pos[1] + self.height):
                    return True

            return False 
