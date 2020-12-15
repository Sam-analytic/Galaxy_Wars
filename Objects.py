import pygame as pg
from pygame.draw import *
import numpy as np
from random import randint
import constants as const

screen = pg.display.set_mode((const.screen_x,const.screen_y))
BLUE = (0,230,0)
RED = (230,0,0)
GREEN = (0,0,230)
YELLOW = (240,0,240)
WHITE = (240,240,240)
BLACK = (0,0,0)
COLOR = [RED,GREEN,YELLOW,BLUE, WHITE,BLACK]

#numerical execution variable values
max_num = 5
n = 0
x = [0] * 10
y = [0] * 10
vx = [0] * 10
vy = [0] * 10
ax = [0] * 10
ay = [0] * 10
v_o = 15
color = [0] * 10
exist = [False] * 10
planet_num = 5
g = 0.1
r = 10
score = 0
planet_x = []
planet_y = []
planet_r = []
planet_col = []


for i in range(max_num, max_num * 2):
    exist[i] = True


for i in range (planet_num):
    planet_x = [400, 500, 450, 500, 350]
    planet_y = [350, 450, 240, 340, 210]
    planet_r = [10] * 5


def new_ball(ship_x, ship_y, mouse_x, mouse_y):
    '''рисует новый шарик '''
    i = 0
    for k in range (0, max_num * 2):
        if exist[k] == False:
            i = k
            exist[k] = True
            break
    x[i] = ship_x
    y[i] = ship_y
    dx = mouse_x - ship_x
    dy = mouse_y - ship_y
    c_sq = dx ** 2 + dy ** 2
    c = c_sq ** 0.5
    vx[i] = int(v_o * dx / c)
    vy[i] = int(v_o * dy / c)
    circle(screen, COLOR[randint(0, 4)], (ship_x,ship_y), 10)

def mult(x0, y0, x1, y1, x2, y2):
    x1 = x1 - x0
    x2 = x2 - x0
    y1 = y1 - y0
    y2 = y2 - y0
    return x1 * y2 - y1 * x2

def check_hit(ball_num, ship):
    x1 = ship.x - 30
    y1 = ship.y
    x2 = ship.x + 30
    y2 = ship.y + 20
    x3 = ship.x + 30
    y3 = ship.y - 20
    a = mult(x1, y1, x2, y2, x[ball_num], y[ball_num])
    b = mult(x3, y3, x1, y1, x[ball_num], y[ball_num])
    c = mult(x2, y2, x3, y3, x[ball_num], y[ball_num])
    if a * b * c == 0 or a > 0 and b > 0 and c > 0 or a < 0 and b < 0 and c < 0:
        ship.score+=1
        destroy(ball_num)
    for i in range(0, planet_num):

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
        ax += g * planet_r[i] ** 2.4 / l * dx
        ay += g * planet_r[i] ** 2.4 / l * dy
    ax = -int(ax)
    ay = -int(ay)
    return ax, ay

def ball(i, ship2):
    print(i)
    check_hit(i, ship2)
    ax[i], ay[i] = grav(i)
    vx[i] += ax[i]
    vy[i] += ay[i]
    x[i] += vx[i]
    y[i] += vy[i]
    if(x[i] <= 0 or x[i]>=1190 or y[i] <= 0 or y[i] >= 890):
        destroy(i)
        return
    else:
        circle(screen, COLOR[2], (x[i], y[i]), r)

class Space_object():
     '''
     Class makes and gives methods to spherical space objects.
     '''
     def __init__(self,x,y,r):
         self.x = x
         self.y = y
         self.r = r
         circle(screen, COLOR[randint(0, 4)], (self.x,self.y), self.r)

class Middle_cloud(Space_object):
    '''
    Class makes the middle cloud of small black holes that deflect weapon balls.
    '''
    def help(self):
        print('Draws a cloud of random black holes over the screen. #Uses Space_objects.')

    def __init__(self):
        for i in range(planet_num):
            Space_object(planet_x[i], planet_y[i], planet_r[i])


class Ship1(Space_object):
    '''
    This class creates ship object.
    '''
    def __init__(self,index,x,y,i):
        self.x = x
        self.score = 0
        self.y = y
        self.i = i
        self.barrelx = self.x +((-1)**(i+1))*30
        self.barrely = self.y

    def shoot(self, i, colorcode):
        assert colorcode == 4 or colorcode == 5
        #assert False, "colorcode can only be 4 or 5 which corresponds to WHITE or BLACK in the colors list."
        shoot_x = (self.barrelx + 5) + i
        shoot_y = self.barrely
        Space_object(4, shoot_x, shoot_y,5)

    def draw(self):
        i = self.i
        polygon(screen, COLOR[1], [(self.x + ((-1) ** i) * 20, self.y), (self.x + ((-1) ** i) * 30, self.y + 20),
                                   (self.x + ((-1) ** (i + 1)) * 30, self.y), (self.x + ((-1) ** i) * 30, self.y - 20)],
            3)


class Ship2(Ship1):

    def __init__(self,index,ship1):
        X = 1200 - ship1.x
        Y = ship1.y
        I = ship1.i
        self.x = X
        self.y = Y
        self.score = 0
        Ship1(index,X,Y,I+1)
        self.barrelx = X - 30
        self.barrely = Y
    def draw(self):
        X = self.x
        Y = self.y
        polygon(screen, COLOR[2],
                [(X + 20, self.y), (X + 30, self.y + 20), (X - 30, self.y), (X + 30, self.y - 20)],
                3)
    def shoot(self, i, colorcode):
        assert colorcode == 4 or colorcode == 5
        #assert False, "colorcode can only be 4 or 5 which corresponds to WHITE or BLACK in the colors list."
        shoot_x = (self.barrelx - 5) + i
        shoot_y = self.barrely
        Space_object(colorcode,shoot_x, shoot_y,5)

    #def shoot(self):
        #Space_object(4,self.barrelx,self.barrely, )


class Panel:
    '''
    Screen panel that shows score during game time. Creates a screen panel (rectangle with text "Score "
    inside when instantiated.
    arguments - color index, left x, width, height
    '''

    def __init__(self, index, x1,y1,width, height):
        #Rect((left, top), (width, height))
        rect(screen, COLOR[index], (x1,y1, width,height), 2)

