import pygame
from DRobj import obj
from menu import Menu
from game import Game
from instruction import InstructionScreen
#from bubble_transition import BubbleTransition

#precisa testar     
pygame.init()
icon = pygame.image.load("assets/icon.png")

class Main:
    def __init__(self,sizex,sizey,title):

        self.window = pygame.display.set_mode((sizex,sizey))
        self.title = pygame.display.set_caption(title)
        self.icon = pygame.display.set_icon(icon)

        self.loop = True
        self.menu = Menu()
        self.game = Game()
        self.underwater_fx = pygame.mixer.Sound("assets/underwater-fx.wav")
        self.fx_started = False
        self.jump_sound = pygame.mixer.Sound("assets/diving-fx.wav")  # ou outro nome de som
        self.jump_sound.set_volume(0.6)  # ajuste de volume

        self.gameStatus = 0

        self.instruction = InstructionScreen()
        self.instruction_already_shown = False

        #self.transition = BubbleTransition()
        #self.transition_active = False
        #self.prev_instruction_visible = False  # para detectar fechamento
     

    def updategamestatus(self,arg):
        self.gameStatus = arg

    def draw(self):
        
        match self.gameStatus:

            case 0:
                self.menu.draw(self.window)
            
            case 1:
                self.game.draw(self.window)
                self.game.update()

                #if not self.instruction.visible:
                #    self.game.update()
                    
        #self.game.draw(self.window)
        #self.transition.draw(self.window)

        # Desenhar a tela de instrução por cima de tudo
        if self.instruction.visible:
            self.instruction.draw(self.window)


                


    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            match self.gameStatus:
                case 0: 
                    self.menu.events(events)
                case 1:
                    self.game.events(events)    
            
            
            # Tecla M ativa/desativa as instruções (somente se não estiver visível)
            if events.type == pygame.KEYDOWN and events.key == pygame.K_m:
                if not self.instruction.visible:
                    self.instruction.visible = True

            # Eventos para a tela de instrução (se ativa)
            if self.instruction.visible:
                self.instruction.events(events)
            else:
                match self.gameStatus:
                    case 0: 
                        self.menu.events(events)
                    case 1:
                        self.game.events(events)
            
            #som na barra de espaço
            if events.type == pygame.KEYDOWN and events.key == pygame.K_SPACE:
                if self.gameStatus == 1 and not self.instruction.visible:
                    self.jump_sound.play()

    #def draw_transition(self):
    #    self.game.draw(self.window)
    #    self.transition.draw(self.window)
    #   
    #    if self.instruction.visible:
    #        self.instruction.draw(self.window)

    
    def update(self):
        while self.loop:
            self.events()
            self.draw()

            # Se sair do menu, iniciar o jogo
            if self.gameStatus == 0 and self.menu.change_scene:
                self.updategamestatus(1)
                self.game.set_start()

                if not self.fx_started:
                    pygame.mixer.music.load("assets/underwater-fx.wav")
                    self.underwater_fx.play(-1)
                    self.fx_started = True

                if not self.instruction_already_shown:
                    #self.instruction.visible = False
                    self.instruction_already_shown = True
                else:
                    self.instruction.visible = False

            pygame.display.update()

    def stop_game_sound(self):
        self.underwater_fx.stop()
        self.fx_started = False



game = Main(288,512,"CappyBird")
game.update()


