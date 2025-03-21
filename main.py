import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
  
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()        
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    field_of_asteroids = AsteroidField()
    player_one = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('#000000')

        updatable.update(dt)
     
        for roid in asteroids:
            if roid.collision_check(player_one):
                print('Game over!')
                pygame.quit()
                sys.exit()
        for roid in asteroids:
            for shot in shots:
                if roid.collision_check(shot):
                    roid.split(screen)
                    shot.kill()
                
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
       


if __name__ == "__main__":
    main()