import pygame
from pygame import mixer

class Bullet:

    def __init__(self, screen):
        self.bulletImg = pygame.image.load('resources/images/bullet.png')
        self.bulletSound = mixer.Sound('resources/sounds/laser.wav')
        self.bulletSound.set_volume(0.5)
        self.state = "ready"
        self.posX = 0
        self.posY = 0
        self.speed = -10
        self.screen = screen

    def fire(self, x = None, y = None):
        if not self.isfired():
            self.bulletSound.play()
            self.posX = x
            self.posY = y
        self.state = "fire"
        self.screen.blit(self.bulletImg, (self.posX, self.posY))
        self.posY += self.speed
        if self.posY <= -32:
            self.state = "ready"

    def isfired(self):
        return self.state == "fire"

    def setspeed(self, s):
        self.speed = -s

    def position(self):
        return [self.posX+16, self.posY+16]

    def stop(self):
        self.state = "ready"
        self.__init__(self.screen)
