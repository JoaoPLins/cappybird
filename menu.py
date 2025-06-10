import pygame
from DRobj import obj

class Menu: 
    def __init__(self,main):
        self.bg = obj("assets/start-menu.png",0,0)
        self.change_scene = False
        self.main = main
        self.sound = pygame.mixer.Sound("assets/theme-sound.wav") #musica de fundo

        # Inicia a música do menu
        pygame.mixer.music.load("assets/theme-sound.wav")
        pygame.mixer.music.set_volume(0.5)  # Volume de 0.0 a 1.0
        pygame.mixer.music.play(-1)  # -1 = loop infinito

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
                pygame.mixer.music.stop()
                self.main.updategamestatus(1)
                print ("gamestart")
            if event.key == pygame.K_m:
                self.main.updategamestatus(2)
                print ("instruções")
    
