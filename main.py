from pygame import *
from random import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
background = (255,255,255)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed_x, speed_y, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width,player_height))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(GameSprite):
    def update_left(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_s] and self.rect.y < 630:
            self.rect.y += self.speed_y
        if key_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed_y

    def update_right(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_DOWN] and self.rect.y < 630:
            self.rect.y += self.speed_y
        if key_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed_y


racket1 = player('racket.png', 50, 175, 0, 5, 30, 100)
racket2 = player('racket.png', 600, 175, 0, 5, 30, 100)
ball = GameSprite('ball.png', 225, 325, 5, 5, 50, 50)

font.init()
write = font.SysFont('arial', 24)

losed = write.render('LOSE', 1, (255,0,0))
won = write.render('WIN', 1, (0,255,0))










clock = time.Clock()
FPS = 60

finish = False
game = True

while game:
    window.fill(background)
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        racket1.reset()
        racket2.reset()

        ball.reset()

        racket1.update_left()
        racket2.update_right()







    if ball.rect.y > win_height or ball.rect.y < win_height:
        ball.speed_y *= -1
    if ball.rect.x < win_width:
        window.blit(losed, (20,15))

    display.update()
    clock.tick(FPS)
