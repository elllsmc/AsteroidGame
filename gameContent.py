import pygame

from utils import load_sprite
from models import *

class Spacerocks:
    def __init__(self): # class constructor, holds initialisation methods
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600)) # Creates the display surface
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        self.spaceship = Spaceship((400, 300))

    def main_loop(self): # game loop for each frame
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self): #one time initialisation of pygame
        pygame.init() # calls for pygame features, important
        pygame.display.set_caption("Space Rocks") # sets the game name

    def _handle_input(self):
        for event in pygame.event.get(): # event loop to quit the game
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE # custom key control, keydown = key pressed then specify key K_a/6/TAB etc
            ):
                quit()

    def _process_game_logic(self):
        self.spaceship.move()
        #self.asteroid.move()

    def _draw(self): # this function is called every frame to draw content on the screen
        #self.screen.fill((60, 158, 120)) # set colour
        self.screen.blit(self.background, (0, 0)) #blit() displays one surface on another based on co ordinates given
        self.spaceship.draw(self.screen)
        #self.asteroid.draw(self.screen)
        #print("Collides:", self.spaceship.collides_with(self.asteroid)) #test if collision function works
        self.clock.tick(60) # game runs at 60 frames per second
        pygame.display.flip() #updates the display per frame

