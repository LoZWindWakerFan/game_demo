import pygame as pg
from sys import exit

pg.init()

#Window 
screen = pg.display.set_mode((850, 500))
pg.display.set_caption("Prototype/Demo")

#Clock
clock = pg.time.Clock()

#Game loop
active = True
while active:
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            pg.quit()
            exit()


pg.display.update()
clock.tick(60)