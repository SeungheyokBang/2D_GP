
from pico2d import *

class Rebel:

     image=None

     def __init__(self) :
        self.x, self.y = 500, 150
        self.idle = load_image('asd.png')
     #   self.attack = load_image('Swordsman_atk.png')
     #  self.run = load_image('Swordsman_run.png')
     # self.die = load_image('Swordsman_die.png')

        self.frame = 0
        self.idle_frame = 0
        self.atk_frame = 0

        self.time =0
        self.w = 90
        self.h = 180

        self.state = 'idle'
        self.alive = 'true'

     def update(self) :
        self.idle_frame = (self.idle_frame + 1 ) % 5
    #    self.atk_frame = (self.atk_frame + 1 ) % 10
     #   self.frame = (self.frame + 1 ) % 11

     def draw(self) :
        if self.state == 'idle':
            self.idle.clip_draw(self.idle_frame * 100,100, 100, 100, self.x, self.y)
            #delay(0.02)




        pass
        #if self.state == 'attack':
        #    self.attack.clip_draw(self.atk_frame * 200, 219, 200, 219, self.x, self.y)
        #if self.state == 'die' and self.alive == 'true':
        #    self.die.clip_draw(self.frame * 180, 194, 180, 194, self.x, self.y)
        #    self.alive = 'false'
        #if self.state == 'run':
        #    self.run.clip_draw(self.frame * 180, 191, 180, 191, self.x, self.y)
     #def get_bb(self):
     #   if self.alive == 'true':
     #       return self.x - self.w/2, self.y+36 - self.h/2, self.x + self.w/2, self.y+36 + self.h/2
     #   else:
     #           return self.x , self.y, self.x, self.y
     #def draw_bb(self):
     #   if self.alive == 'true':
     #       draw_rectangle(*self.get_bb())


