import pygame as pg

pg.init()
window = pg.display.set_mode((700, 600))
pg.display.set_caption("Space Invaders")
icon = pg.image.load('Caption.png')
pg.display.set_icon(icon)


playerIcon = pg.image.load('player.png')

def player(playerX, playerY):
    window.blit(playerIcon, (playerX, playerY))


isClose = True
while isClose:
    window.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isClose = False
    player(360, 400)
    pg.display.update()