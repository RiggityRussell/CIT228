import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('gray')
        self.rect = self.image.get_rect(topleft = pos)
        #self.block = pygame.image.load('Platformer/media/block.png')
        #self.block_rect = self.block.get_rect(topleft = pos)

    def update(self, shift):
        self.rect.x += shift
