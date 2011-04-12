import pygame
import sys
from math import sqrt

font_size = 300
frame_rate = 30
screen_size = (800, 600)
letter_change_freq = 2  #number of seconds until next letter displayed
screen = pygame.display.set_mode(screen_size)
font_color = (255, 255, 255)
letter_velocity = 6   #in pixels per frame
cos_dict = {0:1, 45:sqrt(2)/2, 90:0, 135:-sqrt(2)/2, 180:-1, 225:-sqrt(2)/2, \
    270:0, 315:sqrt(2)/2}
sin_dict = {0:0, 45:sqrt(2)/2, 90:1, 135:sqrt(2)/2, 180:0, 225:-sqrt(2)/2, \
    270:-1, 315:-sqrt(2)/2}

