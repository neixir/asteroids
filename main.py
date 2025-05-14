# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Aixo de "color" no va; s'ha provat (0,0,0) i tampoc
        screen.fill(rect=None, color="black", special_flags=0)
        pygame.display.flip()

if __name__ == "__main__":
    main()