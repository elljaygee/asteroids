import pygame
from constants import *
from player import Player

pygame.init() # initialise pygame module

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # set initial display size

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock() # initialise clock object
    dt = 0 # set initial delta time


    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        screen.fill((0, 0, 0)) # set the screen colour to black
        player.update(dt) # calls update method to move player object on keystrokes
        player.draw(screen) # draw the player object in the centre of the screen
        pygame.display.flip() # refresh the screen
        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS


if __name__ == "__main__":
    main()