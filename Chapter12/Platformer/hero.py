import pygame
from support import import_folder

class Hero(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_pictures()
        self.frame_index = 0 #used to pick one of the pictures in import pictures
        self.animation_speed = 0.005 # how fast animation updates
        self.image = self.animations['moveright'][self.frame_index]

        self.rect = self.image.get_rect(topleft = pos)


        #hero movement
        self.direction = pygame.math.Vector2(0,0) # vector is a list that contains an x and y value
        #you can add a vector to the position of a rect, rect.center += pygame.math.Vector2(x,y)
        #you can also access the x and y seperately
        self.hero_speed = .5   
        self.gravity= 0.02
        self.jump_speed = -2

        #hero status
        self.status = 'idle'
        self.face_right = True
        self.ground = False
        self.ceiling = False
        self.left = False
        self.right = False

    def import_pictures(self):
        pictures_folder = 'Platformer/media/' # creating path to the folder with the pictures
        self.animations = {'idle':[], 'moveright': [], 'jump': [], 'fall': []} # creating a dictionary with the folders as the name of action, and list to hold and go through pictures

        for animation in self.animations.keys():
            full_path = pictures_folder + animation #the pictures folder is appended to one of the list of pictures.
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed # adding speed to frame index
        if self.frame_index >= len(animation): #after adding to the frame index, if it is greater than or equal to the numberof photos in the folder
            self.frame_index = 0 #reset it to zero.

        self.image = animation[int(self.frame_index)] # we convert to integer.
        if self.face_right:
            self.image = self.image
        else:
            self.flip_image = pygame.transform.flip(self.image, True, False) #we flip the moving right image. 
            self.image = self.flip_image

        if self.ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)

    def movement(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = .5 #moves to the right
            self.face_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -.5 #moves to the left
            self.face_right = False
        else:
            self.direction.x = 0 # stops movement
        
        if keys[pygame.K_SPACE] and self.ground:
            #self.direction.y = 0

            self.jump()

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'moveright'
            else:
                self.status = 'idle'
            

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        
    def update(self):
        self.movement()
        self.get_status()
        self.animate()
        
        