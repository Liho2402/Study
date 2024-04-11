import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Frame
Fps = 60
Frame = pygame.time.Clock()

# Colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
grey = pygame.Color(128,128,128)
red = pygame.Color(255,0,0)
blue = (0, 0, 255)

# Size of screen
screen_width = 400
screen_height = 600

# variables
speed = 5
score = 0
coins_counter = 0

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

# Background
background = pygame.image.load("images/AnimatedStreet.png")

# Create white screen
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")

# Coins
class Coins(pygame.sprite.Sprite):
    def __init__(self, enemies):
        super().__init__()
        self.image = pygame.image.load("images/coin-svgrepo-com.svg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width-40), 0)
        self.enemies = enemies

        while pygame.sprite.spritecollideany(self, self.enemies):
            self.rect.center = (random.randint(40, screen_width-40), 0)
    def move(self):
        global coins_counter
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40,screen_width - 40), 0)
# Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width-40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)

    def collect_coins(self, coin):
        global coins_counter
        collisions = pygame.sprite.spritecollide(self, coin, True)
        for coin in collisions:

            # different weights
            if random.choice([3,2,1]) == 3:
                coins_counter += 3
            elif random.choice([3, 2]) == 2:
                coins_counter += 2
            else:
                coins_counter += 1

            return True
        return False

p1 = Player()
e1 = Enemy()

# Sprites Group
enemies = pygame.sprite.Group()
enemies.add(e1)

c = Coins(enemies)
coins = pygame.sprite.Group()
coins.add(c)

all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
all_sprites.add(c)


# Increase speed
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

# Game loop
while True:
    # Loop of occurring events
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.1
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Show score and render back
    display.blit(background, (0,0))
    scores = font_small.render(str(score), True, black)
    coins_scores = font_small.render(str(coins_counter), True, black)
    display.blit(scores, (10,10))
    display.blit(coins_scores, (360, 10))

    # Move and re-draw all sprites
    for entity in all_sprites:
        display.blit(entity.image, entity.rect)
        entity.move()
    # When score not zero and divided on 10 we increase speed
    if coins_counter > 0 and coins_counter % 20 == 0:
        speed += 0.1
    if p1.collect_coins(coins):
        pygame.mixer.Sound("sound/brosok-odnoy-monetki-v-obschuyu-kuchu.wav").play()
        # coins_counter += 1
        new_coin = Coins(enemies)
        coins.add(new_coin)
        all_sprites.add(new_coin)
        coins_scores = font_small.render(str(coins_counter), True, black)  # Обновление текста с количеством монеток

    # Collision between p and e
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound("sound/crash.wav").play()
        time.sleep(0.5)

        display.fill(2)
        display.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    Frame.tick(Fps)