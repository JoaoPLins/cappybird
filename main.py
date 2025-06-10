import pygame
from DRobj import obj
from menu import Menu
from game import Game
from instruction import InstructionScreen
from winner import WinnerScreen
from lose import LoseScreen

import sys

#precisa testar     
pygame.init()
icon = pygame.image.load("assets/icon.png")
FPS = 10

class Main:
    def __init__(self,sizex,sizey,title):

        #informacoes de tamanho
        self.window = pygame.display.set_mode((sizex,sizey))
        self.title = pygame.display.set_caption(title)
        self.icon = pygame.display.set_icon(icon)
        
        # onde você cria o Game
        self.game = Game(self)
        
        self.loop = True
        self.menu = Menu(self)

        self.underwater_fx = pygame.mixer.Sound("assets/underwater-fx.wav")
        self.fx_started = False
        self.jump_sound = pygame.mixer.Sound("assets/diving-fx.wav")  #som underwater
        self.jump_sound.set_volume(0.6)  # ajuste de volume
        #definir url do som para parar posteriormente
        self.winner_screen = WinnerScreen(self,bg_sound="assets/underwater-fx.wav")
        self.lose_screen = LoseScreen(self, bg_sound="assets/underwater-fx.wav")

        self.gameStatus = 0
        #0 menu, 
        #1 Game,
        #2 Instruction?==
        #3 ==
        #4 ==

        #tela de instrucoes tecla M
        self.instruction = InstructionScreen(self)
        self.instruction_already_shown = False

        self.lose_screen = LoseScreen(self)

        
     

    def updategamestatus(self,arg):
        self.gameStatus = arg
        print(self.gameStatus)
        if arg == 1:
            self.game.set_start()
            self.game.setStatus(1)
            if not self.fx_started:
                pygame.mixer.music.load("assets/underwater-fx.wav")
                self.underwater_fx.play(-1)
                self.fx_started = True

            if not self.instruction_already_shown:
                    #self.instruction.visible = False
                    self.instruction_already_shown = True
            else:
                    self.instruction.visible = False
        elif arg == 3:
                self.stop_game_sound()
                self.winner_screen.play_video()

    def draw(self):
        
        match self.gameStatus:

            case 0:
                self.menu.draw(self.window)
            
            case 1:
                self.game.draw(self.window)
                self.game.update()

            # Desenhar a tela de instrução 
            case 2:
                self.instruction.draw(self.window)

    def quit(self):
        self.loop = False

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            match self.gameStatus:
                case 0: 
                    self.menu.events(events)
                    if events.type == pygame.KEYDOWN and events.key == pygame.K_m:
                        if not self.instruction.visible:
                            self.updategamestatus(2)
                case 1:
                    self.game.events(events)
                    if events.type == pygame.KEYDOWN and events.key == pygame.K_SPACE:
                        self.jump_sound.play()    
            
                # Tecla M ativa/desativa as instruções (somente se não estiver visível)
           

                # Eventos para a tela de instrução (se ativa)
                case 2: 
                    self.instruction.events(events)

            #som na barra de espaço

    
    def update(self):
        while self.loop:
            self.events()
            self.draw()

            if self.gameStatus == 4:
                self.stop_game_sound()
                restart = self.lose_screen.play_video()

                if not self.loop:
                    break  # impede o reinício se o jogador fechou a janela

                if restart:

                    self.updategamestatus(1)
                    
                    self.underwater_fx.play(-1)
                    self.fx_started = True
                    self.instruction.visible = False
                else:
                    self.loop = False  # Encerra o jogo completamente
                    break

            

            pygame.display.update()
        pygame.quit()
        sys.exit()
    


    def stop_game_sound(self):
        self.underwater_fx.stop()
        self.fx_started = False
    


game = Main(288,512,"CappyBird")
game.update()