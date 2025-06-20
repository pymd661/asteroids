import pygame
from constants import *

game_on = True

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill(color="black")
    pygame.display.flip() 

    clock = pygame.time.Clock()
    dt = 0

    while game_on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        clock.tick(60)


if __name__ == "__main__":
    main()