import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #A class to manage the ship

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        self.moving_right = False # Movement flag
        self.moving_left = False # Movement flag
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x =self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)