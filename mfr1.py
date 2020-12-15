import pygame as pg
from pygame.draw import *
import Objects as gameob
from random import randint
from Objects import screen     #imports pygame screen from Objects module
import constants as const
import socket as sock
import struct

pg.init()
FPS = const.fps
gametime = const.gametime
max_num = 5

sock = sock.socket()
sock.bind(('127.0.0.1', 8000))
sock.listen(1)
conn, addr = sock.accept()

#sock.connect (('main IP', 14880))

ship1 = gameob.Ship1(randint(0,3),70,400,1)
ship2 = gameob.Ship2(randint(0,3),ship1)
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
    font = pg.font.Font(None, 25)
    text1 = font.render(str(ship1.score), True, gameob.WHITE)
    text2 = font.render(str(ship2.score), True, gameob.WHITE)
    screen.blit(text2, [60, const.screen_y - 40])
    screen.blit(text1, [const.screen_x - 60, const.screen_y - 40])

    clock.tick(FPS)
    Sx = [0] * 15
    for i in range(0, max_num):
        Sx[i] = gameob.x[i]
        Sx[i + max_num] = gameob.y[i]
        Sx[i + max_num * 2] = gameob.exist[i]
    bts = struct.pack('i i 15i', ship1.y, ship1.score, *Sx)
    conn.send(bts)
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

    bts = conn.recv(1024)
    ship2.y, ship2.score, *Sx = struct.unpack('i i 15i', bts)
    print(ship2.score)
    for i in range(max_num, max_num * 2 - 1):
        gameob.x[i] = Sx[i - max_num]
        gameob.y[i] = Sx[i]
        gameob.exist[i] = Sx[i + max_num]
    ship1.draw()
    ship2.draw()
    gameob.Middle_cloud()
    gameob.Panel(0, 0, const.screen_y - 60, 300, 60)
    gameob.Panel(0, const.screen_x - 300, const.screen_y - 60, 300, 60)

    for i in range(0, max_num * 2):
        if gameob.exist[i] == True:
            gameob.ball(i, ship2)
    pg.display.update()
    screen.fill(gameob.COLOR[5])

# print("Player 1 Score is: ", gameob.score)
pg.quit()