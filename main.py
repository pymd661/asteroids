import pygame
from constants import *
from player import Player
from asteroidfield import *
from asteroid import *

game_on = True

def main():
    pygame.init() # initialize pygame
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT)) # create 
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) # setting the location for player
    

    
    dt = 0

    while game_on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill(color="black")

        for sprite in drawable:
            sprite.draw(screen)

        
        
        pygame.display.flip() 
        dt = clock.tick(60)/1000

    

if __name__ == "__main__":
    main()