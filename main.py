# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    #Initialize Pygame
    pygame.init()
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)
            
        screen.fill((1,1,1))
        player.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        frame_time = clock.tick(60)
        dt = frame_time / 1000
        
        
if __name__ == "__main__":
    main()