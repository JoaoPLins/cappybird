import pygame
import random

class Bubble:
    bubble_img = None  # imagem será carregada uma única vez

    def __init__(self):
        if Bubble.bubble_img is None:
            Bubble.bubble_img = pygame.image.load("assets/bubble.png").convert_alpha()
        self.reset()

    def reset(self):
        self.size = random.randint(20, 150)
        self.image = pygame.transform.scale(Bubble.bubble_img, (self.size, self.size))
        self.x = random.randint(-self.size, 256)
        self.y = 480 + random.randint(0, 960)
        self.speed = random.uniform(1.5, 5)

    def update(self):
        self.y -= self.speed
        if self.y + self.size < 0:
            self.reset()

    def draw(self, surface):
        surface.blit(self.image, (int(self.x), int(self.y)))

class BubbleTransition:
    def __init__(self, duration=2000):
        self.bubbles = [Bubble() for _ in range(100)]
        self.start_time = None
        self.duration = duration
        self.done = False

    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.done = False

    def update(self):
        if self.start_time is None:
            return
        for b in self.bubbles:
            b.update()
        if pygame.time.get_ticks() - self.start_time > self.duration:
            self.done = True

    def draw(self, surface):
        for b in self.bubbles:
            b.draw(surface)
