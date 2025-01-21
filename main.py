import pygame
import time
pygame.init()
from map1 import *

fps = 165
win_w, win_h = 1400, 1000

window = pygame.display.set_mode((win_w, win_h))

pygame.display.set_caption("Labirint")

pygame.mixer.music.load("jungles.ogg")

timer = pygame.time.Clock()

background = pygame.image.load("bg.jpg")
background = pygame.transform.scale(background, (win_w, win_h))

class Sprite:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed

    def move(self, a, d, s, w): 
        keys = pygame.key.get_pressed() 
        if keys[d]: 
            self.rect.x += self.speed
        if keys[a]: 
            self.rect.x -= self.speed
        if keys[w]: 
            self.rect.y -= self.speed
        if keys[s]: 
            self.rect.y += self.speed

class Enemy(Sprite):
    def __init__(self, x, y, w, h, image, speed, x2):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.x1 = x
        self.x2 = x2

    def move(self):
        self.rect.x += self.speed

blocks = []
block_size = 25

block_x = 0
block_y = 0
block_img = pygame.image.load("wall.png")

for row in lvl1:
    for tile in row:
        if tile == "1":
            blocks.append(Sprite(block_x, block_y, block_size, block_size, block_img))
        block_x = 0
        block_y += block_size

font = pygame.font.SysFont("Arial", 80)
lose = font.render("You Lose!", True, (255, 0, 0))
win = font.render("You Win!", True, (0, 255, 0))


img_gold = pygame.image.load("treasure.png")
treasure = Sprite(100, 50, 50, 50, img_gold)

player = Player(0, 400, 50, 50, pygame.image.load("sprite1.png"), 2)

enemy1 = Enemy(200, 300, 50, 50, pygame.load.image("cyborg.png"), 2, 400)

game = True
finish = False

while game:

    if not finish:

        window.blit(background, (0, 0))
    
        for b in blocks:
            b.draw()


        player.draw()
        player.move(pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w)
        treasure.draw()
        enemy1.draw()
        enemy1.move()

        for b in blocks:
            if player.rect.colliderect(b.rect):
                window.blit(lose, (50, 100))
                game = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event

        timer.tick(fps)
        pygame.display.update()

pygame.time.delay(1000)
