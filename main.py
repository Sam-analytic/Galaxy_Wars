import pygame
from pygame.draw import *
from random import randint
import gameplay_objects
import ingameconstants

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))

# SECTION WITH COLORS 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#numerical execution variable values
ship_x = 150
ship_y = 400
max_num = 5
n = 0
x = [0] * 5
y = [0] * 5
r = [0] * 5
vx = [0] * 5
vy = [0] * 5
ax = [0] * 5
ay = [0] *5
v_o = 15
color = [0] * 5
exist = [False] * max_num
planet_num = 2
g = 0.0025
planet_x = [600, 800]
planet_y = [400, 200]
planet_r = [50, 50]

def new_ball(ship_x, ship_y, mouse_x, mouse_y):
    '''рисует новый шарик '''
    i = 0
    for k in range (0, max_num):
        if exist[k] == False:
            i = k
            exist[k] = True
            break
    #x[i] = ship_x
    #y[i] = ship_y
    #r[i] = 10
    dx = mouse_x - ship_x
    dy = mouse_y - ship_y
    c_sq = dx ** 2 + dy ** 2
    c = c_sq ** 0.5
    vx[i] = int(v_o * dx / c)
    vy[i] = int(v_o * dy / c)
    color[i] = COLORS[randint(0, 5)]
    circle(screen, color[i], (ship_x,ship_y), 10)

def check_hit(ball_num):
    for i in range(0, planet_num):
        print(i)
        l = (x[ball_num] - planet_x[i]) ** 2 + (y[ball_num] - planet_y[i]) ** 2
        if l <= planet_r[i] ** 2:
            destroy(ball_num)
            return True
    return False

def destroy(i):
    global n
    exist[i] = False
    n -= 1

def grav(num):
    ax = 0
    ay = 0
    for i in range(0, planet_num):
        dx = x[num] - planet_x[i]
        dy = y[num] - planet_y[i]
        l = dx ** 2 + dy ** 2
        ax += g * planet_r[i] ** 3 / l * dx
        ay += g * planet_r[i] ** 3 / l * dy
    ax = -int(ax)
    ay = -int(ay)
    return ax, ay

def ball(i):
    ax[i], ay[i] = grav(i)
    vx[i] += ax[i]
    vy[i] += ay[i]
    x[i] += vx[i]
    y[i] += vy[i]
    if(x[i] <= 0 or x[i]>=1120 or y[i] <= 0 or y[i] >= 720):
        destroy(i)
        return
    else:
        circle(screen, color[i], (x[i], y[i]), r[i])

def ship():
    polygon(screen, RED, ((ship_x - 40, ship_y - 30), (ship_x - 40, ship_y + 30), (ship_x + 40, ship_y + 30), (ship_x + 40, ship_y - 30)), 0)

def laser():
    dx = mouse_x - ship_x
    dy = mouse_y - ship_y
    k = dy / dx
    b = ship_y - k * ship_x
    if(dx > 0):
        if k < 0:
            end_y = 0
        if k > 0:
            end_y = 800
        if k == 0:
            end_x = 1200
            end_y = ship_y
        else:
            end_x = (end_y - b) / k
    if(dx < 0):
        if k < 0:
            end_y = 800
        if k > 0:
            end_y = 0
        if k == 0:
            end_x = 0
            end_y = ship_y
        else:
            end_x = (end_y - b) / k
    for i in range(0, planet_num):
        l = (k * planet_x[i] - planet_y[i] + b) ** 2
        l /= k ** 2 + 1
        #if l < planet_r[i] ** 2:
            #find coordinates
    line(screen, RED, (ship_x, ship_y), (end_x, end_y), 3)

def planets():
    for i in range(0, planet_num):
        circle(screen, BLUE, (planet_x[i], planet_y[i]), planet_r[i])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

score = 0

while not finished:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            dx = mouse_x - ship_x
            dy = mouse_y - ship_y
            new_ball(ship_x, ship_y, mouse_x, mouse_y)
            laser()

    for i in range(0, max_num):
        if exist[i] == True:
            ball(i)
            check_hit(i)
    ship()
    planets()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()