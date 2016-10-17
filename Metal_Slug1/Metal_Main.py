import random
import json
import os

from pico2d import *
from Stage_1 import *

import game_framework
import title_state

name = "MainState"


class Marco:


    global left, right, up, down
    global Move_stop
    global Move_left
    global Move_right
    global Move_down
    global Move_up

    left = False
    right = False
    up = False
    down = False

    Move_stop = 0

    Move_left= 0
    Move_right= 0
    Move_down= 0
    Move_up= 0


    def __init__(self):

        self.x, self.y = 50, 170
        self.frame = 0
        self.state_run = load_image('Move_Run.png')
        self.state_up=load_image('Act_IdleLookup.png')
        self.state_down =load_image('Act_SitDown.png')
        self.state_stop = load_image('Move_Stop.png')




    def handle_events(self, event):

        global left, right, up, down
        global Move_stop

        Move_stop = 'stop'

        print("KeyInput")

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            left = True


        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            right = True
            self.Move_right = 'right'
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            up = True
            self.Move_up = 'up'
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            down = True
            self.Move_down = 'down'
        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            left = False
            self.Move_left = 'left'
        if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            right = False
        if (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            up = False
        if (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            down = False

    def update(self):

        self.frame = (self.frame + 1)

        if right == True:
            self.x = self.x + 1

        if left == True:
            self.x = self.x - 1

        if up == True:
            self.y = self.y + 0

        if down == True:
            self.y = self.y - 0

        if self.frame > 11:
            self.frame = 0

    def draw(self):

        self.state_stop.clip_draw(self.frame * 125,  150, 125, 150, self.x, self.y)

        if right == True:
            self.state_run.clip_draw(self.frame *110,  150, 110, 150, self.x, self.y)
        elif left == True:
            self.state_run.clip_draw(self.frame * 110, 0, 110, 150, self.x, self.y)
        elif up == True:
            self.state_up.clip_draw(self.frame * 123,  150, 123, 150, self.x, self.y)
        elif down == True:
            self.state_down.clip_draw(self.frame * 186, 150, 186, 150, self.x, self.y)


def enter():

    global boy,grass

    boy = Marco()
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
            boy.handle_events(event)

def update():

    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

    delay(0.0001)