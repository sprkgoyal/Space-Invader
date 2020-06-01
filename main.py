import pygame
from math import sqrt, pow
from bullet import Bullet
from enemy import Enemy
from player import Player
from pygame import mixer
from random import randrange

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space Invader')
clock = pygame.time.Clock()
background = pygame.image.load('resources/images/background.jpg')
mixer.music.load('resources/sounds/backgroundmusic.mp3')
mixer.music.play(-1)

isrunning = True
enemy = [Enemy(screen) for i in range(6)]
player = Player(screen)
bullet = [Bullet(screen) for i in range(10)]

netscore = 0
highscore = int(open('resources/highscore.txt', 'r').readline())

font = pygame.font.SysFont('Copperplate Gothic', 15, True)
def printScoreBoard():
    pygame.draw.rect(screen, (0,0,0), [[0,0], [160, 55]])
    score = font.render("Score : " + str(netscore), True, (255, 255, 255))
    mscore = font.render("High Score : " + str(highscore), True, (255, 255, 255))
    screen.blit(score, (10, 10))
    screen.blit(mscore, (10, 30))

font2 = pygame.font.SysFont('Castellar', 80, True)
gameover = font2.render("GAME OVER", True, (255, 255, 255))
def printGameOver():
    screen.blit(gameover, (110, 240))

play = False
font3 = pygame.font.SysFont('Castellar', 75)
font4 = pygame.font.SysFont('Castellar', 15)
startgame = font3.render("Space Invader", True, (255, 255, 255))
entertostart = font4.render("Press Enter to Start", True, (255, 255, 255))
def printStartGame():
    screen.blit(startgame, (80, 240))
    screen.blit(entertostart, (310, 325))

while isrunning:

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open('resources/highscore.txt', 'w').write("{}".format(max(netscore, highscore)))
            isrunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and play:
                for i in range(10):
                    if not bullet[i].isfired():
                        pos = player.position()
                        bullet[i].fire(pos[0]+16, pos[1])
                        break
            if event.key == pygame.K_RIGHT and play:
                player.move('right')
            if event.key == pygame.K_LEFT and play:
                player.move('left')
            if event.key == pygame.K_RETURN:
                play = True
        if event.type == pygame.KEYUP and play:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.move(None)

    if play:

        for i in range(10):
            if bullet[i].isfired():
                bullet[i].fire()
        
        player.display()

        for i in range(6):
            enemy[i].display()

        for i in range(10):
            for j in range(6):
                a = bullet[i].position()
                b = enemy[j].position()
                if sqrt(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2)) <= 40:
                    enemy[j].hit()
                    bullet[i].stop()
                    if enemy[j].isdead():
                        netscore += 1

        for i in range(6):
            enpos = enemy[i].position()
            if enpos[1] + 64 >= 500:
                for j in range(6):
                    enemy[j].setposition([200, 700])
                    enemy[j].setspeed(0)
                printGameOver()
                break

    else:
        printStartGame()

    printScoreBoard()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
