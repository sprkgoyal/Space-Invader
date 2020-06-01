import pygame
from random import randrange, choice
from pygame import mixer

class Enemy:

    def __init__(self, screen):
        self.enemyImg = pygame.image.load('resources/images/enemy.png')
        self.healthbar1 = pygame.image.load('resources/images/health1.png')
        self.healthbar2 = pygame.image.load('resources/images/health2.png')
        self.healthbar3 = pygame.image.load('resources/images/health3.png')
        self.blastSound = mixer.Sound('resources/sounds/blast.wav')
        self.blastSound.set_volume(0.5)
        self.posX = randrange(0, 736)
        self.posY = randrange(70, 150)
        self.speed = randrange(3, 4) * choice([-1, 1])
        self.screen = screen
        self.health = 3

    def display(self):
        if self.posX <= 0 or self.posX >= 736:
            self.speed = -self.speed
            self.posY += 40
        if self.health == 3:
            self.screen.blit(self.healthbar3, (self.posX, self.posY-2))
        if self.health == 2:
            self.screen.blit(self.healthbar2, (self.posX, self.posY-2))
        if self.health == 1:
            self.screen.blit(self.healthbar1, (self.posX, self.posY-2))
        self.screen.blit(self.enemyImg, (self.posX, self.posY))
        self.posX += self.speed

    def setspeed(self, s):
        self.speed = s
    
    def position(self):
        return [self.posX+32, self.posY+32]

    def hit(self):
        self.blastSound.play()
        self.health -= 1

    def isdead(self):
        if self.health == 0:
            self.__init__(self.screen)
            return True
        return False
    
    def setposition(self, coordinate):
        self.posX, self.posY = coordinate
