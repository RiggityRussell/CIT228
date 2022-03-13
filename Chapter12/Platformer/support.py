from os import walk # walk is used in for loops, returns directory path, directory name, and file names in folder specified. JUST NEED FILE NAME
#import os
import pygame


def import_folder(path):
    surface_list = []

    for _,__,images in walk(path):
        for image in images:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    
    return surface_list

#print(os.path.abspath(os.getcwd())) # Paths confuse me more often than they should!
#import_folder('Platformer/media/run') # proves that we can get the pictures
