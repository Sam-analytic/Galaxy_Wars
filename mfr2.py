import pygame as pg
from pygame.draw import *
import Objects as gameob
from Objects import screen            #imports pygame screen from Objects module
from random import randint
import constants as const
import socket as sock
import struct 

a = input("Please enter your IP address: ")
sock.connect ((a, 8000))
pg.init()
FPS = const.fps
gametime = const.gametime                     #maximum number of balls shot by one ship at any moment on the screen
max_num = const.max_num

sock = sock.socket()

ship1 = gameob.Ship1(randint(0, 3), 70, 400, 1, 0)
ship1.score = 0
ship2 = gameob.Ship2(randint(0,3),ship1, 0)
ship2.score = 0
init_cloud = gameob.Middle_cloud()
init_cloud
gameob.Panel(0, 0, 740, 300, 60)
gameob.Panel(0, 900, 740, 300, 60)
pg.display.update()
clock = pg.time.Clock()
finished = False

#initial shooting condition = instantiation of bullets
i = -1
# start_ticks=pg.time.get_ticks() #starter tick



while not finished:
    #TIMER
    # seconds = (pg.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
    # if seconds > gametime:  # if more than 10 seconds close the game
    #     break

    bts = sock.recv(1024)
    Sx = [0] * 15
    ship1.y, ship2.score, *Sx = struct.unpack('i i 15i', bts)
    i += 1
    for i in range(max_num, max_num * 2 - 1):
        gameob.x[i] = Sx[i - max_num]
        gameob.y[i] = Sx[i]
        gameob.exist[i] = Sx[i + max_num]
    count_ship_1 = 0
    count_ship_2 = 0
    balls_list = []

    font = pg.font.Font(None, 25)
    text1 = font.render(str(ship1.score), True, gameob.WHITE)
    text2 = font.render(str(ship2.score), True, gameob.WHITE)
    screen.blit(text2, [60, const.screen_y - 40])
    screen.blit(text1, [const.screen_x - 60, const.screen_y - 40])
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
    for i in range(0, max_num):
        Sx[i] = gameob.x[i]
        Sx[i + max_num] = gameob.y[i]
        Sx[i + max_num * 2] = gameob.exist[i]
    bts = struct.pack('i i 15i', ship2.y, ship1.score, *Sx)
    sock.send(bts)
    ship1.draw()
    ship2.draw()
    gameob.Middle_cloud()
    gameob.Panel(0, 0, const.screen_y - 60, 300, 60)
    gameob.Panel(0, const.screen_x - 300, const.screen_y - 60, 300, 60)

    for i in range(0, max_num * 2):
        if gameob.exist[i] == True:
            gameob.ball(i, ship1)
    pg.display.update()
    screen.fill(gameob.COLOR[5])


pg.quit()