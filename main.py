import pygame
from constants import *

game_on = True

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill(color="black")
    pygame.display.flip() 
    while game_on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        


if __name__ == "__main__":
    main()