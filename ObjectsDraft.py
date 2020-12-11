import pygame as pg
from pygame.draw import *

pg.init()
screen = pg.display.set_mode((1200,800))
#FPS = pass

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLOR = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

ship_x = 150
ship_y = 400
max_num = 5
n = 0
x = [0] * 5
y = [0] * 5
vx = [0] * 5
vy = [0] * 5
ax = [0] * 5
ay = [0] *5
v_o = 15
color = [0] * 5
exist = [False] * 5
planet_num = 2
g = 0.0025
planet_x = [600, 800]
planet_y = [400, 200]
planet_r = [50, 50]




class Space_object():
     '''
     Class makes and gives methods to spherical space objects.
     '''
     def __init__(self,x,y,r,index):
         self.x = x
         self.y = y
         self.r = r
         self.index = index
     def draw(self):
         circle(screen, COLOR[self.index], (self.x,self.y), self.r)



class Ball(Space_object):
    '''
    This class makes circular bullets.
    '''

    def move(self):
        self.x += 1*(mouse_clickx)/dist_ship_mouseclick
        #FIXME
        #mouse_clickx = x coor of click.pos
        #dist_ship_mouseclick = distance between position of mouseclik and ship

class Ship():
    '''
    This class creates ship object.
    '''

    class Ship():
        '''
        This class creates ship object.
        '''

    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index

    def draw(self):
        polygon(screen, COLOR[self.index], [(self.x - 20, self.y), (self.x - 30, self.y + 20), (self.x + 30, self.y),
                                           (self.x - 30, self.y - 20)], 3)


def laser(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 & dy > 0:
        end_x = x1
        end_y = 800
        line(screen, RED, (x1, y1), (end_x, end_y), 3)
        return
    elif dx == 0 & dy < 0:
        end_x = x1
        end_y = 0
        line(screen, RED, (x1, y1), (end_x, end_y), 3)
        return
    if dx != 0:
        k = dy / dx
        c = y1 - k * x1
        if (dx > 0):
            if k < 0:
                end_y = 0
            if k > 0:
                end_y = 800
            if k == 0:
                end_x = 1200
                end_y = y1
            else:
                end_x = (end_y - c) / k
        if (dx < 0):
            if k < 0:
                end_y = 800
            if k > 0:
                end_y = 0
            if k == 0:
                end_x = 0
                end_y = y1
            else:
                end_x = (end_y - c) / k
        x21 = [0] * (planet_num + 1)
        x22 = [0] * (planet_num + 1)
        for i in range(0, planet_num):
            a = planet_x[i]
            b = planet_y[i]
            r = planet_r[i]
            be = (a + k * b - c * k)
            ae = (k ** 2 + 1)
            de = be ** 2 - ae * (a ** 2 + c ** 2 - 2 * b * c + b ** 2 - r ** 2)
            if de > 0:
                if dx > 0:
                    x21[i] = int((be - de ** 0.5) / ae)
                    x22[i] = int(abs(x21[i] - x1))
                else:
                    x21[i] = int((be + de ** 0.5) / ae)
                    x22[i] = int(abs(x21[i] - x1))
        mini = planet_num
        x22[mini] = 1200
        print(x21 + x22)
        for i in range(0, planet_num):
            if x21[i] != 0 & x22[i] < x22[mini]:
                mini = i
        if mini != planet_num:
            end_x = x21[mini]
            end_y = k * end_x + c
        print(mini, end_x, end_y, k, c)
        line(screen, RED, (x1, y1), (end_x, end_y), 3)



ball = Ball(600,600,20, 1)

pg.display.update()

