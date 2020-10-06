import pygame
import os
import glob

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Images
        images_path = glob.glob("objects/sprites/dino_walking*.png")
        self.jump_image = pygame.image.load("objects/sprites/dino_standing.png")
        self.images = []
        for image in images_path:
            self.images.append(pygame.image.load(image))
        self.index_image = 0
        self.animate()

        # Rect
        self.rect = self.image.get_rect()
        self.set_colision_boxes()

    def animate(self):
        self.image = self.images[self.index_image]
        self.image = pygame.transform.scale(self.image, (75, 80))
        self.index_image += 1
        if self.index_image >= len(self.images):
            self.index_image = 0

    def jump_posture(self):
        self.image = self.jump_image
        self.image = pygame.transform.scale(self.image, (75, 80))

    def set_colision_boxes(self):
        # Colision Boxes
        self.colision_boxes = [
            (self.rect.x + 35, self.rect.x + 65, self.rect.y, self.rect.y + 30), # Head Box
            (self.rect.x, self.rect.x + 45, self.rect.y + 30, self.rect.y + 60), # Body Box
            (self.rect.x + 15, self.rect.x + 40, self.rect.y + 60, self.rect.y + 80), # Feet Box
        ]

    def check_colision(self, rect_of_colision):
        self.set_colision_boxes()
        rect_x = rect_of_colision.x
        rect_y = rect_of_colision.y
        rect_width = rect_of_colision.width
        rect_height = rect_of_colision.height
        for box in self.colision_boxes:
            for x in range(rect_x, rect_width + rect_x):
                if x >= box[0] and x <= box[1]:
                    for y in range(rect_y, rect_height + rect_y):
                        if y >= box[2] and y <= box[2]:
                            return True
