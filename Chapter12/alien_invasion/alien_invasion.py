import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


class AlienInvasion:
    #Overall class to manage game assets and behavior

    def __init__(self):
        pygame.init() #initializes the game, creates game resources
        self.settings = Settings()
        
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #create an instance to store game stats and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Make the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        #Main Loop for the game.
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _create_fleet(self):
        #create a fleet of aliens
        
        alien = Alien(self) #Make an alien
        alien_width, alien_height = alien.rect.size #creating width and height of alien
        available_space_x = self.settings.screen_width - (2 * alien_width) #setting the width of the screen so we dont spill over or have too many aliens
        number_aliens_x = available_space_x // (2 * alien_width) #find the number of aliens we can fit on screen with modulo

        #determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #create the full fleet of aliens
        for row_number in range(number_rows):
            #create the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        #create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size #.size contains tuple with the width and height of the rect object.
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)        
           
    def _check_fleet_edges(self):
        #Respond appropriately if any aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        #drop the entire fleet and change the fleets direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #get rid oof any remaining aliens and bullets
            self.aliens.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            #hide the mouse cursor
            pygame.mouse.set_visible(False)
    
    def _check_keydown_events(self, event):
        #Respond to keypress
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE: #CHANGED THE EXIT KEY FROM Q TO ESCAPE
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #Create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):    
        #Update position of bullets and get rid of old bullets
        #Update bullet positions
        self.bullets.update()

        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            #print(len(self.bullets)) # shows in the console log that the bullets are getting deleted at 0
        
        #check for any bullets that have hit aliens
        #if so get rid of the bullet and the alien
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        #respond to bullet-alien collisions
        #remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        #Check if fleet at edge, update positions of all aliens in fleet
        self._check_fleet_edges()
        #update the positions of all the aliens in the fleet
        self.aliens.update()

        #look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens): #if no collisions occur, spritecollideany returns none and if block wont execute
            self._ship_hit()

        #look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()
    
    def _check_aliens_bottom(self):
        #check if any aliens have reached the bottom of the screen
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat the same as if the ship got hit
                self._ship_hit()
                break

    def _ship_hit(self):
        #respond to the ship being hit by an alien
        #decrement ships left
        if self.stats.ships_left > 0:
            #decrement ships left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty() #.empty removes all sprites from a group
            
            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) #Redraw the screen during each pass through the loop
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen) #call the groups draw method to make alien appear

        #draw the score info
        self.sb.show_score()

        #draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip() # Make the most recently drawn screen visible

if __name__ == '__main__':
    ai = AlienInvasion() #make a game instance, and run the game.
    ai.run_game()