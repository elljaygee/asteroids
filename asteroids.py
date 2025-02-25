import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):

    # initialises the Player class and pulls variables from the parent CircleShape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    