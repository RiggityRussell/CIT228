import pygame
from map import *

class Settings:
    #class to store all settings for my game!
    def __init__(self):
        windInfo = pygame.display.Info()
        self.screen_width = windInfo.current_w
        self.screen_height = 64 * 15