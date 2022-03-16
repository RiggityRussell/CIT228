import sys
from time import sleep
import pygame
from settings import Settings
from ninja import Ninja
from star import Star
from flipNinja import FlipNinja
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button



class NinjaStar:
    #Overall class to manage game assets and behavior

    def __init__(self):
        pygame.init() #initializes the game, creates game resources
        
        self.settings = Settings()
        
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Ninja Star")

        #create an instance to store game stats and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ninja = Ninja(self)
        self.star = pygame.sprite.Group()
        self.flips = pygame.sprite.Group()

        self._create_flips()

        #Make the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        #Main Loop for the game.
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ninja.update()
                self._update_stars()
                self._update_flips()

            self._update_screen()

    def _create_flips(self):
        #create a fleet of flip ninjas
        
        flip = FlipNinja(self) #Make an flip ninja
        flip_width, flip_height = flip.rect.size #creating width and height of flip ninja
        available_space_x = self.settings.screen_width - (2 * flip_width) #setting the width of the screen so we dont spill over or have too many flip ninjas
        number_flip_x = available_space_x // (2 * flip_width) #find the number of flip ninjas we can fit on screen with modulo

        #determine the number of rows of ninjas that fit on the screen
        ninja_height = self.ninja.rect.height
        available_space_y = (self.settings.screen_height - (3 * flip_height) - ninja_height)
        number_rows = available_space_y // (2 * flip_height)

        #create the full fleet of flip ninjas
        for row_number in range(number_rows):
            #create the first row of flip ninjas
            for flip_number in range(number_flip_x):
                self._create_flip(flip_number, row_number)

    def _create_flip(self, flip_number, row_number):
        #create an flip ninja and place it in the row.
        flip = FlipNinja(self)
        flip_width, flip_height = flip.rect.size #.size contains tuple with the width and height of the rect object.
        flip.x = flip_width + 2 * flip_width * flip_number
        flip.rect.x = flip.x
        flip.rect.y = flip_height + 2 * flip.rect.height * row_number
        self.flips.add(flip)        
           
    def _check_flip_edges(self):
        #Respond appropriately if any flip ninjas have reached an edge
        for flipninja in self.flips.sprites():
            if flipninja.check_edges():
                self._change_fleet_direction() 
                break
    
    def _change_fleet_direction(self):
        #drop the entire fleet and change the fleets direction
        for flipninja in self.flips.sprites(): 
            flipninja.rect.y += self.settings.flip_drop_speed
        self.settings.flip_direction *= -1

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        #start a new game when the player clicks play
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        pygame.mixer.music.load('Chapter12/ninjaStar/media/KevinMacleod.mp3') #Music found off of youtube audio library, creative content, by Kevin Macleod
        pygame.mixer.music.play(-1)
        
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ninja()

            #get rid of any remaining aliens and bullets
            self.flips.empty()

            #create a new fleet and center the ninja
            self._create_flips()
            self.ninja.center_ninja()
            #hide the mouse cursor
            pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self, event):
        #Respond to keypress
        if event.key == pygame.K_RIGHT:
            #Move the ninja to the right
            self.ninja.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ninja.moving_left = True
        elif event.key == pygame.K_ESCAPE: #CHANGED THE EXIT KEY FROM Q TO ESCAPE
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_star()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ninja.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ninja.moving_left = False


    def _fire_star(self):
        #Create a new star and add it to the stars group and add the throw sound
        if len(self.star) < self.settings.star_allowed:
            new_star = Star(self)
            self.star.add(new_star)
            throw = pygame.mixer.Sound('Chapter12/ninjaStar/media/throw.wav')
            pygame.mixer.Sound.play(throw)
    
    def _update_stars(self):    
        #Update position of stars and get rid of old stars
        #Update star positions
        self.star.update()

        for stars in self.star.copy():
                if stars.rect.bottom <= 0:
                    self.star.remove(stars)
        
        #check for any starss that have hit flip ninjas
        #if so get rid of the star and the flip ninja
        self._check_star_flip_collisions()
    
    def _check_star_flip_collisions(self):
        #respond to star-flip ninjas collisions
        #remove any stars and flip ninjas that have collided
        collisions = pygame.sprite.groupcollide(self.star, self.flips, True, True)
        
        if collisions:
            for flips in collisions.values():
                self.stats.score += self.settings.flip_points * len(flips)
                dead = pygame.mixer.Sound('Chapter12/ninjaStar/media/dead.wav')
                pygame.mixer.Sound.play(dead)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.flips:
            #destroy existing stars and create new flips
            self.star.empty()
            self._create_flips()
            self.settings.increase_speed()

            #Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_flips(self):
        #Check if fleet at edge, update positions of all flip ninjas in fleet
        self._check_flip_edges()
        #update the positions of all the flipninjas
        self.flips.update()

        #look for flip-ninja collisions
        if pygame.sprite.spritecollideany(self.ninja, self.flips): #if no collisions occur, spritecollideany returns none and if block wont execute
            self._ninja_hit()

        #look for flips hitting the bottom of the screen
        self._check_flips_bottom()
    
    def _check_flips_bottom(self):
        #check if any flip ninjas have reached the bottom of the screen
        screen_rect = self.screen.get_rect()
        for flip in self.flips.sprites():
            if flip.rect.bottom >= screen_rect.bottom:
                #treat the same as if the ninja got hit
                self._ninja_hit()
                break

    def _ninja_hit(self):
        #respond to the ninja being hit by a flip ninja
        #decrement ninjas left
        Ninja_dead = pygame.mixer.Sound('Chapter12/ninjaStar/media/Ninja_dead.wav')
        pygame.mixer.Sound.play(Ninja_dead)
        if self.stats.ninja_left > 0:
            #decrement ninjas left and update scoreboard
            self.stats.ninja_left -= 1
            self.sb.prep_ninja()

            #get rid of any remaining flip ninjas and stars
            self.flips.empty()
            self.star.empty() #.empty removes all sprites from a group
            
            #create a new fleet and center the ninja
            self._create_flips()
            self.ninja.center_ninja()

            #pause
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        #self.screen.fill(self.settings.bg_color) #Redraw the screen during each pass through the loop
        self.screen.blit(pygame.transform.scale(self.settings.bg_image, (self.settings.screen_width, self.settings.screen_height)), (0, 0))
        self.ninja.blitme()
        self.star.draw(self.screen)
        for stars in self.star.sprites():
            stars.draw_star()

        self.flips.draw(self.screen) #call the groups draw method to make flip ninja appear

        #draw the score info
        self.sb.show_score()

        #draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip() # Make the most recently drawn screen visible

if __name__ == '__main__':
    ai = NinjaStar() #make a game instance, and run the game.
    ai.run_game()