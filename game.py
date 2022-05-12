# Start out program

# import the pygame module
import pygame


from pygame.image import load
# from pygame.math import Vector
from pygame.math import Vector2

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

# variable to keep main loop running
running = True

# set game window width and height (DEFAULT: SCREEN_WIDTH = 1200, SCREEN_HEIGHT = 800)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Create the display
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Py_Bots', './assets/imgs/icon.png')


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = load('./assets/imgs/background_1.png').convert()
        self.rect = self.surf.get_rect()


screen_img = Background()

# create sprite groups
enemies = pygame.sprite.Group()
player_bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

all_sprites.add(screen_img)

enemies.add(enemy_bullets)


class GameObjects(pygame.sprite.Sprite):
    p_velo = Vector2(1, 0)
    e_velo = Vector2(-1, 0)

    def __init__(self):
        super().__init__()

    def get_sprites(self):
        all_sprites.add(*enemies, *player_bullets, *enemy_bullets)

        return all_sprites


class Bullet(GameObjects):

    def __init__(self, bullet_type, position, velo):
        super().__init__()
        # copy vector
        self.surf = bullet_type
        self.rect = self.surf.get_rect()
        self.direction = velo
        self.position = position
        self.bounding_rect = self.surf.get_bounding_rect()


class Enemy(GameObjects):
    type_e = load('./assets/imgs/enemy_bullet.png')
    
    def __init__(self):
        super().__init__()

    class Crocodile(GameObjects):
        def __init__(self, x_pos, y_pos):
            super().__init__()
            self.surf = load('./assets/imgs/crocodile.png')
            self.rect = self.surf.get_rect(center=(x_pos, y_pos))
            self.velocity = [-1, 0]

        def update(self):
            self.rect = self.rect.update(self.velocity)

            # Check if any bullets have collided with the enemy
            if pygame.sprite.spritecollideany(self, player_bullets):
                # If so, then remove the player and stop the loop
                self.kill()
                self.surf = load('./assets/imgs/explosion.png').convert()
                self.kill()

    class SawBot(GameObjects):
        def __init__(self, x_pos, y_pos):
            super().__init__()
            self.surf = load('./assets/imgs/saw_bot.png').convert()
            self.rect = self.surf.get_rect(center=(x_pos, y_pos))
            self.velocity = (-3, 0, 0, 0)

        def update(self):
            self.rect = self.rect.update(self.velocity)

            # Check if any player_bullets have collided with the enemy
            if pygame.sprite.spritecollideany(self, player_bullets):

                self.kill()

    class Turret(GameObjects):
        def __init__(self, x_pos, y_pos):
            super().__init__()
            self.surf = load('./assets/imgs/turret_open.png').convert()
            self.rect = self.surf.get_rect(center=(x_pos, y_pos))
            self.functioning = True
            self.position = self.rect.center

        def shoot(self):
            type_e = load('./assets/imgs/enemy_bullet.png').convert()
            enemy_bullet_velocity = Vector2(-1, 0)
            enemy_bullet = Bullet(type_e, self.position, enemy_bullet_velocity)
            enemy_bullets.add(enemy_bullet)

        def update(self):
            # Check if any player bullets have collided with the enemy
            if pygame.sprite.spritecollideany(self, player_bullets):
                # If so, then remove the turret
                self.kill()


class Player(GameObjects):

    def __init__(self):
        super().__init__()
        self.surf = load('./assets/imgs/player_bot_1.png').convert()
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH-1100, SCREEN_HEIGHT-100))

    def shoot(self):
        if pressed_keys[K_RIGHT]:
            p_velo_1 = Vector2(2, 0)
        else:
            p_velo_1 = Vector2()
        type_p = load('./assets/imgs/player_bullet.png').convert()
        player_bullet = Bullet(type_p, self.rect.left, p_velo_1)
        player_bullets.add(player_bullet)

    def update(self, pressed_keys):

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # If so, then the player dies and the game ends
            self.kill()
            exit()
        # Check if any enemy bullets have collided with the player
        elif pygame.sprite.spritecollideany(player, enemy_bullets):
            # If so, then the player dies and the game ends
            self.kill()
            exit()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2, 0)

        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(2, 0)

        # Keep player on the screen_img
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


player = Player()

# create enemies for the game start and add them to 
turret_1 = Enemy.Turret(SCREEN_WIDTH-200, SCREEN_HEIGHT-100)
turret_2 = Enemy.Turret(SCREEN_WIDTH-150, SCREEN_HEIGHT-150)
saw_bot_1 = Enemy.SawBot(SCREEN_WIDTH-460, SCREEN_HEIGHT-100)
saw_bot_2 = Enemy.SawBot(SCREEN_WIDTH-440, SCREEN_HEIGHT-100)
crocodile = Enemy.Crocodile(SCREEN_WIDTH-500, SCREEN_HEIGHT-100)

enemies.add(turret_1, saw_bot_1, turret_2, saw_bot_2, crocodile)

all_sprites.add(screen_img)


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
        elif player and event.type == pygame.KEYDOWN and event.key == K_SPACE:
            player.shoot()

    tick_int = '1'
    try:
        index = tick_int.rindex(tick_int)

    except:
        print('rindex() error')

    # get currently pressed keys
    pressed_keys = pygame.key.get_pressed()

    # add enemies and bullets
    all_sprites.add(enemies)

    if player:
        all_sprites.add(player)

    for enemy in enemies:
        if enemy:
            all_sprites.add(enemy)

    for player_bullet in player_bullets:
        if player_bullet:
            all_sprites.add(player_bullet)

    # update player sprite based on user key presses
    player.update(pressed_keys)

    turret_1.update()
    turret_2.update()
    saw_bot_1.update()
    saw_bot_2.update()
    crocodile.update()

    # Draw all sprites
    for entity in all_sprites:
        display.blit(entity.surf, entity.rect)

    pygame.display.update()
