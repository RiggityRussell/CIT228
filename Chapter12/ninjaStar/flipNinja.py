import pygame
from pygame.sprite import Sprite

class FlipNinja(Sprite):
    #A class to represent a single flip ninja in the fleet

    def __init__(self, ai_game):
        #initialize the flip ninja and set its starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the flip ninja image and set its rect attribute
        self.image = pygame.image.load('Chapter12/ninjaStar/media/flipNinja.png')
        self.rect = self.image.get_rect()

        #Start each new flip ninja near the top left of the screen
        #self.rect.x = self.rect.bottomleft

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the flip ninjas exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        #return true if flip ninja is at edge of screen
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right or self.rect.left <=0):
            return True

    def update(self):
        #move the flip ninjas to the right
        self.x += (self.settings.flip_speed * self.settings.flip_direction)
        self.rect.x = self.x