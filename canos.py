import pygame
import random
from DRobj import obj

class Canos():
    def __init__(self):
        self.canoID = []
        self.CanoObjup = []
        self.CanoObjdn = []
        self.canoImage = ["assets/pipe.png","assets/pipe2.png"]
        #self.counter = 0
        self.ticks =200
        self.points = 0

    def AddCano(self,v,base):
        if self.ticks == 200:
            theBase = 200 + base
            Diffeerence = -200-v
            #self.canoID.append(self.counter)
            self.CanoObjup.append(obj(self.canoImage[0],280,theBase))
            self.CanoObjdn.append(obj(self.canoImage[1],280,Diffeerence))
            self.ticks = 0 
        else:
            self.ticks = self.ticks + 1
    
    def get_points(self):
        return self.points

    def removethecanos(self):
        a=0
        for a in  range(len(self.CanoObjup)-1):
            if self.CanoObjdn[a].sprite.rect[0] == -100:
                self.CanoObjup.pop(a)
                self.CanoObjdn.pop(a)
                print("canoremoved")
    
    def drawtheCanos(self,window):
        a=0
        for a in range(len(self.CanoObjup)):
            self.CanoObjup[a].drawing(window)
            self.CanoObjdn[a].drawing(window)
    
    def updateTheCanos(self):
        
        a=0
        for a in range(len(self.CanoObjup)):
            self.CanoObjup[a].updateposs()
            self.CanoObjdn[a].updateposs()
            if self.CanoObjdn[a].givethepoints() == 1:
                self.points = self.points +1
                print(self.points)
            


        self.removethecanos()

    def getCanoNcanos(self):
        return len(self.CanoObjup)

    def getRectup(self,a):
        
        return self.CanoObjup[a].group.spritedict
    
    def getRectdn(self,a):
        return self.CanoObjdn[a].group.spritedict

    
        