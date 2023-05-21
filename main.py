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

racket1 = player('racket.png', 40, 200, 0, 5, 40, 100)
racket2 = player('racket.png', 620, 200, 0, 5, 40, 100)
ball = ball('ball.png', 325, 225, 4*(choice([-1,1])), 5.5*(choice([-1,1])), 50, 50)

font.init()
write = font.SysFont('arial', 24)
write_aa = font.SysFont('arial', 48)

right_score = 0
left_score = 0

losed = write.render('LOSE', 1, (255,0,0))
won = write.render('WIN', 1, (0,255,0))
right_score_wr = write.render(f'{right_score}', 1, (0,255,255))
left_score_wr = write.render(f'{left_score}', 1, (0,255,255))
losed_aa = write_aa.render('LOSED', 1, (255,0,0))
won_aa = write_aa.render('WON', 1, (0,255,0))


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
        ball.rect.x = 325
        ball.rect.y = 225
        racket1.rect.y = 200
        racket2.rect.y = 200
        reloading = False

    if ball.rect.x < 71:
        window.blit(losed, (100,15))
        window.blit(won, (535,15))
    elif ball.rect.x > 579:
        window.blit(losed, (535,15))
        window.blit(won, (100,15))


    if ball.rect.x < 69:
        ball.speed_x *= -1
        ball.rect.x += 1
        reloading = True
        lastReloadTime = t.time()
        ball.speed_x *= choice([-1,1])
        ball.speed_y *= choice([-1,1])
    elif ball.rect.x > 581:
        ball.speed_x *= -1
        ball.rect.x -= 1
        reloading = True
        lastReloadTime = t.time()
        ball.speed_x *= choice([-1,1])
        ball.speed_y *= choice([-1,1])


    if ball.rect.x > 583:
        left_score += 1
    elif ball.rect.x < 67:
        right_score += 1

    right_score_wr = write.render(f'{right_score}', 1, (0,255,255))
    left_score_wr = write.render(f'{left_score}', 1, (0,255,255))

    window.blit(right_score_wr, (620,15))
    window.blit(left_score_wr, (65,15))

    if left_score >= 5:
        window.blit(losed_aa, (410,200))
        window.blit(won_aa, (120,200))
        finish = True
    elif right_score >= 5:
        window.blit(won_aa, (430,200))
        window.blit(losed_aa, (120,200))
        finish = True


    display.update()
    clock.tick(FPS)
