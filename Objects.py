import pygame as pg
from pygame.draw import *

pg.init()
screen = pg.display.set_mode((1200,800))
#FPS = pass

BLUE = (0,230,0)
RED = (230,0,0)
GREEN = (0,0,230)
YELLOW = (240,0,240)
COLOR = [RED,GREEN,YELLOW,BLUE]





class Space_object():
     '''
     Class makes and gives methods to spherical space objects.
     '''
     def __init__(self,x,y,r,index):
         self.x = x
         self.y = y
         self.r = r
         circle(screen, COLOR[index], (self.x,self.y), self.r)



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
    def __init__(self,x,y,index):
        self.x = x
        self.y = y
        polygon(screen, COLOR[index], [(self.x - 20, self.y), (self.x - 30, self.y +20), (self.x + 30, self.y),(self.x - 30,self.y - 20)], 3)

    def pair(self,index):
        X = 1200 - self.x
        polygon(screen, COLOR[index],
                [(X + 20, self.y), (X + 30, self.y + 20), (X - 30, self.y), (X + 30, self.y - 20)],
                3)



sun = Space_object(100,100,40,2)
spaceship = Ship(400,400,3)
spaceship.pair(2)
ball = Ball(600,600,20, 1)

pg.display.update()

