import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):

    # initialises the Player class and pulls variables from the parent CircleShape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill() # call the kill function on the orginal asteroid

        if self.radius < ASTEROID_MIN_RADIUS: # kill small asteroids immeditadelt
            return
        
        random_angle = random.uniform(20, 50) # set a random angle for the split

        new_radius = self.radius - ASTEROID_MIN_RADIUS # set a new radius for the split asteroid

        # set up two new asteroid objects that are created by the split and set their path & speed
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
        asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2
            
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    