import pygame
from DRobj import obj
from cappy import Cappy
from canos import Canos
import random



class Game: 
    def __init__(self):
        self.background = obj("assets/background.png", 0,0)
        self.bg = obj("assets/base.png", 0 ,480)
        self.bg2 = obj("assets/base.png",-256,480)
        self.player = Cappy()
        self.canos = Canos()
        self.canos.AddCano(1,0)
        self.change_scene = False
        self.clock = pygame.time.Clock()
        self.pulo = -1
        self.boost = False
        self.boostfall = False
        self.gamelost = False

    def draw(self,window):
        self.background.drawing(window)
        self.canos.drawtheCanos(window)
        self.bg.drawing(window)
        self.bg2.drawing(window)
        
        self.player.drawing(window)
       

    def movebg(self):

         

        self.bg.sprite.rect[0] -=1
        self.bg2.sprite.rect[0] -=1
        self.canos.updateTheCanos()

        if self.bg.sprite.rect[0] <= -256:
            self.bg.sprite.rect[0] = 256

        if self.bg2.sprite.rect[0] <= -256:
            self.bg2.sprite.rect[0] = 256

    def set_start(self):
        pass
        pygame.init()

    def Cappypulo(self):
        if self.boost == True:
            if self.boostfall == False:
                if self.pulo > -10:
                    self.player.update(self.pulo)
                    self.pulo = self.pulo-1
                else:
                    self.boostfall = True
            else:
                if self.pulo < 0:
                    self.player.update(self.pulo)
                    self.pulo = self.pulo+1
                else:
                    self.pulo = 0
                    self.boost = False
                    self.boostfall = False


    def colision(self):
        for a in range(self.canos.getCanoNcanos()):
            if self.player.cappyRect.collidedict(self.canos.getRectup(a)):
                self.gamelost = True
                print("gamelost for pipe up")
            if self.player.cappyRect.collidedict(self.canos.getRectdn(a)):
                self.gamelost = True
                print("gamelost for pipe down")
            
    def update(self):
        self.clock.tick(250) 
        self.movebg()
        self.player.update(+1)
        self.Cappypulo()
        self.colision()
        self.canos.AddCano(random.randint(0,100),random.randint(0,100))
    
    def status(self):
        if self.change_scene == False: 
            return False
    
    def events(self,event):
        if event.type == pygame.KEYUP:
            if event.dict.get('key') == pygame.K_SPACE:
                self.boost = True
                self.boostfall = False
