import pygame
import sys

# define some colors in the RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    # set up pygame and its screen
    pygame.init()
    screen_size = (1200, 800)
    screen = pygame.display.set_mode(screen_size)

    # create a game clock
    clock = pygame.time.Clock()

    while True:
        # handle mouse and keyboard event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # fills screen with a background color
        screen.fill(WHITE)

        # create your graphics on the screen 
        pygame.draw.line(screen, BLACK, [100, 350], [500, 350], 2)
        pygame.draw.polygon(screen, BLACK, [[50, 300], [550, 300], [300, 150]], 6)
        pygame.draw.rect(screen, BLACK, [50, 400, 500, 200], 5)
        pygame.draw.ellipse(screen, BLACK, [50, 400, 500, 200])

        # update display based on what's drawn on the screen
        pygame.display.flip()

        # loop through at most 30 times per second
        clock.tick(30)

main()
