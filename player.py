import pygame
from circleshape import *
from constants import *

class Player(CircleShape):

    # initialises the Player class and pulls variables from the parent CircleShape
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # creates a triangle shape for the player
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # overrides the draw function from the parent class CircleShape using the points given in triangle
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    # changes player position with keystrokes
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) # rotate left
        if keys[pygame.K_d]:
            self.rotate(dt) # rotate right

    # refreshes the dt value with the new rotation
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

