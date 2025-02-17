# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    #Initialize Pygame
    pygame.init()
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((1,1,1))
        pygame.display.flip()


if __name__ == "__main__":
    main()