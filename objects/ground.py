import pygame
import os

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img_path = os.path.join("objects/sprites", "ground.png")
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (2400, 26))
        self.rect = self.image.get_rect()

    def flip_side(self):
        self.image = pygame.transform.flip(self.image, True, False)
