from pygame import*
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, pimage, x, y, speed):
        super().__init__()

        self.pimage = transform.scale(image.load(pimage), (60, 60))

        self.rect = self.pimage.get_rect()
        self.speed = speed 

        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.pimage, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed
        if keys[K_d] and self.rect.x < win_width - self.rect.width:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x > win_width - self.rect.width:
            self.direction = "left"
        if self.rect.x < win_width * 0.7:
            self.direction = "right"

        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
    
    direction2 = "left"

    def update2(self):
        if self.rect.x > 170:
            self.direction2 = "left"
        if self.rect.x < 0:
            self.direction2 = "right"

        if self.direction2 == "left":
            self.rect.x -= self.speed
        if self.direction2 == "right":
            self.rect.x += self.speed

win_height = 500
win_width = 700

window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("wawe.jpg"), (win_width, win_height))
display.set_caption("Лабіринт")

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_w, wall_h):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = Player("tank.png", 10, win_height-80, 4)
enemy = Enemy("tank2.png", win_width-80, 110, 2)
enemy2 = Enemy("tank2.png", 100, 300, 2)
final = GameSprite("treasure.png", win_width-80, win_height-80, 0)

wall2 = Wall(3, 121, 121, 20, 20, 20, 380)
wall3 = Wall(3, 121, 121, 650, 20, 20, 390)
wall4 = Wall(3, 121, 121, 120, 120, 20, 400)
wall5 = Wall(3, 121, 121, 220, 20, 20, 380)
wall6 = Wall(3, 121, 121, 220, 380, 120, 20)
wall7 = Wall(3, 121, 121, 420, 380, 100, 20)
wall8 = Wall(3, 121, 121, 520, 380, 20, 150)
wall1 = Wall(3, 121, 121, 20, 20, 650, 20)
wall9 = Wall(3, 121, 121, 420, 280, 20, 100)
wall10 = Wall(3, 121, 121, 420, 280, 145, 20)
wall11 = Wall(3, 121, 121, 320, 170, 20, 140)
wall12 = Wall(3, 121, 121, 320, 170, 230, 20)
wall13 = Wall(3, 121, 121, 620, 390, 40, 20)
wall14 = Wall(3, 121, 121, 540, 160, 20, 140)
wall15 = Wall(3, 121, 121, 320, 20, 20, 50)
wall16 = Wall(3, 121, 121, 480, 120, 20, 50)
wall17 = Wall(3, 121, 121, 480, 120, 95, 15)

game = True
clock = time.Clock()
FPS = 30

mixer.init()
mixer.music.load("pirate-ship-cinematic-movie-scene-254144.mp3")
mixer.music.play()
mixer.music.get_volume()

kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")

while game:
    window.blit(background, (0, 0))

    player.update()
    enemy.update()
    enemy2.update2()

    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()
    wall7.draw_wall()
    wall8.draw_wall()
    wall9.draw_wall()
    wall10.draw_wall()
    wall11.draw_wall()
    wall12.draw_wall()
    wall13.draw_wall()
    wall14.draw_wall()
    wall15.draw_wall()
    wall16.draw_wall()
    wall17.draw_wall()

    player.draw()
    enemy.draw()
    enemy2.draw()
    final.draw()

    if sprite.collide_rect(player, enemy2):
        enemy2.rect.x = randint(0, 700)
        enemy2.rect.y = randint(0,500)
        kick.play()
        player.rect.x = 30
        player.rect.y = 430

    if sprite.collide_rect(player, enemy):
        enemy.rect.x = randint(0, 700)
        enemy.rect.y = randint(0,500)
        kick.play()
        player.rect.x = 30
        player.rect.y = 430

    if sprite.collide_rect(player, wall1) or \
            sprite.collide_rect(player, wall2) or \
            sprite.collide_rect(player, wall3) or \
            sprite.collide_rect(player, wall4) or \
            sprite.collide_rect(player, wall5) or \
            sprite.collide_rect(player, wall6) or \
            sprite.collide_rect(player, wall7) or \
            sprite.collide_rect(player, wall9) or \
            sprite.collide_rect(player, wall10) or \
            sprite.collide_rect(player, wall11) or \
            sprite.collide_rect(player, wall12) or \
            sprite.collide_rect(player, wall13) or \
            sprite.collide_rect(player, wall14) or \
            sprite.collide_rect(player, wall15) or \
            sprite.collide_rect(player, enemy) or \
            sprite.collide_rect(player, enemy2):
        kick.play()
        player.rect.x = 30
        player.rect.y = 430
    if sprite.collide_rect(player, final):
        time.delay(1000)
        money.play()
        game = False

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)