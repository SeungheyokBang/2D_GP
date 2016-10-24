from pico2d import *
import json



class Map_1:

    def __init__(self):

        self.image = load_image('stage_1_map.png')

    def draw(self):

        self.image.clip_draw(0 , 0, 800, 700, 400, 300)