import random
import json
import os


from pico2d import *
from Stage_1 import *


import game_framework
import title_state

name = "MainState"

class Marco:


    def __init__(self):



        self.x, self.y =200, 150
        self.move_frame = 0
        self.jump_frame = 0
        self.act_frame =0
        self.shot_frame = 0

        self.direction = 'right'

        self.move_state = 'idle'
        self.jump_state = 'ready'
        self.act_state = 'ready'
        self.shot_state = 'ready'

        self.isjump = False

        self.Move_Run = load_image('Move_Run.png')
        self.Act_IdleLookUp=load_image('Act_IdleLookup.png')
        self.Act_SitDown =load_image('Act_SitDown.png')
        self.Move_Idle = load_image('Move_Stop.png')
        self.Shot_IdleShot = load_image('Shot_idleShot.png')

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:

            if event.key == SDLK_LEFT:
                    self.move_state = 'run'
                    self.direction = 'left'

                    self.act_state = 'ready'
                    self.shot_state = 'ready'
                    self.move_frame = 0
                    self.act_frame = 0
                    self.shot_frame = 0

            elif event.key == SDLK_RIGHT:
                    self.move_state = 'run'
                    self.direction = 'right'

                    self.act_state = 'ready'
                    self.shot_state = 'ready'
                    self.move_frame = 0
                    self.act_frame = 0
                    self.shot_frame = 0
            # Attack
            if event.key == SDLK_a:
                self.shot_state = 'shot'
                self.shot_frame = 0

            # Up
            if event.key == SDLK_UP:
                self.act_state = 'lookup'
                self.act_frame = 0

            # SitDown
            if event.key == SDLK_DOWN:
                self.act_state = 'sitdown'
                self.act_frame = 0

            # Jump
            if event.key == SDLK_s:
                if self.isjump == False:
                    self.jump_state = 'jump_up'
                    self.act_frame = 0
                    self.isjump = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT and self.move_state == 'run':
                self.move_state = 'idle'
                self.move_frame = 0
            elif event.key == SDLK_LEFT and self.move_state == 'run':
                self.move_state = 'idle'
                self.move_frame = 0
            elif event.key == SDLK_DOWN:
                self.move_state = 'idle'
                self.act_state = 'ready'
                self.act_frame = 0
            elif event.key == SDLK_UP:
                self.act_frame = 8

    def update(self):

            if(self.move_state in ('run','idle')):
               self.move_frame = (self.move_frame + 1) % 11


            if(self.shot_state in ('shot')):
                if self.shot_frame < 11:
                      self.shot_frame = self.shot_frame + 1
                else:
                  self.shot_state='ready'
                  self.move_frame = 0
                  self.shot_frame = 0


            if(self.act_state in ('sitdown')):
                if self.act_frame < 10:
                    self.act_frame = self.act_frame + 1
                else:
                    self.act_frame = 4
            elif(self.act_state in ('lookup')):
                if self.act_frame < 7:
                    self.act_frame = self.act_frame + 1
                elif self.act_frame == 7:
                    self.act_frame = 5
                elif self.act_frame > 7 and self.act_frame < 11:
                    self.act_frame = self.act_frame + 1
                else:
                    self.move_state = 'idle'
                    self.act_state = 'ready'
                    self.act_frame = 0


            if self.move_state == 'run':
                if self.act_state == 'ready':
                    if self.direction == 'right':
                         self.x = self.x + 1
                    elif self.direction == 'left':
                         self.x = self.x - 1
                print('x pos %d' % self.x)

            if self.jump_state == 'jump_up' and self.isjump == True:
                self.jump_frame= (self.jump_frame + 1)
                if self.jump_frame == 6:
                    self.jump_state == 'jump_down'
                else:
                    self.y = self.y + 5
                print('up jump frame %d' % self.jump_frame)


            if self.jump_state == 'jump_down' and self.isjump == True:
                self.jump_frame= (self.jump_frame - 1)
                if self.jump_frame == 0:
                    self.jump_state == 'ready'
                    self.isjump = False
                else:
                    self.y = self.y - 5
                print('down jump frame %d' % self.jump_frame)



    def draw(self):
        if self.move_state == 'idle':
            if self.shot_state == 'shot':
                if self.direction == 'right':
                    self.Shot_IdleShot.clip_draw(self.shot_frame * 142,  150, 142, 150, self.x, self.y)
                elif self.direction == 'left':
                    self.Shot_IdleShot.clip_draw((142*11) - ((self.shot_frame+1) * 142),  0, 142, 150, self.x, self.y)
            elif self.shot_state == 'ready':
                if self.act_state == 'ready':
                    if self.direction == 'right':
                        self.Move_Idle.clip_draw(self.move_frame * 125,  150, 125, 150, self.x, self.y)
                    elif self.direction == 'left':
                        self.Move_Idle.clip_draw((126*11) - ((self.move_frame+1) * 126),  0, 126, 150, self.x, self.y)
                elif self.act_state == 'sitdown':
                    if self.direction == 'right':
                        self.Act_SitDown.clip_draw(self.act_frame * 186,  150, 186, 150, self.x, self.y)
                    elif self.direction == 'left':
                        self.Act_SitDown.clip_draw((186*10) - ((self.act_frame+1) * 186),  0, 186, 150, self.x, self.y)
                elif self.act_state == 'lookup':
                    if self.direction == 'right':
                        self.Act_IdleLookUp.clip_draw(self.act_frame * 123,  150, 123, 150, self.x, self.y)
                    elif self.direction == 'left':
                        self.Act_IdleLookUp.clip_draw((123*11) - ((self.act_frame+1) * 123),  0, 123, 150, self.x, self.y)
        elif self.move_state == 'run':
            if self.act_state == 'ready':
                if self.direction == 'right':
                    self.Move_Run.clip_draw(self.move_frame * 110,  150, 110, 150, self.x, self.y)

                elif self.direction == 'left':
                    self.Move_Run.clip_draw(self.move_frame * 110,  0, 110, 150, self.x, self.y)

def enter():

    global marco,grass

    marco = Marco()
    grass = Map_1()

def exit():

    global boy,grass
    del(boy)
    del(grass)

def pause():
    pass

def resume():
    pass

def handle_events():

    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
                running = False
        else:
            marco.handle_event(event)

def update():

    marco.update()

def draw():
    clear_canvas()
    grass.draw()
    marco.draw()
    update_canvas()

