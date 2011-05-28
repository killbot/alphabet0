import os
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
        global font_outline
        global letter_velocity
        global cos_dict
        global sin_dict
        self.background_color = [90, 90, 90]
        self.background_direction = [1, 1, 1]
        self.velocity = {'speed':letter_velocity, 'direction':45}
        self.background = pygame.Surface(screen_size)
        self.background = self.background.convert()
        self.background.fill(self.background_color)
        self.my_font = pygame.font.Font(None, font_size)
        self.escape_font = pygame.font.Font(None, 24)
        self.playing = True
        self.letter_list_uc = ["A", "B", "C", "D", "E", "F", "G", "H", "I"\
            , "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"\
            , "V", "W", "X", "Y", "Z"]
        self.letter_list_lc = []
        self.temp_counter =0
        for i in self.letter_list_uc:
            temp_string_lc = string.lower(i)
            temp_string_uc = self.letter_list_uc[self.temp_counter]
            self.letter_list_lc.append(textOutline(self.my_font, temp_string_lc, font_color, font_outline))
#            self.letter_list_lc.append(self.my_font.render(temp_string_lc, 1,\
#                font_color))
#            self.letter_list_lc[self.temp_counter] = \
#                self.my_font.render(temp_string_lc, 1, font_color)
#            self.letter_list_uc[self.temp_counter] = \
#                self.my_font.render(temp_string_uc, 1, font_color)
            self.letter_list_uc[self.temp_counter] = textOutline(self.my_font, temp_string_uc, font_color, font_outline)
            self.temp_counter += 1
        self.letter_list = [self.letter_list_uc, self.letter_list_lc]
        self.current_letter = 0     #index of the current letter
        self.current_caps = 0       # 0 = uppercase, 1 = lowercase
        self.letter_counter = 0     #used for animating from letter to letter
        self.letter_rect = self.create_rect()
        self.escape_message = self.escape_font.render("Press L-Shift, R-shift, and S to quit", 1, (0,0,0))
        self.escape_rect = self.escape_message.get_rect()
        self.escape_rect.bottomleft = (0, screen_size[1])
        self.load_music("miab-soundtrack.ogg")
        pygame.mixer.music.play(-1)

    def update(self):
        if self.letter_counter >= (frame_rate * letter_change_freq):
            self.letter_counter = 0
            self.current_letter += 1
            if self.current_letter >= len(self.letter_list_uc):
                self.current_letter = 0
        self.letter_counter += 1
        self.check_bounds()
        dx = self.velocity['speed'] * cos_dict[self.velocity['direction']]
        dy = self.velocity['speed'] * sin_dict[self.velocity['direction']]
        self.letter_rect = self.letter_rect.move(dx, dy)
        self.change_background_color()

    def handle_events(self):
        mods = pygame.key.get_mods()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.current_caps = self.current_caps^1
                if event.key == pygame.K_s and \
                    mods & pygame.KMOD_RSHIFT and \
                    mods & pygame.KMOD_LSHIFT:
                    self.playing = False
        return self.playing

    def draw(self):
             
        screen.blit(self.background, (0,0))
        screen.blit(self.letter_list[self.current_caps][self.current_letter],\
            (self.letter_rect))
        screen.blit(self.escape_message, self.escape_rect)
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

    def change_background_color(self):            
        for i in range(len(self.background_color)):
            self.background_color[i] += (i + 1) * self.background_direction[i]
            if self.background_color[i] > 255:
                self.background_color[i] = 255
                self.background_direction[i] *= -1  #switch color direction
            elif self.background_color[i] < 0:
                self.background_color[i] = 0
                self.background_direction[i] *=-1   #switch color direction
        self.background.fill(self.background_color)

    def load_music(self, song_name):
        fullname = os.path.join('Soundtrack', song_name)
        pygame.mixer.music.load(fullname)

if __name__ == "__main__":
    main()
