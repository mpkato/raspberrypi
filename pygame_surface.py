import pygame
from time import sleep

# initialization of pygame
pygame.init()

# setup a game window
screen = pygame.display.set_mode((450, 450))

# load images
background = pygame.image.load('brick.png')
background.convert_alpha()
enemy = pygame.image.load('games-alt-1.png')
enemy.convert_alpha()

# init position of enemy
x = 130

# draw
while True:
    # draw the surfaces
    screen.blit(background, (0, 0))
    screen.blit(enemy, (x, 330))
    # move!
    x += 1
    pygame.display.update()
    sleep(0.1)
