import random
import json
import os
import Marco_Char

from pico2d import *
import Background

import game_framework
import title_state

name = "MainState"

def enter():

    global marco_body,marco_leg,bg_1

    marco_body = Marco_Char.Marco_body()
    marco_leg = Marco_Char.Marco_Leg()
    bg_1 = Background.BG_1()

def exit():

    global marco_body,marco_leg,bg_1
    del(marco_body)
    del(bg_1)
    del(marco_leg)

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
            marco_body.handle_events(event)
            marco_leg.handle_events(event)


def update():
    marco_body.update()
    marco_leg.update()

def draw():
    clear_canvas()
    bg_1.draw()
    marco_body.draw()
    marco_leg.draw()
    update_canvas()

