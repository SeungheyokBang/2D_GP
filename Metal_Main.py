import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

boy = None
grass = None
font = None

global X
X = 0

class Grass:

    def __init__(self):
        self.image = load_image('stage_1_map.png')

    def draw(self):

        self.image.clip_draw(0 , 0, 800, 600, 400, 300)


class Marco:

    global Index
    global State
    global Time
    global Standard

    global left, right, up, down

    left = False
    right = False
    up = False
    down = False

    Index = 0
    State = 0
    Frame = 0
    Standard = 100

    def __init__(self):
        self.x, self.y = 30, 100
        self.frame = 0
        self.image = load_image('Untitled-2.png')
        self.dir = 1

    def handle_events(self, event):

        global right
        global x

        x = 0

        print("KeyInput")

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            right = True

        if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            right = False

        print("Event")

        #if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
        #  left = True
        #if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
        #   right = True
        #if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
         #   up = True
        #if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
         #   down = True
        #if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
         #   left = False

        #if (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
         #   up = False
        #if (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
         #   down = False

    def update(self):

        self.frame = (self.frame + 1)

        #Marco.right = True
        if right == True:
            self.x = self.x + 2

        if self.frame > 10:
            self.frame = 0

    def draw(self):
        self.image.clip_draw(100 * self.frame, 0, 100, 100, self.x, self.y)

def enter():
    global boy,grass
    boy = Marco()
    grass = Grass()

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
        else :
            boy.handle_events(event)

def update():

    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()