import pygame
from DRobj import obj
from cappy import Cappy
import random

class Game: 
    def __init__(self):
        self.background = obj("assets/background.png", 0,0)
        self.bg = obj("assets/base.png", 0 ,400)
        self.bg2 = obj("assets/base.png",-640,400)
        self.player = Cappy()
        self.change_scene = False

        self.frame = 1

    def draw(self,window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.player.drawing(window)
        #self.spider.drawing(window)

    def movebg(self):
        self.bg.sprite.rect[0] +=1
        self.bg2.sprite.rect[0] +=1

        if self.bg.sprite.rect[0] >= 640:
            self.bg.sprite.rect[0] = -640

        if self.bg2.sprite.rect[0] >=640:
            self.bg2.sprite.rect[0] = -640

            
            
    def update(self):
        self.movebg()
        #self.spider.animateSpider()
    
    def status(self):
        if self.change_scene == False: 
            return False
    