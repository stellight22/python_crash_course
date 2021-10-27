import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init() 
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bg_color = (230, 230, 230)
    
    def _check_events(self):
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
            self.screen.fill(self.bg_color)
            self.ship.blitme()

            #make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
