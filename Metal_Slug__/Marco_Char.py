import random
import json
import os
from pico2d import *

Left,Right, Up = 0,1,2
Stand, Run, Shot, Jump, Swing , MovingJump = 0,1,2,3,4,5

class Marco_body():
    def __init__(self):
        self.x, self.y = 100,150
        self.frame ,self.shot = 0,0
        self.peak = 0
        self.swing = 0
        self.image = load_image('Marco_shot_Motion_R.png')

    def Move(self,Key, Direct,state):
        self.Direct=Direct

        self.state = state
        if self.Direct == Right:
            if self.state == Swing:
                self.image= load_image('Macro_Swing_Motion_R.png')
            elif self.state == Jump:
                self.image = load_image('Marco_Jump_R.png')
            else:
                self.image = load_image('Macro_shot_Motion_R.png')
            if Key == Right:
                self.x += 10
                #이동 속도는 10으로 한다 일단
                self.frame = (self.frame + 1) % 10
            elif Key  == Left:
                if self.x > 20:
                    # 왼쪽으로 가는 길이를 제한 한다.
                    self.x -= 10
                self.frame = (self.frame + 1) % 10
            elif Key == Up:
                self.y += 5
                self.frame = (self.frame + 1) % 10
            ###########공격##################3

            if self.state == Shot:
                self.shot = (self.shot + 1)
            if self.state == Swing:
                self.swing = (self.swing + 1)

    def update(self):
        if self.state == Stand:
            self.frame = (self.frame + 1) %10

    
    def draw(self):
        if self.state == Stand:
            if self.Direct == Right:
                self.image.clip_draw(56 * self.frame, 30*self.state, 56, 30, self.x, self.y,110,90)
            elif self.Direct == Left:
                self.image.clip_draw(560-(56 * (self.frame+1)), 30*self.state, 56, 30, self.x-56, self.y,110,90)
        elif self.state == Run:
            if self.Direct == Right:
                self.image.clip_draw(56 * self.frame, 30*self.state, 56, 30, self.x, self.y,110,90)
            elif self.Direct == Left:
                self.image.clip_draw(560-(56 * (self.frame+1)), 30*self.state, 56, 30, self.x-56, self.y,110,90)
        elif self.state == Shot:
            if self.Direct == Right:
                self.image.clip_draw(56 * self.shot, 30*self.state, 56, 30, self.x-10, self.y+3,110,90)
            elif self.Direct == Left:
                self.image.clip_draw(560-(56 * (self.shot+1)), 30*self.state, 56, 30, self.x-56+10, self.y+3,110,90)
        elif self.state == Swing:
            if self.Direct == Right:
                self.image.clip_draw(56 * self.swing, 0, 56, 50, self.x-25, self.y+10,120,120)
            elif self.Direct == Left:
                self.image.clip_draw(560-(56 * (self.frame+1)), 0, 56, 30, self.x-56, self.y,110,90)
        elif self.state == Jump:
            if self.Direct == Right:
                self.image.clip_draw(56 * self.frame, 0, 56, 40, self.x, self.y,110,90)
            elif self.Direct == Left:
                self.image.clip_draw(560-(56 * (self.frame+1)), 0, 56, 40, self.x-56, self.y,110,90)


class Marco_Leg():
    def __init__(self):
        self.x, self.y, self.frame = 85, 105 ,0
        self.image = load_image('Marco_Leg_R.png')

    def move(self, key,direction,state):
        self.direction = direction
        self.state = state
        if self.direction == Right:
            self.image = load_image('Marco_Leg_R.png')

        elif self.direction == Left:
            self.image = load_image('Marco_Leg_L.png')
        if key == Right:
            self.x +=10
            self.frame = (self.frame + 1 ) % 10
        if key == Left:
            if self.x > 20:
                self.x -= 10
            self.frame = (self.frame + 1) % 10
        elif key == Up:
            self.y+=5
            self.frame = (self.frame +1) % 10

    def update(self):

       if self.state == Stand:
           self.frame = (self.frame + 1 ) % 10


    def draw(self):
        if self.state == Stand:
            if self.direction == Right:
                self.image.clip_draw(56 * self.frame, 25*self.state, 56, 25, self.x, self.y, 80,50)
            elif self.direction == Left:
                self.image.clip_draw(560-(56 * (self.frame+1)), 25*self.state, 56, 25, self.x-25, self.y, 80,50)
        elif self.state == Run:
            if self.direction == Right:
                self.image.clip_draw(56 * self.frame, 25*self.state, 56, 25, self.x+3, self.y, 80,70)
            elif self.direction == Left:
                self.image.clip_draw(560-(56 * (self.frame+1)), 25*self.state, 56, 25, self.x-25-3, self.y, 80,70)
        elif self.state == Jump:
            if self.direction == Right:
                self.image.clip_draw(56 * self.frame, 25*(self.state-1), 56, 25, self.x, self.y, 80,50)
            elif self.direction == Left:
                self.image.clip_draw(560-(56 * (self.frame+1)), 25*(self.state-1), 56, 25, self.x-25, self.y, 80,50)

def handle_events(self, event):

    global key
    global body_state, leg_state
    global Direct

    events = get_events()

    if event.type == SDL_KEYDOWN:
        if event.key == SDLK_RIGHT:
            Key = Right
            Direct = Right
            body_state, leg_state = Run, Run
        elif event.key == SDLK_LEFT:
            Key = Left
            Direct = Left
            body_state, leg_state = Run, Run
                    # elif event.key == SDLK_s:
                    #   body_state,leg_state = JUMP, JUMP
                    #  key = UP
                    # elif event.key == SDLK_a:
                    #    body_state = SHOT
                    # elif event.key == SDLK_a:
                    #   body_state = STAB

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                 Key = -1
                 leg_state = Stand
            elif event.key == SDLK_LEFT:
                  Key = -1
                  leg_state = Stand








