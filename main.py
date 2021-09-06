import pygame as pg
import math
import random

#
pg.init()
window = pg.display.set_mode((800, 600))
pg.display.set_caption("Space Invaders")
icon = pg.image.load('Caption.png')
pg.display.set_icon(icon)
background = pg.image.load('space2.png')

#
playerIcon = pg.image.load('player.png')
playerXcoord = 360
playerYcoord = 470
playerSpeedChange = 0

score = 0
font = pg.font.Font('freesansbold.ttf', 30)
gameOver = pg.font.Font('freesansbold.ttf', 50)
counter = 0


def showScore(scoreXcoord, scoreYcoord):
    totalScore = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(totalScore, (scoreXcoord, scoreYcoord))


def player(playerX, playerY):
    window.blit(playerIcon, (playerX, playerY))


#
enemyIcon = []
enemyXcoord = []
enemyYcoord = []
enemySpeedChange = []
enemyHightChange = []
numOfEnemies = 6
for i in range(numOfEnemies):
    if (i % 2 == 0):
        enemyIcon.append(pg.image.load('enemy1.png'))
    else:
        enemyIcon.append(pg.image.load('enemy2.png'))
    enemyXcoord.append(random.randint(0, 800))
    enemyYcoord.append(random.randint(50, 100))
    enemySpeedChange.append(0.15)
    enemyHightChange.append(40)


def enemy(enemyX, enemyY, i):
    window.blit(enemyIcon[i], (enemyX, enemyY))


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


def collision(enemyXcoord, enemyYcoord, bulletXcoord, bulletYcoord):
    isCollision = math.sqrt((math.pow(enemyXcoord - bulletXcoord, 2)) + (math.pow(enemyYcoord - bulletYcoord, 2)))
    if isCollision < 30:
        return True
    else:
        return False


def end_game_win():
    gameOverTitle = gameOver.render("YOU WIN! CONGRATULATIONS", True, (255, 255, 255))
    window.blit(gameOverTitle, (10, 250))

def end_game_lose():
    gameOverTitle = gameOver.render("YOU LOSE! TRY NEXT TIME!", True, (255, 255, 255))
    window.blit(gameOverTitle, (50, 250))


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
    for i in range(numOfEnemies):
        enemyXcoord[i] += enemySpeedChange[i]
        if enemyXcoord[i] <= 0:
            enemySpeedChange[i] = 0.15
            enemyYcoord[i] += enemyHightChange[i]
        elif enemyXcoord[i] >= 740:
            enemySpeedChange[i] = -0.15
            enemyYcoord[i] += enemyHightChange[i]

        isCollision = collision(enemyXcoord[i], enemyYcoord[i], bulletXcoord, bulletYcoord)
        if isCollision:
            bulletYcoord = 470
            bulletIsReady = "Ready"
            score += 10
            enemyYcoord[i] = 2000
            counter += 1
        enemy(enemyXcoord[i], enemyYcoord[i], i)
        if counter == numOfEnemies:
            end_game_win()
            break
        if enemyYcoord[i]>400 and enemyYcoord[i]<1900 :
            for j in range(numOfEnemies):
                enemyYcoord[j] = 2000
            end_game_lose()
            break

    #
    if bulletIsReady == "Not ready":
        bullet(bulletXcoord, bulletYcoord)
        bulletYcoord -= bulletHightChange
    if bulletYcoord <= 0:
        bulletIsReady = "Ready"
        bulletYcoord = 470

    #
    player(playerXcoord, playerYcoord)
    showScore(10, 10)
    pg.display.update()
