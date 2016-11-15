import random
import json
import os
from Bullet import shot
import Rebel_Soldie_Char
import Background

from pico2d import *

Left, Right, Up = 0, 1, 2
Stand, Run, Shot, Jump, Swing, MovingJump,Sit = 0, 1, 2, 3, 4, 5,6
fTime = 0.1
AddValue = 0
Debug = 0

bulletContainer = []
Rebel = None
Map = None

Scr = 0

class Marco_body():
    def __init__(self):
        global Rebel, Map
        AAA = 0
        Map = Background.BG()
        Rebel = Rebel_Soldie_Char.Rebel()
        self.x, self.y = 100, 110
        self.frame, self.shot = 0, 0
        self.peak = 0
        self.swing = 0
        self.image = load_image('Marco_shot_Motion_R.png')
        self.state = 0;
        self.ScrollX = 0;




    def Move(self, Key, Direct, state):
        global Debug
        self.Direct = Direct

        if self.state == state:
            Debug = 0;
        else:
            if self.state == Shot:
                Debug = 0;
            else:
                self.state = state;
                self.frame = 0;

        if self.Direct == Right:
            if self.state == Swing:
                self.image = load_image('Macro_Swing_Motion_R.png')
            elif self.state == Jump:
                self.image = load_image('Marco_Jump_R.png')
            elif self.state == Sit:
                self.image = load_image('Marco_앉기_Motion_R.png')


            else:
                self.image = load_image('Marco_shot_Motion_R.png')

        elif self.Direct == Left:
            self.image = load_image('Marco_shot_Motion_L.png')

        if Key == Right:
             self.x += 30 * fTime;
                # 이동 속도는 10으로 한다 일단

        elif Key == Left:
                self.x -= 30 * fTime;

    # 왼쪽으로 가는 길이를 제한 한다.
        elif Key == Up:
            self.y += 5
            ###########공격##################3

        if self.state == Shot:
            self.shot = (self.shot + 1)
        if self.state == Swing:
            self.swing = (self.swing + 1)

    def update(self):
        global AddValue, Rebel, Scr, Map

        #Scr = self.x - 800 / 2.0;

        if Scr < 0 :
            Scr = 0

        if Scr > 1950:
            Scr = 1950

        Map.scroll(Scr);

        AddValue += fTime;

        if(self.state == Shot):
            if (AddValue > 0.5):
                AddValue = 0
                self.frame += 1;
                if(self.frame == 3):
                    bulletContainer.append(shot(self.x, self.y, self.Direct));
                if (self.frame > 10):
                    self.frame = 0;
                    self.state = Stand;

        else:
            if(AddValue > 1):
                AddValue = 0
                self.frame += 1;
                if(self.frame > 9):
                    self.frame = 0;

        for bullet in bulletContainer:
            bullet.update()
            if collide(bullet, Rebel):
                bulletContainer.remove(bullet)

    def get_bb(self):
        return self.x - 12.5, self.y - 12.5, self.x + 12.5, self.y + 12.5


    def draw(self):
        global Scr
        if self.state == Stand:
            if self.Direct == Right:
                self.image.clip_draw(56 * self.frame, 30 * self.state, 56, 30, self.x - Scr, self.y, 110, 90)

            elif self.Direct == Left:
                self.image.clip_draw(560 - (56 * (self.frame + 1)), 30 * self.state, 56, 30, self.x - 56, self.y, 110, 90)


        elif self.state == Run:
            if self.Direct == Right:
                self.image.clip_draw(56 * self.frame, 30 * self.state, 56, 30, self.x - Scr, self.y, 110, 90)
            elif self.Direct == Left:
                self.image.clip_draw(560 - (56 * (self.frame + 1)), 30 * self.state, 56, 30, self.x - 56, self.y, 110,90)
        elif self.state == Shot:
            if self.Direct == Right:
                self.image.clip_draw(56 * self.frame , 30 * self.state, 56, 30, self.x - 10, self.y + 3, 110, 90)
            elif self.Direct == Left:
                self.image.clip_draw(560 - (56 * (self.frame )), 30 * self.state, 56, 30, self.x - 56 + 10, self.y + 3, 110, 90)

        for bullet in bulletContainer:
            bullet.draw()






def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True



class Marco_Leg():
    def __init__(self):
        self.x, self.y, self.frame = 85, 65, 0
        self.image = load_image('Marco_Leg_R.png')
        self.state = 0;

    def Move(self, key, direction, state):
        self.direction = direction
        if self.state == state:
            Debug = 0;
        else:
            self.state = state;
            self.frame = 0;

        if self.direction == Right:
            self.image = load_image('Marco_Leg_R.png')
        elif self.direction == Left:
            self.image = load_image('Marco_Leg_L.png')
        if key == Right:
                self.x += 30 * fTime;
        if key == Left:
                self.x -= 30 * fTime;
        elif key == Up:
            self.y += 5

    def update(self):
        global AddValue

        AddValue += fTime;
        if(AddValue > 1):
            AddValue = 0
            self.frame += 1;
            if(self.frame > 9):
                self.frame = 0;

    def draw(self):
        if self.state == Stand:
            if self.direction == Right:
                self.image.clip_draw(56 * self.frame, 25 * self.state, 56, 25, self.x, self.y, 80, 50)
                print(self.frame);
            elif self.direction == Left:
                self.image.clip_draw(560 - (56 * (self.frame + 1)), 25 * self.state, 56, 25, self.x - 25, self.y, 80, 50)
        elif self.state == Run:
            if self.direction == Right:
                self.image.clip_draw(56 * self.frame, 25 * self.state, 56, 25, self.x + 3, self.y, 80, 70)
            elif self.direction == Left:
                self.image.clip_draw(560 - (56 * (self.frame)), 25 * self.state, 56, 25, self.x - 25 - 3, self.y, 80, 70)

        elif self.state == Shot:
            if self.direction == Right:
                self.image.clip_draw(56 * self.frame, 0, 56, 25, self.x, self.y, 80, 50)
                print(self.frame);
            elif self.direction == Left:
                self.image.clip_draw(560 - (56 * (self.frame + 1)), 0, 56, 25, self.x - 25, self.y, 80, 50)
