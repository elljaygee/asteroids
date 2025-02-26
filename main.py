import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init() # initialise pygame module
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # set initial display size
    clock = pygame.time.Clock() # instantiate clock object

    updatable = pygame.sprite.Group() # create updatable Group
    drawable = pygame.sprite.Group() # create drawable Group
    asteroids = pygame.sprite.Group() # create asteroids Group
    asteroidfield = pygame.sprite.Group() # create asteroid_field group
    shots = pygame.sprite.Group() # create shot group

    Player.containers = (updatable, drawable) # add Player to Groups
    Asteroid.containers = (asteroids, updatable, drawable) # add Asteroid to Groups
    AsteroidField.containers = updatable # add AsteroidField to Group

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # instantiate Player object
    asteroid_field = AsteroidField() # instantiate asteroid_field object

    dt = 0 # set initial deltatime value

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        
        updatable.update(dt) # calls update method to move objects in the updatable Group on keystrokes
        
        screen.fill((0, 0, 0)) # set the screen colour to black

        for item in drawable:
             item.draw(screen) # iterates over drawable Group objects and draws them
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("GAME OVER!")
                sys.exit()

        pygame.display.flip() # refresh the screen
        
        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS


if __name__ == "__main__":
    main()
