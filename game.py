# Start out program

# import the pygame module
import pygame

# from pygame.math import Vector
from pygame.math import Vector2

# import random
import random

# import pygame.locals for easier access to key coordinates
from pygame.locals import (
    RLEACCEL,
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
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Create the screen object
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('./assets/imgs/background_1.png').convert()
        self.rect = self.surf.get_rect()


screen = Background()

# create sprite groups
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
game_objects = pygame.sprite.Group()


class GameObjects(pygame.sprite.Sprite):
    vector = Vector2(0.5, 0)

    def __init__(self):
        super().__init__()

    def _get_game_objects(self):
        game_objects.add(*enemies, *bullets)

        if player:
            game_objects.add(player)

        return game_objects


class Bullet(GameObjects):
    def __init__(self, bullet_type):
        super().__init__()
        self.surf = bullet_type
        self.rect = self.surf.get_rect()
        self.bounding_rect = self.surf.get_bounding_rect()
        self.velocity = GameObjects.vector


class Enemy(GameObjects):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface
        self.velocity = Vector2(0.2, 0)

    def update(self):
        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(self, bullets):
            # If so, then remove the player and stop the loop
            player.kill()
            self.surf = pygame.image.load('./assets/explosion.png').convert()
            
            self.kill()

    class Crocodile(GameObjects):
        def __init__(self):
            super().__init__()
            self.surf = pygame.image.load('./assets/imgs/crocodile.png').convert()
            self.rect = self.surf.get_rect()
            self.bounding_rect = self.surf.get_bounding_rect()
            self.velocity = Vector2(0.3, 0)

        def update(self):
            # Check if any enemies have collided with the player
            if pygame.sprite.spritecollideany(self, bullets):
                # If so, then remove the player and stop the loop
                player.kill()
                self.surf = pygame.image.load('./assets/explosion.png').convert()
                
                self.kill()

    class SawBot(GameObjects):
        def __init__(self):
            super().__init__()
            self.surf = pygame.image.load('./assets/imgs/saw_bot.png').convert()
            self.rect = self.surf.get_rect()
            self.bounding_rect = self.surf.get_bounding_rect()
            self.velocity = Vector2(0.3, 0)

        def update(self):
            # Check if any enemies have collided with the player
            if pygame.sprite.spritecollideany(self, bullets):
                # If so, then remove the player and stop the loop
                player.kill()
                self.surf = pygame.image.load('./assets/explosion.png').convert()
                
                self.kill()

    class Turret(GameObjects):
        def __init__(self):
            super().__init__()
            self.surf = pygame.image.load('./assets/imgs/turret_closed.png').convert()
            self.surf.set_colorkey((255, 255, 0), RLEACCEL)
            self.rect = self.surf.get_rect()
            self.bounding_rect = self.surf.get_bounding_rect()

        def update(self):
            # Check if any enemies have collided with the player
            if pygame.sprite.spritecollideany(self, bullets):
                # If so, then remove the player and stop the loop
                player.kill()
                self.surf = pygame.image.load('./assets/explosion.png').convert()
                
                self.kill()


class Player(GameObjects):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('./assets/imgs/player_bot_1.png').convert()
        self.surf.set_colorkey((255, 255, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH-1100, SCREEN_HEIGHT-100))

    def update(self, pressed_keys):
        # if hit, subtract one player_health point
        p_hit = False
        player_health = 3

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # If so, then remove the player and stop the loop
            p_hit = True

        if p_hit:
            player_health = player_health - 1
            p_hit = False
            return p_hit, player_health

        if player_health <= 0:
            self.surf = pygame.image.load('/assets/imgs/explosion.png').convert()
            
            self.kill()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if pressed_keys[K_SPACE]:
            type_p = pygame.image.load('./assets/imgs/player_bullet.png').convert()
            bullet = Bullet(type_p)
            bullets.add(bullet)

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

    # fill screen with background image
    display.blit(screen.surf, screen.rect)

    enemy_type = [Enemy.Turret(), Enemy.Crocodile(), Enemy.SawBot()]
    enemy_choice = random.choice(enemy_type)

    n_enemy = Enemy()
    # Draw all sprites
    for entity in game_objects:
        display.blit(entity.surf, entity.rect)

    # get currently pressed keys
    pressed_keys = pygame.key.get_pressed()

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    # add new enemy bullets
    
    type_e = pygame.image.load('./assets/imgs/enemy_bullet.png')
    eBullet = Bullet(type_e)
    bullets.add(eBullet)

    # update player sprite based on user key presses
    player.update(pressed_keys)

    # draw surf onto the screen at the center
    display.blit(player.surf, player.rect)
    pygame.display.flip()
