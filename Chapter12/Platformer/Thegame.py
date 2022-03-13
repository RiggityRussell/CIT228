import pygame
import sys
from settings import Settings
from levels import Level
from map import *

class RussGame: 
    #Class to call all functions
    def __init__(self):
        pygame.init() # allows us to use settings for pygame
        self.settings = Settings() #importing settings, we use this to pull variables and attributes from settings into the main code.
        self.screen = pygame.display.set_mode((self.settings.screen_width -50, self.settings.screen_height))
        self.level = Level(theMap, self.screen)
    
    def run_game(self):
        while True:
            self.screen.fill('black')
            self.level.run() # access the run function and trigger it constantly   
            self._check_events() 
            pygame.display.update()

    def _check_events(self):
        #respond to keypresses and mouse events
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()


if __name__ == '__main__': #this is where the code starts running
    ai = RussGame() #set ai as the class Russ game for easier access
    ai.run_game() #start the game!