import pygame
from time import sleep

# initialization of pygame
pygame.init()

# setup a game window
screen = pygame.display.set_mode((450, 450))

# setup a system font
font = pygame.font.SysFont('freeserif', 72)

# create a text surface (the second arg is anti-aliasing flag)
text_surface = font.render('Hello!', True, pygame.Color(255, 255, 255))

# draw the text
screen.blit(text_surface, (10, 10))
while True:
    pygame.display.update()
    sleep(0.1)
