import pygame
from DRobj import obj

class Menu: 
    def __init__(self):
        self.bg = obj("assets/start.png",0,0)
        self.change_scene = False

    def draw(self,window):
        self.bg.group.draw(window)

    def status(self):
        if self.change_scene == False:
            return False
        else:
            return True

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True
                print ("gamestart")
    
