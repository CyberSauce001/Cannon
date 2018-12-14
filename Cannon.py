import pygame ,sys, time
from math import *
from pygame.locals import *
import numpy as np

pygame.init() #initialize all import pygame modules


FPS = 60
fpsClock = pygame.time.Clock()

#Set Up Window
resolution = (1325, 603) #set screen size
display = pygame.display.set_mode(resolution, pygame.RESIZABLE)
pygame.display.set_caption("Test")

g = 9.8 #value of gravity
vel = 2.0 #value of initial velocity
theta = 40.0 * np.pi / 180.0
t = 2 * vel * np.sin(theta) / g #time



#pixel images
cannon_size = (100,100)
cannon_ball_sz = (25,25)
background = pygame.transform.smoothscale(pygame.image.load("C:/Users/Alexander.n/PycharmProjects/Database/.idea/pixel.jpg").convert(), resolution)
cannon = pygame.transform.scale(pygame.image.load("C:/Users/Alexander.n/PycharmProjects/Database/.idea/cannon.png").convert_alpha(),cannon_size)
cannon_ball = pygame.transform.scale(pygame.image.load("C:/Users/Alexander.n/PycharmProjects/Database/.idea/cannonball.png").convert_alpha(),cannon_ball_sz)
cannonball_rect = cannon_ball.get_rect(topleft=(0,370))


dir = 'right'

while True:
    display.blit(background, (0, 0))  # top left corner of screen
    display.blit(cannon, (0, 370))  # 370 in y-axis top down
    if dir == 'right':
        cannonball_rect.x += 1
        cannonball_rect.y -= 1
        print([cannonball_rect.x, cannonball_rect.y])
        if cannonball_rect.x == 310 and cannonball_rect.y == 60:
            dir = 'down'
    elif dir == 'down':
        cannonball_rect.x += (5*t)
        cannonball_rect.y +=1
    display.blit(cannon_ball, cannonball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.type == pygame.K_SPACE:

    pygame.display.update()
    fpsClock.tick(FPS)
