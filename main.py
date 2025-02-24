import pygame
from constants import *

pygame.init() # initialise pygame module

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # set initial display size


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
        pygame.display.flip() # refresh the screen
        dt = clock.tick(60) / 1000 #


if __name__ == "__main__":
    main()