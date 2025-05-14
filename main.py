import pygame
from DRobj import obj
from menu import Menu
from game import Game

#precisa testar     
pygame.init()
icon = pygame.image.load("assets/cappy.png")

class Main:
    def __init__(self,sizex,sizey,title):

        self.window = pygame.display.set_mode((sizex,sizey))
        self.title = pygame.display.set_caption(title)
        self.icon = pygame.display.set_icon(icon)

        self.loop = True
        self.menu = Menu()
        self.game = Game()
        self.gameStatus = 0
        

    def updategamestatus(self,arg):
        self.gameStatus = arg

    def draw(self):
        
        match self.gameStatus:

            case 0:
                self.menu.draw(self.window)
            
            case 1:
                self.game.draw(self.window)
                self.game.update()
                
        


    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            match self.gameStatus:
                case 0: 
                    self.menu.events(events)
                case 1:
                    self.game.events(events)    
    
    
    def update(self):
        
        while self.loop:
            self.draw()
            self.events()
            if self.menu.change_scene == True:
                            
                self.updategamestatus(1)
                self.game.set_start()
            
            pygame.display.update()




game = Main(288,512,"CappyBird")
game.update()


