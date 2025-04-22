import pygame
from DRobj import obj

class game: 
    def __init__(self):
        self.bg = obj("assets/bg.png", 0 ,0)
        self.bg2 = obj("assets/bg.png",0,-640)
        self.spider = obj("assets/spider1.png",200,200)
        self.change_scene = False

        self.frame = 1

    def draw(self,window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.spider.drawing(window)

    def movebg(self):
        self.bg.sprite.rect[1] +=1
        self.bg2.sprite.rect[1] +=1

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = -640

        if self.bg2.sprite.rect[1] >=640:
            self.bg2.sprite.rect[1] = -640

        #self.spider.    
            
    def update(self):
        self.movebg()
        self.spider.animateSpider()
    
    def status(self):
        if self.change_scene == False: 
            return False
    