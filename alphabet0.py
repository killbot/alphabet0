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
        self.my_font = pygame.font.Font(None, font_size)
        self.playing = True
        self.letter_list_uc = ["A", "B", "C", "D", "E", "F", "G", "H", "I"\
            , "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"\
            , "V", "W", "X", "Y", "Z"]
        self.letter_list_lc = []
        self.temp_counter =0
        for i in self.letter_list_uc:
            temp_string = string.lower(i)
            self.letter_list_lc[self.temp_counter] = \
                self.my_font.render(temp_string, 1, font_color)
            self.letter_
            self.temp_counter += 1
        self.letter_list = [self.letter_list_uc, self.letter_list_lc]
        self.current_letter = 0     #index of the current letter
        self.current_caps = 0       # 0 = uppercase, 1 = lowercase
        self.letter_counter = 0
    def update(self):
        if self.letter_counter >= frame_rate * letter_change_freq:
            self.letter_counter = 0

    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

        return self.playing

    def draw(self):
        pass



if __name__ == "__main__":
    main()
