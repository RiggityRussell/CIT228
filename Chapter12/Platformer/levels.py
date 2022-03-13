import pygame
from tiles import Tile #using Tile to create what the layout of the tiles will be
from map import * # bring in map, size of tiles
from hero import *
from settings import Settings

class Level:
    def __init__(self, map, surface): # we pass in the map, and assign it to the screen

        #level setup
        self.settings = Settings()
        self.display_surface = surface #surface will always be screen
        self.setup_level(map) #passing map into the setup level method
        self.world_shift = 0 # we will use this variable to allow the map to shift with the player
  

    def setup_level(self, map): #we pass the map in
        self.tiles = pygame.sprite.Group() #create a group of sprites for tiles assign variable
        self.hero = pygame.sprite.GroupSingle()
        self.treasure = pygame.sprite.GroupSingle()
        self.map = map #using the self
        for row_index, row in enumerate(self.map): 
            for column_index, col in enumerate(row):
                self.x = column_index * 64
                self.y = row_index * 64
                if col == 'X':
                    self.tile = Tile((self.x, self.y), 64) 
                    self.tiles.add(self.tile)
                if col == 'H':
                    self.hero_sprite = Hero((self.x, self.y)) 
                    self.hero.add(self.hero_sprite)
                if col == 'Z':
                    self.treasure = Tile((self.x, self.y), 24)
                    self.tiles.add(self.treasure)
                    

    def scrolling_level(self):
        speed = self.hero_sprite.hero_speed
        hero = self.hero.sprite
        hero_x = hero.rect.centerx #getting the postition of the center of x of the hero's sprite
        dir_x = self.hero_sprite.direction.x
        screen_w = self.settings.screen_width

        if hero_x < screen_w / 4 and dir_x < 0:
            self.world_shift = 2
            speed = 0
            self.hero_sprite.hero_speed = speed
        elif hero_x > screen_w - (screen_w / 4) and dir_x > 0:
            self.world_shift = -2
            speed = 0
            self.hero_sprite.hero_speed = speed
        else:
            self.world_shift = 0
            speed = 2    
            self.hero_sprite.hero_speed = speed
        
    def horizontal_movement_collision(self):
        hero = self.hero.sprite
        hero.rect.x += self.hero_sprite.direction.x * self.hero_sprite.hero_speed #applying horizontal movement

        for sprite in self.tiles.sprites(): #look through all sprites and see if there is a direct collision
            if sprite.rect.colliderect(hero.rect): # is it hero and rectangle?
                if self.hero_sprite.direction.x <0: 
                    hero.rect.left = sprite.rect.right #is it left 
                  
                elif self.hero_sprite.direction.x >0:
                    hero.rect.right = sprite.rect.left #is it right
                   
        

    def vertical_movement_collision(self):
        hero = self.hero.sprite
        #hero.apply_gravity()
        self.hero_sprite.apply_gravity()
        for sprite in self.tiles.sprites(): #look through all sprites and see if there is a direct collision
            if sprite.rect.colliderect(hero.rect): # is it hero and rectangle?
                if self.hero_sprite.direction.y > 0: 
                    hero.rect.bottom = sprite.rect.top #is it the bottom
                    self.hero_sprite.direction.y = 0
                    hero.ground = True
                elif self.hero_sprite.direction.y < 0:
                    hero.rect.top = sprite.rect.bottom #is it the top
                    self.hero_sprite.direction.y = 0
                    hero.ceiling = True
        
        if hero.ground and hero.direction.y < 0 or hero.direction.y > 1:
            hero.ground = False
        if hero.ceiling and hero.direction.y > 0:
            hero.ceiling = False

    def run(self):
        #map tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
        #hero tiles
        self.hero.update()
        self.hero.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.scrolling_level() # call the scrolling level function constantly