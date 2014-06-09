import pygame
from pygame.locals import *
from time import sleep

# const variables
WIDTH = 640
HEIGHT = 640
STROKE = 1
FPS = 1

# initialization of pygame
pygame.init()

# setup a game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(pygame.Color(255, 255, 255))

# mouse position
mouse_x, mouse_y = 0, 0

# create Clock object to keep the refresh rate stable
clock = pygame.time.Clock()

# draw
while True:
    # processing each event
    for event in pygame.event.get():
        # record the mouse position if the mouse moved
        if event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        # refresh the window if the mouse button was clicked
        if event.type == MOUSEBUTTONDOWN:
            window.fill(pygame.Color(255, 255, 255))
    radius = (abs(WIDTH / 2 - mouse_x) + abs(HEIGHT / 2 - mouse_y)) / 2 + 1
    # draw a circle
    pygame.draw.circle(window,
        pygame.Color(255, 0, 0),
        (mouse_x, mouse_y), radius, STROKE)
    pygame.display.update()
    # this control the fresh rate
    clock.tick(FPS)
    print 'FPS: %s' % clock.get_fps()

