import pygame
from time import sleep

width = 640
height = 480
radius = 100
stroke = 1

# initialization of pygame
pygame.init()

# setup a game window
window = pygame.display.set_mode((width, height))
window.fill(pygame.Color(255, 255, 255))

# draw
while True:
    pygame.draw.circle(window,
        pygame.Color(255, 0, 0),
        (width / 2, height / 2),
        radius, stroke)
    # update the window
    pygame.display.update()
    sleep(0.1)
