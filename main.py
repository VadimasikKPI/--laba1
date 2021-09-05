import pygame as pg
#
pg.init()
window = pg.display.set_mode((800, 600))
pg.display.set_caption("Space Invaders")
icon = pg.image.load('Caption.png')
pg.display.set_icon(icon)
background = pg.image.load('space.png')

#
playerIcon = pg.image.load('player.png')
playerXcoord = 360
playerYcoord = 470
playerSpeedChange = 0
def player(playerX, playerY):
    window.blit(playerIcon, (playerX, playerY))

#
enemyIcon = pg.image.load('enemy1.png')
enemyXcoord = 360
enemyYcoord = 50
enemySpeedChange = 0.15
enemyHightChange = 40
def enemy(enemyX, enemyY):
    window.blit(enemyIcon, (enemyX, enemyY))

#
bulletIcon = pg.image.load('star_bullet.png')
bulletXcoord = 360
bulletYcoord = 470
bulletHightChange = 0.45
bulletIsReady = "Ready"
def bullet(bulletX, bulletY):
    global bulletIsReady
    bulletIsReady = "Not ready"
    window.blit(bulletIcon, (bulletX + 32, bulletY + 10))

#
isClose = True
while isClose:
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isClose = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                playerSpeedChange = 0.5
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                playerSpeedChange = -0.5
            if event.key == pg.K_SPACE:
                if bulletIsReady == "Ready":
                    bulletXcoord = playerXcoord
                    bullet(bulletXcoord, bulletYcoord)
                    bulletYcoord -= bulletHightChange
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_d or event.key == pg.K_a:
                playerSpeedChange = 0

    #
    playerXcoord += playerSpeedChange
    if playerXcoord <= 0:
        playerXcoord = 0
    elif playerXcoord >= 740:
        playerXcoord = 740

    #
    enemyXcoord += enemySpeedChange
    if enemyXcoord <= 0:
        enemySpeedChange = 0.15
        enemyYcoord += enemyHightChange
    elif enemyXcoord >= 740:
        enemySpeedChange = -0.15
        enemyYcoord += enemyHightChange

    #
    if bulletIsReady == "Not ready":
        bullet(bulletXcoord, bulletYcoord)
        bulletYcoord -= bulletHightChange
    if bulletYcoord <=0:
        bulletIsReady = "Ready"
        bulletYcoord = 470

    #
    player(playerXcoord, playerYcoord)
    enemy(enemyXcoord, enemyYcoord)
    pg.display.update()