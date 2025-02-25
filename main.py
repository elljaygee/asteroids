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
    asteroidfield = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # add Player to Groups
    Asteroid.containers = (asteroids, updatable, drawable) # add Asteroid to Groups
    AsteroidField.containers = updatable # add AsteroidField to Group

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # instantiate Player object
    field = AsteroidField()

    dt = 0 # set initial deltatime value

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        
        updatable.update(dt) # calls update method to move objects in the updatable Group on keystrokes
        
        screen.fill((0, 0, 0)) # set the screen colour to black

        for obj in drawable:
             obj.draw(screen) # iterates over drawable Group objects and draws them
        
        pygame.display.flip() # refresh the screen
        
        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS


if __name__ == "__main__":
    main()