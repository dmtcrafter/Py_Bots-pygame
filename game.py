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

# set game window width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# fill screen with background image
screen_img = pygame.image.load('./assets/imgs/star-wars-backgrounds-24.jpg')
screen.blit(screen_img, (0, 0))


class GameObjects(pygame.sprite.Sprite):
    vector = Vector2(0.5, 0)
    enemy_bullets = []
    enemies = []

    def __init__(self):
        super().__init__()

    def _get_game_objects(self, enemies):
        game_objects = [*enemies]

        if player_1:
            game_objects.append(player_1)

        return game_objects


class Bullet(GameObjects):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('./assets/imgs/player_bullet.png')
        self.velocity = GameObjects.vector


class Enemy(GameObjects):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface
        self.velocity = Vector2(0.2, 0)

    def update(self):
        if self.rect == Player.player_bullets[bullet]:
            self.surf = pygame.image.load('./assets/explosion.png')

    class Gopher(GameObjects):
        def __init__(self):
            super().__init__()
            self.surf = pygame.Surface
            self.velocity = Vector2(0.3, 0)


class Player(GameObjects):
    player_bullets = []
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('./assets/imgs/player_bot_1.png').convert()
        self.rect = self.surf.get_rect(center=(SCREEN_HEIGHT-100, SCREEN_WIDTH-1100))

    def update(self, pressed_keys):
        # if hit, subtract one health point
        hit = False
        health = 3
        par_1 = (GameObjects.enemy_bullets[bullet].rect.top
                or GameObjects.enemy_bullets[bullet].rect.left or GameObjects.enemy_bullets[bullet].rect.right
                or GameObjects.enemy_bullets[bullet].rect.right)
        par_2 = (player_1.rect.top
                    or player_1.rect.left or player_1.rect.right
                    or player_1.rect.bottom)
        if par_1 == par_2:
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
            bullet = Bullet()
            player_1.player_bullets.append(bullet)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0


# create player_1
player_1 = Player()


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
    while running:

        enemy_type = [Enemy.ChomperBot(), Enemy.ChompingFish(), Enemy.Gopher()]
        enemy_choice = random.choice(enemy_type)
        n_enemy = Enemy()
        # delay new enemy creation
        time.sleep(0.5)
        
        if player_1.rect >= (Enemy.ChomperBot or Enemy.ChompingFish() or Enemy.Gopher()):
            time.sleep(0.2)
            bullet = EnemyBullet()

    # get currently pressed keys
    pressed_keys = pygame.key.get_pressed()

    # update player sprite based on user key presses
    player_1.update(pressed_keys)

    # Fill the screen with a color
    screen.fill((0, 255, 255, 255))

    # draw surf onto the screen at the center
    screen.blit(player_1.surf, player_1.rect)
    pygame.display.flip()
