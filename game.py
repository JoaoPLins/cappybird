import pygame
from DRobj import obj
from cappy import Cappy
from canos import Canos
from winner import WinnerScreen
from lose import LoseScreen
import random



class Game: 
    def __init__(self, main):
        self.main = main
        self.background = obj("assets/background.png", 0,0)
        self.bg = obj("assets/base.png", 0 ,480)
        self.bg2 = obj("assets/base.png",-256,480)
        #self.botao= obj("assets/information.png",220,10)
       
        self.mouse = pygame.Rect(10,10,10,10) 
        
        self.player = Cappy()
        self.canos = Canos()
        self.canos.AddCano(100,100)

        self.font = pygame.font.SysFont("arial",20,True)
        
        self.change_scene = False
        self.clock = pygame.time.Clock()


        self.pulo = -1
        
        self.boost = False
        self.boostfall = False
        self.gamelost = False
        
        self.gameStatus = 1

        self.janeladeConversa = obj("assets/paused.png",0,0)
        
        #tela com video winner
        self.winner_screen = WinnerScreen()

        


    def write(self,window):
        match self.gameStatus:
            case 1:
                thepoints = self.font.render(str(self.canos.get_points()),1,[0,0,0])
                window.blit(thepoints,(130,50))
            case 2:
                lose_screen = LoseScreen(video_path="assets/perdeu.mp4", bg_sound="assets/underwater-fx.wav")
                restart = lose_screen.draw()

                if restart:
                    self.status = 1  # Por exemplo, 1 = jogo rodando de novo
                else:
                    self.status = 2  # Ou outro status que você usa para sair, por exemplo

                #adicionar transição de bolhas e som quando perder
                #thepoints = self.font.render(str(self.canos.get_points()),1,[0,0,0])
                #window.blit(thepoints,(130,120))
                #theMessage = self.font.render("Você perdeu o jogo!" ,1,[0,0,0])
                #theMessageb = self.font.render("precione R para Reiniciar.",1,[0,0,0])
                #window.blit(theMessage,(50,150))
                #window.blit(theMessageb,(20,190))


    def draw(self,window):
        match self.gameStatus:
            case 1:
                self.background.drawing(window)
                self.canos.drawtheCanos(window)
                self.bg.drawing(window)
                self.bg2.drawing(window)
                self.write(window)
                #self.botao.drawing(window)
                self.player.drawing(window)
            case 2:
                self.background.drawing(window)
                self.canos.drawtheCanos(window)
                self.bg.drawing(window)
                self.bg2.drawing(window)
                self.write(window)
                self.player.drawing(window)
                self.janeladeConversa.drawing(window)
            case 3:
                self.winner_screen.show_message(window, self.font)
   

    def setMouse(self):
        Mousepos = pygame.mouse.get_pos()
        self.mouse.center = Mousepos

    def setStatus(self,status):
        self.gameStatus = status   

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
                self.setStatus(2)
                print("gamelost for pipe up")
            if self.player.cappyRect.collidedict(self.canos.getRectdn(a)):
                self.gamelost = True
                self.setStatus(2)
                print("gamelost for pipe down")
        
    def restart(self):
        self.canos = Canos()
        self.player = Cappy()
        self.canos.AddCano(100,100)
        self.set_start()
        self.setStatus(1)


    def update(self):
        self.clock.tick(100)
        match self.gameStatus:
            case 1:
                self.setMouse()
                self.movebg()
                self.player.update(+1)
                self.Cappypulo()
                self.colision()
                self.canos.AddCano(random.randint(0,100), random.randint(0,100))

                # Verifica vitória
                if self.canos.get_points() >= 3:
                    self.main.updategamestatus(3)
                    self.venceu = True

                # Verifica derrota
                if self.gameStatus == 2:
                    self.gamelost = True
                    self.main.stop_game_sound()
                    self.main.lose_screen.play_video()
                    self.main.updategamestatus(2)
                    self.gamelost = False

            case 2:
                # game over screen
                pass

            case 3:
                # vitória/tela de vídeo
                pass

    def status(self):
        if self.change_scene == False: 
            return False
    
    
    def events(self,event):
        if event.type == pygame.KEYUP:
            if event.dict.get('key') == pygame.K_SPACE:
                self.boost = True
                self.boostfall = False
            #if event.dict.get('key') == pygame.K_r and self.gameStatus ==2:
            #    self.restart()

            if event.dict.get('key') == pygame.K_RETURN and self.gameStatus == 3:
                self.restart()
