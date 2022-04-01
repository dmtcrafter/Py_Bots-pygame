# Start out program

# import the pygame module
import pygame

# from pygame.math import Vector
from pygame.math import Vector2

# import time module for delays
import time

# import random
import random

# import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_SPACE,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# init pygame
pygame.init()

# set game window width and height (DEFAULT: SCREEN_WIDTH = 1200, SCREEN_HEIGHT = 800)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# fill screen with background image


class Background():
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('./assets/imgs/star-wars-backgrounds-24.jpg')


screen_img = Background()
screen_img_surf = screen_img.surf
screen.blit(screen_img_surf)

# create sprite groups
enemies = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
game_objects = pygame.sprite.Group()


class GameObjects(pygame.sprite.Sprite):
    vector = Vector2(0.5, 0)

    def __init__(self):
        super().__init__()

    def _get_game_objects(self, enemies_1):

        if player:
            game_objects.add(player)

        return game_objects


class Bullet(GameObjects):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('./assets/imgs/player_bullet.png')
        self.rect = self.surf.get_rect()
        self.bounding_rect = self.surf.get_bounding_rect()
        self.velocity = GameObjects.vector


class Enemy(GameObjects):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface
        self.velocity = Vector2(0.2, 0)

    def update(self):
        if self.rect == Player.player_bullets.bullet:
            self.surf = pygame.image.load('./assets/explosion.png')

    class Crocodile(GameObjects):
        def __init__(self):
            super().__init__()
            self.surf = pygame.image.load('./assets/SawBot.png')
            self.rect = self.surf.get_rect()
            self.bounding_rect = self.surf.get_bounding_rect()
            self.velocity = Vector2(0.3, 0)

        def update(self):
            if self.rect == player_bullets.bullet.rect:
                self.surf = pygame.image.load('./assets/explosion.png')

    class SawBot(GameObjects):
        def __init__(self):
            super().__init__()
            self.surf = pygame.image.load('./assets/imgs/saw_bot.png')
            self.rect = self.surf.get_rect()
            self.bounding_rect = self.surf.get_bounding_rect()
            self.velocity = Vector2(0.3, 0)

        def update(self):
            if self.rect == player_bullets.bullet.rect:
                self.surf = pygame.image.load('./assets/explosion.png')

    class Turret(GameObjects):
        def __init__(self):
            super().__init__()
            self.surf = pygame.image.load('./assets/imgs/turret_closed.png')
            self.rect = self.surf.get_rect()
            self.bounding_rect = self.surf.get_bounding_rect()

        def update(self):
            if self.rect == player_bullets.bullet.rect:
                self.surf = pygame.image.load('./assets/explosion.png')
            if player.rect >= (Enemy.Turret or Enemy.Crocodile() or Enemy.SawBot()):
                time.sleep(0.2)
                bullet = Bullet()
                enemy_bullets.add(bullet)


class Player(GameObjects):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('./assets/imgs/player_bot_1.png').convert()
        self.rect = self.surf.get_rect(center=(SCREEN_HEIGHT-100, SCREEN_WIDTH-1100))

    def update(self, pressed_keys):
        # if hit, subtract one health point
        hit = False
        health = 3
        par_1 = bullet.rect

        par_2 = (Enemy.SawBot().rect or Enemy.Crocodile().rect or Enemy.Turret.rect)
        par_3 = player.rect

        if par_1 == par_2:
            hit = True

        elif par_2 == par_3:
            hit = True

        if hit:
            health = health - 1

        if health <= 0:
            self.surf = pygame.image.load('')
            self.kill()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_SPACE]:
            n_bullet = Bullet()
            player.player_bullets.append(n_bullet)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0


# create player
player = Player()

# add player to game_objects group
game_objects.add(player)

# variable to keep main loop running
running = True

# MAIN LOOP
while running:
    # Look at event queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the 'Close' button? If so, stop the loop
        elif event.type == QUIT:
            running = False

    enemy_type = [Enemy.Turret(), Enemy.Crocodile(), Enemy.SawBot()]
    enemy_choice = random.choice(enemy_type)
    n_enemy = Enemy()
    # delay new enemy creation
    time.sleep(0.5)
        
    if player.rect >= (Enemy.Turret or Enemy.Crocodile() or Enemy.SawBot()):
        time.sleep(0.2)
        bullet = Bullet()

    # get currently pressed keys
    pressed_keys = pygame.key.get_pressed()

    # update player sprite based on user key presses
    player.update(pressed_keys)

    # draw surf onto the screen at the center
    screen.blit(player.surf, player.rect)
    pygame.display.flip()
