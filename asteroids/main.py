import pygame
from constants import *
from player import *
from asteroid import * 
from asteroidfield import * 
from shot import *


def main():
    pygame.init()
    clock = pygame.time.Clock()

    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('black', rect=None, special_flags=0)

        for u in updatable:
            u.update(0.03)

        for a in asteroids:
            if a.collision(player):
                exit('Game Over!')
            for s in shots:
                if a.collision(s):
                    s.kill()
                    a.split()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()