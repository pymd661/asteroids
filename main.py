import pygame
from constants import *
from player import *

game_on = True

def main():
    pygame.init() # initialize pygame
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT)) # create surface
    player_1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) # setting the location for player1

    clock = pygame.time.Clock()
    dt = 0

    while game_on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        player_1.draw(screen)
        pygame.display.flip() 
        clock.tick(60)

    

if __name__ == "__main__":
    main()