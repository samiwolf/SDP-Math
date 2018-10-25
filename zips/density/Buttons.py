# -*- coding: cp1252 -*-
#/usr/bin/env python
'''
Simon H. Larsen
Buttons
Project startet: d. 26. august 2012
'''
import pygame
pygame.init()
class Button:
    def create_image_button(self, surface, x,y, image):
        length = surface.get_size()[0]
        height = surface.get_size()[1] 
        self.rect = pygame.Rect(x,y, length,height)
        self.invisible = False
        surface = self.draw_image(surface, image, x,y)
        return surface
    
    def create_invis_button(self, surface, x,y, length,height):
        self.rect = pygame.Rect(x,y, length,height)
        self.invisible = True
        self.click_effect(x,y, length,height, surface)
        return surface
            
    def create_button(self, surface, color, x, y, length, height, width, text, text_color, font_size):
        self.invisible = False
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y, font_size)
        self.rect = pygame.Rect(x,y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y, font_size):
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):           
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)  
        return surface
    
    def draw_image(self, surface, image, x,y):
        surface.blit(image, (x,y))
        return surface

    def click_effect(self, x,y, length,height, surface):
        try:
            if self.pres:
                if self.invisible:
                    s = pygame.Surface((length+4,height))
                    s.fill((166,166,166))
                    pygame.draw.rect(s, (0,0,150), (0,0,length+4,height), 2)
                    s.set_alpha(70)
                    surface.blit(s, (x-3,y-2))
                    self.pres = False
                    return surface
                else:
                    pass
        except:
            self.pres = False

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print "Some button was pressed!"
                        self.pres = True
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False
