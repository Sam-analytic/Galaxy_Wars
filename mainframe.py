import pygame as pg
from pygame.draw import *
import Objects as gameob
from random import randint

pg.init()
screen = pg.display.set_mode((1200,800))
FPS = 32
max_num = 5

'''#This is an example array made for your help, quote it in ''' ''' and write your code.
sun = gameob.Space_object(2,100,100,40)
spaceship = gameob.Ship(3,400,400)
ship2 = gameob.Ship.pair(spaceship,2)
ship2
ball = gameob.Ball(1,600,600,20)

gameob.Panel(2,200,200,300,100)
'''

ship1 = gameob.Ship1(randint(0,3),70,400,1)
#print(ship1.barrelx)
ship2 = gameob.Ship2(randint(0,3),ship1)
#print(ship2.barrelx)
init_cloud = gameob.Middle_cloud()
init_cloud
gameob.Panel(0,0,740, 300,60)
gameob.Panel(0,900,740,300,60)
pg.display.update()
clock = pg.time.Clock()
finished = False

#initial shooting condition = instantiation of bullets
i = -1


while not finished:
    i += 1

    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                ship1.y -= 10
            if event.key == pg.K_s:
                ship1.y += 10
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            ship1.x = 100
            gameob.new_ball(ship1.x, ship1.y, mouse_x, mouse_y)

            #bullet_list
            #pg.display.update()
    ship1.draw()
    # print(ship1.barrelx)
    ship2.draw()
    # print(ship2.barrelx)
    gameob.Middle_cloud()
    gameob.Panel(0, 0, 740, 300, 60)
    gameob.Panel(0, 900, 740, 300, 60)
    for i in range(0, max_num):
        if gameob.exist[i] == True:
            gameob.ball(i)
    pg.display.update()
    screen.fill(gameob.COLOR[5])
    '''for bullet in bullet_list:
        bullet
    pg.display.update()
    for bullet in bullet:
        bullet.colorcode = 5
        bullet.i = i + 1
    pg.display.update()'''


pg.quit()