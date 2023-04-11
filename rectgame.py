import pygame
import random

pygame.init()
win = pygame.display.set_mode((1280, 720))

x = 50
y = 50
h = 60
w = 60
speed = 10

i = 10
r = 10
b = 100
k = 100

d = 50

color = 130

run = True
while run:
    pygame.time.delay(16)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x<1280 - w:
        x += speed
    elif keys[pygame.K_LEFT] and x>0:
        x -= speed
    elif keys[pygame.K_DOWN] and y<720 - h:
        y += speed
    elif keys[pygame.K_UP] and y>0:
        y -= speed

    if keys[pygame.K_d] and b<1280 - i:
        b += speed
    elif keys[pygame.K_a] and b>0:
        b -= speed
    elif keys[pygame.K_s] and k<720 - r:
        k += speed
    elif keys[pygame.K_w] and k>0:
        k -= speed


    win.fill((0, 0, 0))

    if x<b+d and x>b-d and y<k+d and y>k-d:
        color = 0

    pygame.draw.rect(win, (0, 0, 130), (x, y, h, w))
    pygame.draw.rect(win,(color, 0, 0), (b, k, r, i))

    pygame.display.update()
