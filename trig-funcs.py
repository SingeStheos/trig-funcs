# Idea and colors inspired by Beautiful Math's video.
# https://youtu.be/Dsf6ADwJ66E
# 
# Coded with GPT-4 and 3.5 Turbo (ChatGPT)

import pygame
import math

pygame.init()
info = pygame.display.Info ()
screen_width, screen_height = info.current_w, info.current_h
window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("trig-funcs by Singe")

BLACK    = (0, 0, 0)
GREY      = (127, 127, 127)
WHITE    = (255, 255, 255)
PINK       = (255, 0, 255)
RED         = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN    = (0, 255, 0)
CYAN      = (0, 255, 255)
BLUE       = (32, 32, 255)

PI = math.pi
R = 200
CX = 300
CY = 300
FPS = 60
SPEED = 0.01 # This is about 1 radian per second.

# This code is really messy. If you're 
# interested in making it better, I have a 
# few dollars for you via CashApp. 

clock = pygame.time.Clock()
theta = 0
running = True
while running:
    window.fill(BLACK)
    window_center = window.get_rect().center
    pygame.draw.line(window, GREY,(0, window_center[1]), (screen_width, window_center[1]), 2)
    pygame.draw.line(window, GREY, (window_center[0], 0), (window_center[0], screen_height), 2)
    pygame.draw.circle(window, GREY, window_center, R, 2)
    dot_x = window_center[0] + R * math.cos(theta)
    dot_y = window_center[1] - R * math.sin(theta)
    pygame.draw.line(window, GREEN, (window_center[0], window_center[1]), (dot_x, window_center[1]), 2)
    pygame.draw.line(window, RED, (dot_x, window_center[1]), (dot_x, dot_y), 2)
    pygame.draw.line(window, YELLOW, (window_center[0] + R, window_center[1]), (window_center[0] + R, window_center[1] - R * math.tan(theta)), 2)
    pygame.draw.circle(window, WHITE, (dot_x, dot_y), 5)
    pygame.draw.line(window, PINK, (window_center[0], window_center[1]), (window_center[0] + R, window_center[1] - R * math.tan(theta)), 2)
    if math.sin(theta) != 0: 
        hyp = math.sqrt (R ** 2 + R ** 2 * math.tan (theta) ** 2)
        opp = hyp * math.sin (theta) 
        pygame.draw.line(window, CYAN, (window_center[0], window_center[1]), (window_center[0], window_center[1] - R / math.sin(theta)), 2)
    if math.tan(theta) != 0:
        hyp = math.sqrt (R ** 2 + R ** 2 * math.tan (theta) ** 2)
        adj = hyp * math.cos (theta)
        pygame.draw.line(window, BLUE, (dot_x, dot_y), (window_center[0], window_center[1] - R / math.sin(theta)), 2)
    pygame.display.flip()
    theta += SPEED 
    if theta > 2 * PI: 
        theta -= 2 * PI 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
            running = False 
    clock.tick(FPS)
pygame.quit()