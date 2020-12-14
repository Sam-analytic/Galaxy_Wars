import pygame as pg
from pygame.draw import *
import Objects as gameob
from random import randint
import socket as sock
import struct 

pg.init()
screen = pg.display.set_mode((1200,800))
FPS = 32
gametime = 200
max_num = 5

sock = sock.socket()
sock.connect (('127.0.0.1', 139))
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

    bts = sock.recv(1024)
    print(len(bts))
    ship1.y = struct.unpack('<i', bts)
    i += 1
    count_ship_1 = 0
    count_ship_2 = 0
    balls_list = []

    font = pg.font.Font(None, 25)
    text1 = font.render(str(ship1.score), True, gameob.WHITE)
    screen.blit(text1, [100, 100])
    text2 = font.render(str(ship2.score), True, gameob.WHITE)
    screen.blit(text2, [1100, 100])
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
             finished = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                ship2.y -= 10
                   
            if event.key == pg.K_s:
                ship2.y += 10
                    
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse2_x, mouse2_y = event.pos
                
            gameob.new_ball(ship2.x - 5, ship2.y, mouse2_x, mouse2_y)

            #bullet_list
            #pg.display.update()
    bts = struct.pack('i', ship2.y)
    print (bts)
    sock.send(bts)
    ship1.draw()
    # print(ship1.barrelx)
    ship2.draw()
    # print(ship2.barrelx)
    gameob.Middle_cloud()
    gameob.Panel(0, 0, 740, 300, 60)
    gameob.Panel(0, 900, 740, 300, 60)
    for i in range(0, max_num):
        if gameob.exist[i] == True:
            gameob.ball(i, ship1)
    pg.display.update()
    screen.fill(gameob.COLOR[5])


pg.quit()