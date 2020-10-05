import pygame
import os

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img_path = os.path.join("objects/sprites", "cactus.png")
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
