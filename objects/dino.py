import pygame
import os
import glob

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        images_path = glob.glob("objects/sprites/dino_walking*.png")
        self.images = []
        for image in images_path:
            self.images.append(pygame.image.load(image))
        self.index_image = 0
        self.animate()
        self.rect = self.image.get_rect()

    def animate(self):
        self.image = self.images[self.index_image]
        self.image = pygame.transform.scale(self.image, (75, 80))
        self.index_image += 1
        if self.index_image >= len(self.images):
            self.index_image = 0
