# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Grups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Aixo no funciona
    # https://www.boot.dev/lessons/6a09887c-ad3f-4fb3-8726-c7bd9fa4161c
    # "Set both groups as containers for the Player."
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    print(f"drawable: {len(drawable)}, updatable: {len(updatable)}, asteroids: {len(asteroids)}")
    
    dt = 0
    
    while True:
        # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for item in asteroids:
            if item.has_collided(player):
                print("Game over!")
                sys.exit(0)


        screen.fill(rect=None, color="black", special_flags=0)

        # "Loop over all "drawables" and .draw() them individually."
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if shot.has_collided(asteroid):
                    asteroid.split()

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()