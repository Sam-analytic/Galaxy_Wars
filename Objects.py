import pygame as pg
from pygame.draw import *
import numpy as np
from random import randint

screen = pg.display.set_mode((1200,800))
#FPS = pass


BLUE = (0,230,0)
RED = (230,0,0)
GREEN = (0,0,230)
YELLOW = (240,0,240)
WHITE = (240,240,240)
BLACK = (0,0,0)
COLOR = [RED,GREEN,YELLOW,BLUE, WHITE,BLACK]

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
    x[i] = ship_x
    y[i] = ship_y
    r[i] = 10
    dx = mouse_x - ship_x
    dy = mouse_y - ship_y
    c_sq = dx ** 2 + dy ** 2
    c = c_sq ** 0.5
    vx[i] = int(v_o * dx / c)
    vy[i] = int(v_o * dy / c)
    color[i] = COLOR[randint(0, 4)]
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

class Space_object():
     '''
     Class makes and gives methods to spherical space objects.
     '''
     def __init__(self,index,x,y,r):
         self.x = x
         self.y = y
         self.r = r
         circle(screen, COLOR[index], (self.x,self.y), self.r)

class Middle_cloud(Space_object):
    '''
    Class makes the middle cloud of small black holes that deflect weapon balls.
    '''
    def help(self):
        print('Draws a cloud of random black holes over the screen. #Uses Space_objects.')

    def __init__(self):
        for i in range (randint(7,12)):
            #index  = randint(0,3)
            #x = 600 + randint(-200,200)
            #y = 400 + randint(-200, 200)
            Space_object(randint(0,3),600 + randint(-150,150),400 + randint(-350, 350),10 )


class Ship1(Space_object):
    '''
    This class creates ship object.
    '''
    def __init__(self,index,x,y,i):
        self.x = x
        self.y = y
        self.i = i
        polygon(screen, COLOR[index], [(self.x + ((-1)**i)*20, self.y), (self.x +((-1)**i)*30, self.y +20), (self.x +((-1)**(i+1))*30, self.y),(self.x +((-1)**i)*30,self.y - 20)], 3)
        self.barrelx = self.x +((-1)**(i+1))*30
        self.barrely = self.y

    def shoot(self, i, colorcode):
        assert colorcode == 4 or colorcode == 5
        #assert False, "colorcode can only be 4 or 5 which corresponds to WHITE or BLACK in the colors list."
        shoot_x = (self.barrelx + 5) + i
        shoot_y = self.barrely
        Space_object(4, shoot_x, shoot_y,5)



class Ship2(Ship1):

    def __init__(self,index,ship1):
        X = 1200 - ship1.x
        Y = ship1.y
        I = ship1.i
        Ship1(index,X,Y,I+1)
        '''polygon(screen, COLOR[index],
                [(X + 20, self.y), (X + 30, self.y + 20), (X - 30, self.y), (X + 30, self.y - 20)],
                3)'''
        self.barrelx = X - 30
        self.barrely = Y

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

