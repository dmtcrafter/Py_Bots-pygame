# Start out program


# import the pygame module
import pygame

# import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./Block_Bros_assets/imgs/Red_Block_Bot.png")


# init pygame
pygame.init()

# set game window width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constants SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
    # Fill the screen with an image
    screen.fill((69, 139, 116, 255))

    # draw surf onto the screen at the center
    screen.blit(player_1.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    pygame.display.flip()
