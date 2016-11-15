from pico2d import*

LEFT, RIGHT = 0,1
Time = 0.01

class shot:
    def __init__(self, x, y, Direction):
        self.x, self.y = x, y;
        self.Direction = Direction;
        self.image = load_image('bullet_basic.png')

    def update(self):
        global Time
        if self.Direction == LEFT:
            self.x -= Time * 800;

        else:
            self.x += Time * 800;


    def draw(self):
        if self.Direction == RIGHT:
            self.image.draw(self.x ,self.y)
        if self.Direction == LEFT:
            self.image.draw(self.x ,self.y)

    def get_bb(self):
        return self.x - 12.5, self.y - 12.5, self.x + 12.5, self.y + 12.5
