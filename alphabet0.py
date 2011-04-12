import pygame
import string
from a_global import *

def main():
    global font_size
    global frame_rate
    pygame.init()
    pygame.display.set_caption("Alphabet 0")
    clock = pygame.time.Clock()
    playing = True
    my_Alphabet = Alphabet()
    while playing:
        clock.tick(frame_rate)
        playing = my_Alphabet.handle_events()
        my_Alphabet.update()
        my_Alphabet.draw()


class Alphabet(object):
    def __init__(self):
        global letter_change_freq
        global frame_rate
        global font_size
        global font_color
        global letter_velocity
        global cos_dict
        global sin_dict
        self.velocity = {'speed':letter_velocity, 'direction':45}
        self.background = pygame.Surface(screen_size)
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.my_font = pygame.font.Font(None, font_size)
        self.playing = True
        self.letter_list_uc = ["A", "B", "C", "D", "E", "F", "G", "H", "I"\
            , "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"\
            , "V", "W", "X", "Y", "Z"]
        self.letter_list_lc = []
        self.temp_counter =0
        for i in self.letter_list_uc:
            temp_string_lc = string.lower(i)
            temp_string_uc = self.letter_list_uc[self.temp_counter]
            self.letter_list_lc.append(self.my_font.render(temp_string_lc, 1,\
                font_color))
#            self.letter_list_lc[self.temp_counter] = \
#                self.my_font.render(temp_string_lc, 1, font_color)
            self.letter_list_uc[self.temp_counter] = \
                self.my_font.render(temp_string_uc, 1, font_color)
            self.temp_counter += 1
        self.letter_list = [self.letter_list_uc, self.letter_list_lc]
        self.current_letter = 0     #index of the current letter
        self.current_caps = 0       # 0 = uppercase, 1 = lowercase
        self.letter_counter = 0     #used for animating from letter to letter
        self.letter_rect = self.create_rect()
    def update(self):
        if self.letter_counter >= (frame_rate * letter_change_freq):
            self.letter_counter = 0
            self.current_letter += 1
            if self.current_letter >= len(self.letter_list_uc):
                self.current_letter = 0
#        print("counter and letter = ", self.letter_counter, self.current_letter)
        self.letter_counter += 1
        self.check_bounds()
        dx = self.velocity['speed'] * cos_dict[self.velocity['direction']]
        dy = self.velocity['speed'] * sin_dict[self.velocity['direction']]
        self.letter_rect = self.letter_rect.move(dx, dy)
    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if self.current_caps == 0:      #this is the logical
                        self.current_caps = 1       #XOR operation on 
                    elif self.current_caps == 1:    #the current_caps flag
                        self.current_caps = 0       #variable (0 or 1)
        return self.playing

    def draw(self):
        screen.blit(self.background, (0,0))
        screen.blit(self.letter_list[self.current_caps][self.current_letter],\
            (self.letter_rect))
        pygame.display.flip()

    def create_rect(self):
        """this is needed to store one big rectangle for each letter surface
        that can contain the largest capital letter and the lowest lowercase letter.
        For example W or X and q or g
        """
        size_W = self.my_font.size("W")
        size_g = self.my_font.size("g")
        width = size_W[0]
        if size_W[1] >= size_g[1]:
            height = size_W[1]
        else:
            height = size_g[1]
        return pygame.Rect((0, 0), (width, height))

    def check_bounds(self):
        """this will simply check the bounds and bounce the object around the
        screen.
        """
        letter_rect = self.letter_rect
        screen_rect = screen.get_rect()
        screen_left = screen_rect.left
        screen_right = screen_rect.right
        screen_top = screen_rect.top
        screen_bottom = screen_rect.bottom
#        print("screen rect tblr = ", screen_top, screen_bottom, screen_left, screen_right)
 #       print("letter rect tblr = ", letter_rect.top, letter_rect.bottom, letter_rect.left, letter_rect.right)
        print("direction = ", self.velocity['direction'])
        if (letter_rect.bottom >= screen_bottom) or \
            (letter_rect.top <= screen_top):
            self.velocity['direction'] = -self.velocity['direction']
        if (letter_rect.left <= screen_left) or \
            (letter_rect.right >= screen_right):
            if self.velocity['direction'] == 135 or \
                self.velocity['direction'] == 315:
                self.velocity['direction'] -= 90
            else:
                self.velocity['direction'] += 90
        if self.velocity['direction'] >= 360:
            self.velocity['direction'] -= 360
        if self.velocity['direction'] < 0:
            self.velocity['direction'] += 360


if __name__ == "__main__":
    main()
