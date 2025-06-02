from DRobj import obj
import pygame

class Cappy():
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        original_frames = [pygame.image.load(f"assets/00{i}.png") for i in range(1, 7)]
        self.frames = [pygame.transform.scale(img, (img.get_width() // 3, img.get_height() // 3)) for img in original_frames]
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 30  # a cada 5 frames troca a imagem

        # Começa com o primeiro frame
        self.sprite.image = self.frames[self.current_frame]
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = 100
        self.sprite.rect[1] = 100
        self.cappyRect = pygame.Rect(self.sprite.rect[0], self.sprite.rect[1], 10, 10)


    def drawing(self, window):
        self.group.draw(window)

    def update(self,y):
        #self.sprite.rect[1] = self.sprite.rect[1] + y
        #self.cappyRect.update(self.sprite.rect[0],self.sprite.rect[1],10,10)


        # Atualiza a posição vertical
        self.sprite.rect[1] += y
        self.cappyRect.update(self.sprite.rect[0], self.sprite.rect[1], 10, 10)

        # Controla a troca de frame
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.sprite.image = self.frames[self.current_frame]


    def GetTheCappyNumber(self):
        return self.sprite.rect[1]

        