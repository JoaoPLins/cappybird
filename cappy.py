from DRobj import obj
import pygame

class Cappy():
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load("assets/cappy.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = 100
        self.sprite.rect[1] = 100
        self.cappyRect = pygame.Rect(self.sprite.rect[0],self.sprite.rect[1],10,10)
        self.frame = 1


    def drawing(self, window):
        self.group.draw(window)

    def update(self,y):
        self.sprite.rect[1] = self.sprite.rect[1] + y
        self.cappyRect.update(self.sprite.rect[0],self.sprite.rect[1],10,10)

    def GetTheCappyNumber(self):
        return self.sprite.rect[1]

        