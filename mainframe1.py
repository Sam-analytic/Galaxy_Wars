import pygame as pg
from pygame.draw import *
import Objects as gameob
from random import randint
import socket as sock
import struct 

pg.init()
screen = pg.display.set_mode((1200,800))
FPS = 32
gametime = 30
max_num = 5

sock = sock.socket()
sock.bind(('127.0.0.1', 14880))
sock.listen(1)
conn, addr = sock.accept()

#sock.connect (('main IP', 14880))

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
start_ticks=pg.time.get_ticks() #starter tick



while not finished:
    #TIMER
    seconds = (pg.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
    if seconds > gametime:  # if more than 10 seconds close the game
        break

    i += 1
    count_ship_1 = 0
    count_ship_2 = 0
    balls_list = []

    clock.tick(FPS)
    struct.pack('iii', ship1.y, mouse1.x, mouse1.y)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                ship1.y -= 10
            if event.key == pg.K_s:
                ship1.y += 10

        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse1_x, mouse1_y = event.pos
            gameob.new_ball(ship1.x + 5, ship1.y, mouse1_x, mouse1_y)
            #bals_list.append([])
        """gameob.new_ball(ship2.x - 5, ship2.y, mouse_x,mouse1_ye_y)"""

            """ for event in pg.event.get():
            if event.type == pg.QUIT:
                 finished = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    ship2.y -= 10
                   
                if event.key == pg.K_s:
                    ship2.y += 10
                    
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse2_x, mouse2_y = event.pos
                
                gameob.new_ball(ship2.x - 5, ship2.y, mouse2_x, mouse2_y)"""

            #bullet_list
            #pg.display.update()
    
    a = sock.recv()
    struct.unpack('iii', a)
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