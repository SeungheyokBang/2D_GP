from pico2d import *

import Marco_char


from Background import *

program = None
bg_01 = None
ui = None
SHOP = False
arrow = None
char_body, char_leg = None,None
key = None
body_state = None
leg_state = None
direction = None
bullet = None
shooting = 0

LEFT,RIGHT, UP = 0,1,2
STAND, RUN, SHOT, JUMP, STAB, SWING = 0,1,2,3,4,5
MOVEJUMP = 6

def enter():
    global program
    global bg_01

    global char_body, char_leg
    global key
    global arrow
    global body_state, leg_state
    global direction


    shooting = 50
    direction = RIGHT
    body_state = STAND
    leg_state = STAND
    program = True


    char_body = Marco_char.Character_body()
    char_leg = Marco_char.Character_leg()

def update():
    global body_state


    if char_body.shot == 9 or char_body.stab == 5 or char_body.swing == 5:
        body_state = STAND
        char_body.shot = 0
        char_body.stab = 0
        char_body.swing = 0
    if body_state == SHOT:
        bullet.update(char_body.x,char_body.y)

    char_body.move(key,direction,body_state)
    char_leg.move(key,direction,leg_state)


    char_body.update()
    char_leg.update()



def draw():
    global shooting
    if direction == RIGHT:
        if body_state == SHOT:
            shooting += 1
        if shooting >0:
            shooting += 50
    elif direction == LEFT:
        if body_state == SHOT:
            shooting -= 1
        if shooting <0:
            shooting -= 50

    if shooting > 1000 or shooting < -500:
        shooting = 0
    clear_canvas()

    char_leg.draw()
    char_body.draw()
    if shooting != 0:
        bullet.draw(shooting,direction)



def exit():
    global bg_01,ui,arrow,char_body,char_leg

    del(bg_01)
    del(ui)
    del(arrow)
    del(char_body)
    del(char_leg)


def handle_events():

     global program
     global key
     global body_state,leg_state
     global direction
     global SHOP
     mx,my = 0,0

     events = get_events()

     for event in events:
        if event.type == SDL_QUIT:
               program = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                mx, my = event.x, 768 - event.y
                if mx > 945 and mx < 1015 and my >685 and my < 755:
                    SHOP = True;




        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                key = RIGHT
                direction = RIGHT
                body_state, leg_state = RUN,RUN
            elif event.key == SDLK_LEFT:
                key = LEFT
                direction = LEFT
                body_state, leg_state = RUN,RUN
            elif event.key == SDLK_s:
                body_state,leg_state = JUMP, JUMP
                key = UP
            elif event.key == SDLK_a:
                body_state = SHOT
            #elif event.key == SDLK_a:
             #   body_state = STAB
            elif event.key == SDLK_d:
                body_state = SWING


            elif event.key == SDLK_ESCAPE:
                    program = False


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                key = -1
                leg_state = STAND
            elif event.key == SDLK_LEFT:
                key = -1
                leg_state = STAND




def main():

    open_canvas(1024, 768)
    enter()
    while program:
        handle_events()
        update()
        draw()
        update_canvas()

    delay(0.05)
    exit()
    close_canvas()

if __name__ == '__main__':
    main()

