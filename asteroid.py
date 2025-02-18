import pygame
import random
from constants import *
from circleshape import CircleShape 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, ASTEROIDS_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate a random angle between 20 and 50 degrees.
        random_angle = random.uniform(20, 50)

        #New asteroids Going in separate ways
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        #New radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = a * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity  = b * 1.2

        
        
        