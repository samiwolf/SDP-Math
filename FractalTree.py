from __future__ import division
import pygame
from pygame.locals import *
from math import sin, cos, atan, pi

def run():
    pygame.init()

    W, H = 800, 600
    p = W // 2
    q = H // 2
    gray = (211, 211, 211)
    black = (0, 0, 0)
    screen = pygame.display.set_mode((W, H), 0, 32)
    screen.fill(gray)
    phase = lambda x, y, a, b: \
        atan((y - q) / (p - x + 0.1)) + pi * (p - x < 0)


    def rotate(x1, y1, x0, y0, l):
        """rotation CCW,  angle l,  around x0, y0"""
        return ((x1 - x0) * cos(l) - (y1 - y0) * sin(l) + x0,
                (x1 - x0) * sin(l) + (y1 - y0) * cos(l) + y0)


    def line(x1, y1, x2, y2, w):
        points = [(int(x1), int(H - y1)), (int(x2), int(H - y2))]
        pygame.draw.lines(screen, black, False, points, w // 2)


    def tree(x1, y1, x2, y2, a, n):
        r = 0.33  # shortening of next branch,  nice at [0.31..0.48]
        if n:
            line(x1, y1, x2, y2, n)
            x3 = x1 + (x2 - x1) * r
            y3 = y1 + (y2 - y1) * r
            rx1, ry1 = rotate(x3, y3, x2, y2, a)
            tree(x2, y2, rx1, ry1 , a, n - 1)
            rx2, ry2 = rotate(x3, y3, x2, y2, a + pi / 2)
            tree(x2, y2, rx2, ry2, a, n - 1)
        else:
            pygame.draw.circle(screen, (0, 180, 20), (int(x1), int(H - y1)), 3, 1)


    mainloop = True
    while mainloop:
        x, y = pygame.mouse.get_pos()
        tree(W // 2, 40, W // 2, 220, phase(x, y, p, q) - 2.5, 11)  # coords of stem
        pygame.display.update()
        screen.fill(gray)
        for event in pygame.event.get():
            if event.type == QUIT:
                mainloop = False
    #   pygame.time.wait(20)
    #   delay
    pygame.quit()


run()