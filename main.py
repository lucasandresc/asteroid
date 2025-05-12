import sys
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
     
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    Shot.containers = (shots, updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
             
        pygame.Surface.fill(screen, (0, 0, 0))
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
            else:
                for shot in shots:
                    if shot.collision(asteroid):
                        shot.kill()
                        asteroid.split()
        
        
        for i in drawable:
            i.draw(screen)
        
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/ 1000
    
    
if __name__ == "__main__":
    main()