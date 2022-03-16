import pygame
from pygame.sprite import Sprite

class Ninja(Sprite):
    #A class to manage the ninja

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('Chapter12/ninjaStar/media/lilNinja.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ninjas's horizontal position
        self.x = float(self.rect.x)

        self.moving_right = False # Movement flag
        self.moving_left = False # Movement flag
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ninja_speed 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ninja_speed

        #Update rect object from self.x
        self.rect.x =self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ninja(self):
        #center the ninja on the top of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)