import pygame

class Settings:
    #A class for all the settings in the Ninja game.

    def __init__(self):
        #Initialize the games settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('Chapter12/ninjaStar/media/cobbles.jpg') #set an image for the background of the screen.

        #Ninja Settings
        self.ninja_limit = 3 

        #star settings
        self.star_speed = 1.5
        self.star_width = 15
        self.star_height = 15
        self.star_color = (60, 60, 60)
        self.star_allowed = 3

        #Flip Ninja settings
        self.flip_drop_speed = 15
        

        #how quickly the game speeds up
        self.speedup_scale = 2.5
        #how quickly the flip ninja point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        #initialize settings that change throughout the game
        self.ninja_speed = 1.5
        self.star_speed = 3.0
        self.flip_speed = 1.0
        
        # flip_direction of 1 represents right; -1 represents left
        self.flip_direction = 1

        self.flip_points = 50
    
    def increase_speed(self):
        #Increase speed settings and flip ninja point values.
        self.ninja_speed *= self.speedup_scale
        self.star_speed *= self.speedup_scale
        self.flip_speed *= self.speedup_scale

        self.flip_points = int(self.flip_points * self.score_scale)
        print(self.flip_points)