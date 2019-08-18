import pygame
import sys
import logging

def game_init():
    print('init')

def main():
    game_init()
    # passes (numpass, numfail) tuple
    nums_init = pygame.init()
    if nums_init[1] is not 0:
        print('Sth went wrong on init. Abort...')
        sys.exit(1)

    logo = pygame.image.load('files/logo32x32.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption('minimal program')
    image = pygame.image.load('files/smile.png')

    # creating main pane for the screen
    screen = pygame.display.set_mode((1280, 1024))
    screen.blit(pygame.image.load('files/background.png'), (0, 0))

    screen.blit(image, (50, 50))
    pygame.display.flip()

    running = True

    while running:
        # handles all events:
        for event in pygame.event.get():
            # TODO: check the event types in docs:
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    # call the main function:
    main()

