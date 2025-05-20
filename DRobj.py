import pygame

class obj:
    def __init__(self,image,x,y):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1

    
    def drawing(self, window):
        self.group.draw(window)

    def updateposs(self):
        self.sprite.rect[0] = self.sprite.rect[0] -1

    def colision(self):
        self.sprite.rect.collision()