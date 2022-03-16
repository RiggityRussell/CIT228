class GameStats:
    #track stats for ninja Star

    def __init__(self, ai_game):
        #initialize stats
        self.settings = ai_game.settings
        self.reset_stats()

        #start game in an inactive state
        self.game_active = False

        #start ninja star in an active state
        #self.game_active = True

        #high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        #Initialize stats that can change during the game
        self.ninja_left = self.settings.ninja_limit
        self.score = 0
        self.level = 1

    