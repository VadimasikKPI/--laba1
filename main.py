import pygame as pg

pg.init()
window = pg.display.set_mode((700, 600))
pg.display.set_caption("Space Invaders")
icon = pg.image.load('')
pg.display.set_icon(icon)

isClose = True
while isClose:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isClose = False

    window.fill((0, 0, 0))
    pg.display.update()