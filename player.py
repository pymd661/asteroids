from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    rotation = 0
    def __init__(self, x, y):
        super().__init__(x,y,radius=PLAYER_RADIUS)
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen, color="white", line_width=2):
        return pygame.draw.polygon(surface =screen,
            color=color,
            points= self.triangle(), 
            width = line_width)
