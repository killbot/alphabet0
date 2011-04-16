import pygame
import sys
from math import sqrt

font_size = 300
frame_rate = 30
display_flags = 0
#display_flags = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN
screen_size = (1024, 768)
letter_change_freq = 2  #number of seconds until next letter displayed
screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
font_color = (255, 255, 255)
font_outline = (1, 1, 1)
letter_velocity = 6   #in pixels per frame
cos_dict = {0:1, 45:sqrt(2)/2, 90:0, 135:-sqrt(2)/2, 180:-1, 225:-sqrt(2)/2, \
    270:0, 315:sqrt(2)/2}
sin_dict = {0:0, 45:sqrt(2)/2, 90:1, 135:sqrt(2)/2, 180:0, 225:-sqrt(2)/2, \
    270:-1, 315:-sqrt(2)/2}

def textHollow(font, message, fontcolor):
    notcolor = [c^0xFF for c in fontcolor]
    base = font.render(message, 0, fontcolor, notcolor)
    size = base.get_width() + 6, base.get_height() + 6
    img = pygame.Surface(size, 16)
    img.fill(notcolor)
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (6, 0))
    img.blit(base, (0, 6))
    img.blit(base, (6, 6))
    base.set_colorkey(0)
    base.set_palette_at(1, notcolor)
    img.blit(base, (1, 1))
    img.set_colorkey(notcolor)
    return img

def textOutline(font, message, fontcolor, outlinecolor):
    base = font.render(message, 0, fontcolor)
    outline = textHollow(font, message, outlinecolor)
    img = pygame.Surface(outline.get_size(), 16)
    img.blit(base, (1, 1))
    img.blit(outline, (0, 0))
    img.set_colorkey(0)
    return img
