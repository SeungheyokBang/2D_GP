
from pico2d import *
fTime = 0.1
AddValue = 0
class Rebel:

     image=None

     def __init__(self) :
        self.x, self.y = 700, 100
        self.idle = load_image('REBEL_IDLE.png')
        self.attack = load_image('REBEL_SHOOT.png')
        self.run = load_image('REBEL_RUN.png')
        self.die = load_image('REBEL_die.png')

        self.frame = 0
        self.idle_frame = 0
        self.atk_frame = 0

        self.time =0
        self.w = 90
        self.h = 180

        self.state = 'idle'
        self.alive = 'true'

     def update(self) :
         global AddValue

         AddValue += fTime

         if (AddValue > 1):
             AddValue = 0
             self.frame += 1
             if (self.frame > 6):
                 self.frame = 0




     #  self.atk_frame = (self.atk_frame + 1 ) % 10
     #   self.frame = (self.frame + 1 ) % 11

     def draw(self) :
        if self.state == 'idle':
            self.idle.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

        if self.state == 'attack':
           self.attack.clip_draw(self.frame * 200, 200, 100, 100, self.x, self.y)
        if self.state == 'die' and self.alive == 'true':
            self.die.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
            self.alive = 'false'
        if self.state == 'run':
            self.run.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

     def get_bb(self):
        return self.x - 12.5, self.y - 12.5, self.x + 12.5, self.y + 12.5

       # def get_bb(self):
        #    if self.alive == 'true':
         #       return self.x - self.w / 2, self.y + 36 - self.h / 2, self.x + self.w / 2, self.y + 36 + self.h / 2
          #  else:
 #          3     return self.x, self.y, self.x, self.y

#        def draw_bb(self):
 #           if self.alive == 'true':
  #              draw_rectangle(*self.get_bb())






