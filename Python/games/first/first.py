import pygame
import sys
import logging
from game_object import gameObject

step_x = 10
step_y = 10

def game_init():
    print('init')

def dummy(facey):
    global step_x
    global step_y
    if facey.x > 1280 - 64 or facey.x < 0:
        step_x *= -1
    if facey.y > 1024 - 64 or facey.y < 0:
        step_y *= -1
    facey.x += step_x
    facey.y += step_y

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

    emojiObject = gameObject(image, 50, 50, True)

    # creating main pane for the screen
    screen = pygame.display.set_mode((1280, 1024))
    background = pygame.image.load('files/background.png')
    screen.blit(background, (0, 0))

    screen.blit(emojiObject.getImage(), emojiObject.getXYTuple())
    pygame.display.flip()

    running = True

    while running:
        screen.blit(background, (0, 0))
        dummy(emojiObject)
        screen.blit(emojiObject.getImage(), emojiObject.getXYTuple())
        pygame.display.flip()
        # handles all events:
        for event in pygame.event.get():
            # TODO: check the event types in docs:
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    # call the main function:
    main()

