import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    #A class to manage stars thrown from the ninja

    def __init__(self, ai_game):
        #Create a star at the ninja's current position.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #self.color = self.settings.star_color

        #Create a star rectangle at (0, 0) and then set the correct position.
        self.image = pygame.image.load('Chapter12/ninjaStar/media/star.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ninja.rect.midtop

        #Store the star's position as a decimal value.
        self.y = float(self.rect.y)
        
    def update(self):
        #Move the star down the screen
        #Update the decimal position of the star.
        self.y -= self.settings.star_speed
        #Update the rectangle position
        self.rect.y = self.y

    def draw_star(self): 
        #Draw the star to the screen
        #pygame.draw.rect(self.screen, self.color, self.rect)
        # I dont think I actually need this anymore but Im scared to move it.
        self.rect
