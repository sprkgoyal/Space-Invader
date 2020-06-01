import pygame
from random import randrange

class Player:

    def __init__(self, screen):
        self.playerImg = pygame.image.load('resources/images/player.png')
        self.posX = randrange(0, 736)
        self.posY = 500
        self.speed = 0
        self.screen = screen

    def display(self):
        if self.posX > 736:
            self.posX = 736
        if self.posX < 0:
            self.posX = 0
        self.screen.blit(self.playerImg, (self.posX, self.posY))
        self.posX += self.speed

    def move(self, direction = None):
        if direction == "left":
            self.speed = -5
        elif direction == "right":
            self.speed = 5
        else:
            self.speed = 0

    def position(self):
        return [self.posX, self.posY]