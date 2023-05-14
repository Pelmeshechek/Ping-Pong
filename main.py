from pygame import *
from random import *
import time as t


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))

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
        if key_pressed[K_s] and self.rect.y < 400 and not reloading:
            self.rect.y += self.speed_y
        if key_pressed[K_w] and self.rect.y > 10 and not reloading:
            self.rect.y -= self.speed_y

    def update_right(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_DOWN] and self.rect.y < 400 and not reloading:
            self.rect.y += self.speed_y
        if key_pressed[K_UP] and self.rect.y > 10 and not reloading:
            self.rect.y -= self.speed_y

class ball(GameSprite):
    def update(self):
        if not reloading:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y


        if self.rect.y < 0 or self.rect.y > 450:
            self.speed_y *= -1
        if self.rect.colliderect(racket1.rect) or self.rect.colliderect(racket2.rect):
            self.speed_x *= -1


lastReloadTime = 0

racket1 = player('racket.png', 40, 175, 0, 5, 40, 100)
racket2 = player('racket.png', 590, 175, 0, 5, 40, 100)
ball = ball('ball.png', 225, 325, 6, 4, 50, 50)

font.init()
write = font.SysFont('arial', 24)

losed = write.render('LOSE', 1, (255,0,0))
won = write.render('WIN', 1, (0,255,0))


clock = time.Clock()
FPS = 60

finish = False
game = True
reloading = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        window.blit(background,(0,0))
        racket1.reset()
        racket2.reset()
        ball.reset()

        racket1.update_left()
        racket2.update_right()
        ball.update()


    if (t.time() - lastReloadTime > 3) and reloading:
        ball.rect.x = 225
        ball.rect.y = 325
        racket1.rect.y = 175
        racket2.rect.y = 175
        reloading = False

    if ball.rect.x < 71:
        window.blit(losed, (90,15))
        window.blit(won, (515,15))
    elif ball.rect.x > 549:
        window.blit(losed, (515,15))
        window.blit(won, (90,15))


    if ball.rect.x < 69:
        ball.speed_x *= -1
        ball.rect.x += 1
        reloading = True
        lastReloadTime = t.time()
    elif ball.rect.x > 551:
        ball.speed_x *= -1
        ball.rect.x -= 1
        reloading = True
        lastReloadTime = t.time()


    display.update()
    clock.tick(FPS)