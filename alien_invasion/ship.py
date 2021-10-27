import pygame

class Ship:

    def __init__(self, ai_game):
        #ai_game is an instance of alienInvasion class, so ship has access
        #to the attributes and methods in AlienInvasion class
        #initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rectangle, the image is assigned to the shape
        self.image = pygame.image.load('/Users/interstellahyeon/Documents/GitHub/python_crash_course/alien_invasion/alienship2.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        #draws the image to the screen at the position specified by self.rect.
        self.screen.blit(self.image, self.rect)