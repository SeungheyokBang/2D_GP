from pico2d import *

class BG_1:
    def __init__(self):
        self.x = 0
        self.image = load_image('stage_1.png')
    def draw(self):
        self.image.clip_draw(self.x,0,350,300,512,384,1024,800 )