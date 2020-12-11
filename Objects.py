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

    def shoot(self, i,colorcode):
        assert colorcode == 4 or colorcode == 5
        #assert False, "colorcode can only be 4 or 5 which corresponds to WHITE or BLACK in the colors list."
        shoot_x = (self.barrelx + 5) + i
        shoot_y = self.barrely
        Space_object(colorcode,shoot_x, shoot_y,5)


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

