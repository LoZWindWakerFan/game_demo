import pygame as pg
from sys import exit

from char_functions import *

pg.init()

#Window 
screen = pg.display.set_mode((850, 500))
pg.display.set_caption("Prototype/Demo")

#Clock
clock = pg.time.Clock()

#Surfaces
skybox = pg.Surface((850,500))
skybox.fill("Light Blue")

#Game loop
active = True
while active:
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            pg.quit()
            exit()
    
    #Surfaces 
    screen.blit(skybox, (0,0))
    screen.blit(player, (50,0))
    screen.blit(player, (450,0))
    screen.blit(player, (250, 450))


    pg.display.update()
    clock.tick(60)