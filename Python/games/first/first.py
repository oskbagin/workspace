import pygame
import sys
import logging
from game_object import gameObjectClass
from game_background import gameCanvasClass, gameWindow
from game_init import gameInit

step_x = 10
step_y = 10

def main():
    gameInit()

    image = pygame.image.load('files/intro_ball.gif')
    emojiObject = gameObjectClass(image, 111, 111, 50, 50, True)

    # creating main pane for the screen
    screen = gameCanvasClass('files/background.png')
    screen.drawBackground()
    screen.drawObject(emojiObject)

    running = True

    while running:
        # handles all events:
        for event in pygame.event.get():
            # TODO: check the event types in docs:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # case UP
                if event.key == 273:
                    emojiObject.moveUp(event, screen)
                #case DOWN
                elif event.key == 274:
                    emojiObject.moveDown(event, screen)
                screen.drawBackground()
                screen.drawObject(emojiObject)
            else:
                pass

if __name__ == "__main__":
    # call the main function:
    main()

