from pico2d import *
import Background
import Marco_Char
import Bullet
import Rebel_Soldie_Char

program = None
bg_01 = None


arrow = None
char_body, char_leg = None,None
key = None
body_state = None
leg_state = None
direction = None
bullet = None
shooting = 0

LEFT,RIGHT, UP ,DOWN= 0,1,2,3
STAND, RUN, SHOT, JUMP, STAB, SWING = 0,1,2,3,4,5
MOVEJUMP = 6

def enter():
    global program
    global bg_01
    global rebel

    global char_body, char_leg
    global key
    global arrow
    global body_state, leg_state
    global direction
    global bullet
    shooting = 50
    direction = RIGHT
    body_state = STAND
    leg_state = STAND
    program = True
    bg_01 = Background.BG()


    rebel = Rebel_Soldie_Char.Rebel()
    char_body = Marco_Char.Marco_body()
    char_leg = Marco_Char.Marco_Leg()
    #bullet = Bullet.shot()
def update():
    global body_state
    global bullet
    global rebel




    if char_body.shot == 9 or char_body.swing == 5:
        body_state = STAND
        char_body.shot = 0
        char_body.swing = 0
    #if body_state == SHOT:
        #bullet.update(char_body.x,char_body.y)

    char_body.Move(key,direction,body_state)
    char_leg.Move(key,direction,leg_state)
    if char_body.x > 380 and key == RIGHT:
        bg_01.x +=3

    rebel.update()
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
    bg_01.draw()
    rebel.draw()


    char_leg.draw()
    char_body.draw()




def exit():
    global bg_01,arrow,char_body,char_leg,rebel

    del(bg_01)
    del(rebel)
    del(arrow)
    del(char_body)
    del(char_leg)


def handle_events():

     global program
     global key
     global body_state,leg_state
     global direction

     mx,my = 0,0
     events = get_events()
     for event in events:
        if event.type == SDL_QUIT:
               program = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                key = RIGHT
                direction = RIGHT
                body_state, leg_state = RUN,RUN
            if event.key == SDLK_LEFT:
                key = LEFT
                direction = LEFT
                body_state, leg_state = RUN,RUN

            if event.key == SDLK_a:
                body_state = SHOT
                leg_state = SHOT

            elif event.key == SDLK_ESCAPE:
                    program = False

        elif event.type == SDL_KEYUP: # 하드웨어적인 문제로 동시키입력이 안돼
            key = -1
            body_state = STAND
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

