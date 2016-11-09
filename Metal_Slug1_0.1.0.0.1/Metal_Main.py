from pico2d import *
from Bcakground import *

LEFT,RIGHT, UP = 0,1,2
STAND, RUN, SHOT, JUMP, STAB, SWING,MOVEJUMP = 0,1,2,3,4,5,6


class Character_body():
    def __init__(self):
        self.x, self.y, self.frame, self.shot, self.stab, self.swing = 100,150,0, 0,0,0
        self.image = load_image('CHAR_body_S_R_S.png')

    def move(self, key,direction,state):
        self.direction = direction
        self.state = state
        if self.direction == RIGHT:
            if self.state == STAB:
                self.image = load_image('CHAR_body_stab.png')
            elif self.state == SWING:
                self.image = load_image('CHAR_body_swing.png')
            elif self.state == JUMP:
                self.image = load_image('CHAR_body_jump.png')
            else:
                self.image = load_image('CHAR_body_S_R_S.png')
        elif self.direction == LEFT:
            self.image = load_image('CHAR_body_S_R_S_re.png')
        if key == RIGHT:
            if self.x <400:
                self.x += 10
            self.frame = (self.frame + 1) % 10
        elif key == LEFT:
            if self.x > 55:
                self.x -= 10
            self.frame = (self.frame + 1) % 10
        elif key == UP:
            self.y += 5
            self.frame = (self.frame + 1) % 10
        if self.state == SHOT:
            self.shot = (self.shot + 1)
        if self.state == STAB:
            self.stab = (self.stab + 1)
        if self.state == SWING:
            self.swing = (self.swing + 1)

    def update(self):
        if self.state == STAND:
            self.frame = (self.frame + 1 ) % 10

    def draw(self):
        if self.state == STAND:
            if self.direction == RIGHT:
                self.image.clip_draw(56 * self.frame, 30*self.state, 56, 30, self.x, self.y,110,90)
            elif self.direction == LEFT:
                self.image.clip_draw(560-(56 * (self.frame+1)), 30*self.state, 56, 30, self.x-56, self.y,110,90)
        elif self.state == RUN:
            if self.direction == RIGHT:
                self.image.clip_draw(56 * self.frame, 30*self.state, 56, 30, self.x, self.y,110,90)
            elif self.direction == LEFT:
                self.image.clip_draw(560-(56 * (self.frame+1)), 30*self.state, 56, 30, self.x-56, self.y,110,90)
        elif self.state == SHOT:
            if self.direction == RIGHT:
                self.image.clip_draw(56 * self.shot, 30*self.state, 56, 30, self.x-10, self.y+3,110,90)
            elif self.direction == LEFT:
                self.image.clip_draw(560-(56 * (self.shot+1)), 30*self.state, 56, 30, self.x-56+10, self.y+3,110,90)
        elif self.state == STAB:
            if self.direction == RIGHT:
                self.image.clip_draw(56 * self.stab, 0, 56, 35, self.x, self.y,110,90)
            elif self.direction == LEFT:
                self.image.clip_draw(560-(56 * (self.frame+1)), 0, 56, 30, self.x-56, self.y,110,90)
        elif self.state == SWING:
            if self.direction == RIGHT:
                self.image.clip_draw(56 * self.swing, 0, 56, 50, self.x-25, self.y+10,120,120)
            elif self.direction == LEFT:
                self.image.clip_draw(560-(56 * (self.frame+1)), 0, 56, 30, self.x-56, self.y,110,90)
        elif self.state == JUMP:
            if self.direction == RIGHT:
                self.image.clip_draw(56 * self.frame, 0, 56, 40, self.x, self.y,110,90)
            elif self.direction == LEFT:
                self.image.clip_draw(560-(56 * (self.frame+1)), 0, 56, 40, self.x-56, self.y,110,90)

class Character_leg():
    def __init__(self):
        self.x, self.y, self.frame = 85, 105 ,0
        self.image = load_image('CHAR_leg_S_R_J_M.png')

    def move(self, key,direction,state):
        self.direction = direction
        self.state = state
        if self.direction == RIGHT:
            self.image = load_image('CHAR_leg_S_R_J_M.png')

        elif self.direction == LEFT:
            self.image = load_image('CHAR_leg_S_R_J_M_re.png')
        if key == RIGHT:
            if self.x + 15 <400:
                self.x +=10
            self.frame = (self.frame + 1 ) % 10;
        if key == LEFT:
            if self.x + 15 > 55:
                self.x -= 10
            self.frame = (self.frame + 1) % 10;
        elif key == UP:
            self.y+=5
            self.frame = (self.frame +1) % 10
    def update(self):
        pass
#        if self.state == STAND:
#            self.frame = (self.frame + 1 ) % 10


    def draw(self):
        if self.state == STAND:
            if self.direction == RIGHT:
                self.image.clip_draw(56 * self.frame, 25*self.state, 56, 25, self.x, self.y, 80,50)
            elif self.direction == LEFT:
                self.image.clip_draw(560-(56 * (self.frame+1)), 25*self.state, 56, 25, self.x-25, self.y, 80,50)
        elif self.state == RUN:
            if self.direction == RIGHT:
                self.image.clip_draw(56 * self.frame, 25*self.state, 56, 25, self.x+3, self.y, 80,70)
            elif self.direction == LEFT:
                self.image.clip_draw(560-(56 * (self.frame+1)), 25*self.state, 56, 25, self.x-25-3, self.y, 80,70)
        elif self.state == JUMP:
            if self.direction == RIGHT:
                self.image.clip_draw(56 * self.frame, 25*(self.state-1), 56, 25, self.x, self.y, 80,50)
            elif self.direction == LEFT:
                self.image.clip_draw(560-(56 * (self.frame+1)), 25*(self.state-1), 56, 25, self.x-25, self.y, 80,50)

delay(0.05)


