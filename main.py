import pygame
from constants import *

game_on = True

def main():
    while game_on == True:
        pygame.init()
        screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
        screen.fill(color="black")
        pygame.display.flip() 

if __name__ == "__main__":
    main()