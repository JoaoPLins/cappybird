import pygame
from DRobj import obj

class InstructionScreen:
    def __init__(self):
        self.bg = obj("assets/menu.png", 0, 0)
        self.btn_close = obj("assets/close.png", 220, 10)
        self.font = pygame.font.SysFont("arial", 14, True)
        self.texts = [
            "Pressione a tecla ESPAÇO para nadar.",
            "Desvie dos obstáculos.",
            "Pressione ESC para sair"
        ]
        self.visible = False
        self.mouse = pygame.Rect(0, 0, 1, 1)

    def draw(self, window):
        if self.visible:
            self.bg.drawing(window)
            self.btn_close.drawing(window)
            for i, line in enumerate(self.texts):
                rendered = self.font.render(line, True, (255, 255, 255))
                window.blit(rendered, (20, 150 + i * 25))

    def events(self, event):
        if self.visible:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.mouse.center = pos
                if self.mouse.colliderect(self.btn_close.sprite.rect):
                    self.visible = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.visible = False

    def toggle(self):
        self.visible = not self.visible
