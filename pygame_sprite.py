import pygame

# const varibles
WIDTH = 500
HEIGHT = 500
FPS = 3

# Ball class inherits pygame.sprite.Sprite
class Ball(pygame.sprite.Sprite):
    # const variables
    INIT_X = 10
    INIT_Y = 10
    RADIUS = 10
    STROKE = 0
    # this method is called when an instance is generated, 
    # i.e. Ball(x, y, xdir, ydir, speed)
    def __init__(self, x, y, xdir, ydir, speed):
        # call __init__ method of the super class
        pygame.sprite.Sprite.__init__(self)

        # initialize the surface
        self.image = pygame.Surface([20, 20])
        self.image.fill(pygame.Color(255, 255, 255))
        # draw a ball at the initial position
        pygame.draw.circle(self.image, 
            pygame.Color(255, 0, 0),
            (self.INIT_X, self.INIT_Y), self.RADIUS, self.STROKE)
        self.rect = self.image.get_rect()
        # init instance variables with given values
        self.x, self.y = x, y
        self.xdir, self.ydir = xdir, ydir
        self.speed = speed

    # update the position of the ball
    def update(self):
        # update the position
        self.x = self.x + (self.xdir * self.speed)
        self.y = self.y + (self.ydir * self.speed)
        # change the direction if the ball hit the walls
        if (self.x - self.RADIUS < 0) or (self.x + self.RADIUS > WIDTH):
            self.xdir = -self.xdir
        if (self.y - self.RADIUS < 0) or (self.y + self.RADIUS > HEIGHT):
            self.ydir = -self.ydir
        # set the position of the rect
        self.rect.center = (self.x, self.y)

# this block is called only when this program is directly invoked by python
if __name__ == '__main__':
    # initialization of pygame
    pygame.init()

    # setup a game window and create balls
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    balls = []
    balls.append(Ball(100, 250, 1, 1, 5))
    balls.append(Ball(400, 10, -1, -1, 8))

    # create Clock object to keep the refresh rate stable
    clock = pygame.time.Clock()

    while True:
        # update each ball
        for ball in balls:
            ball.update()
        # refresh the window
        window.fill(pygame.Color(255, 255, 255))
        # draw each ball
        for ball in balls:
            window.blit(ball.image, ball.rect)
        pygame.display.update()
        # this control the fresh rate
        clock.tick(FPS)
        print 'FPS: %s' % clock.get_fps()
