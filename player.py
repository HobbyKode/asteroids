import pygame
from constants import *
from circleshape import CircleShape 
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) 
        self.rotation = 0
        self.shoot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)  

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        #ARROW and ZQSD KEYS:
        up = keys[pygame.K_z] or keys[pygame.K_UP]
        down = keys[pygame.K_s] or keys[pygame.K_DOWN]
        left = keys[pygame.K_q] or keys[pygame.K_LEFT]
        right = keys[pygame.K_d] or keys[pygame.K_RIGHT]

        shoot = keys[pygame.K_SPACE]
        #shift = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

        if up:
            self.move(dt)
        if down:
            self.move(-dt)
        if left:
            self.rotate(-dt)
        if right:
            self.rotate(dt)

        if shoot:
            self.shoot()
              



    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shooting_position = pygame.Vector2(0,1).rotate(self.rotation) 
        shot.velocity = shooting_position * PLAYER_SHOOT_SPEED

    def rotate(self, dt):
        self.rotation += PLAYER_TURN * dt 
    
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt



