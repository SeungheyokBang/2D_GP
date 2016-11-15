from pico2d import *

import Marco_Char

Char = None
Scr = 0

class BG:
    def __init__(self):
        global Char
        self.x = 0
        self.cx = 800
        self.image = load_image('stage_1_1.png')
        self.ScrollX = 0;


    def scroll(self, x):
        global Scr
        Scr = x;

    def draw(self):
        global Scr
        print(int(self.x + Scr));
        print(int(self.cx + Scr));

        self.image.clip_draw(int(self.x + Scr), 0, int(self.cx + Scr) , 600,400, 300, 800 , 600 ) # // 센터 x, y
        #self.image.clip_draw(1266, 0, 2066, 600, 400, 300, 800, 600)  # // 센터 x, y