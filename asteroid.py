import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)    

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle =  random.uniform(20, 50)
            asteroid1_vector = self.velocity.rotate(random_angle)
            asteroid2_vector = self.velocity.rotate(-random_angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid1.velocity = asteroid1_vector * 1.2
            
            asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid2.velocity = asteroid2_vector * 1.2