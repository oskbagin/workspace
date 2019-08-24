import pygame
import sys
import logging
from game_object import gameObjectClass
from game_background import gameCanvasClass, gameWindow

step_x = 10
step_y = 10

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
    

    image = pygame.image.load('files/intro_ball.gif')

    emojiObject = gameObjectClass(image, 50, 50, True)

    # creating main pane for the screen
    screen = pygame.display.set_mode((1280, 1024))
    background = pygame.image.load('files/background.png')
    screen.blit(background, (0, 0))

    screen.blit(emojiObject.getImage(), emojiObject.getXYTuple())
    pygame.display.flip()

    running = True

    while running:
        # handles all events:
        for event in pygame.event.get():
            # TODO: check the event types in docs:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 273:
                    emojiObject.moveUp(event)
                screen.blit(background, (0, 0))
                screen.blit(emojiObject.getImage(), emojiObject.getXYTuple())
                pygame.display.flip()
            else:
                pass

if __name__ == "__main__":
    # call the main function:
    main()

