from circleshape import CircleShape
from constants import *
import pygame
from bullet import Shot

class Player(CircleShape):

    

    def __init__(self, x, y):
        super().__init__(x,y,radius=PLAYER_RADIUS)
        self.rotation=0
        self.shot_timer = 0
    
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
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shot_timer > 0:
            return # return nothing
        self.shot_timer = PLAYER_SHOT_COOLDOWN
            
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        



    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    
