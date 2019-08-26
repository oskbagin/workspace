import pygame
import sys
import logging
from game_object import gameObjectClass
from game_background import gameCanvasClass, gameWindow
from game_init import gameInit

step_x = 10
step_y = 10

getEvents = pygame.event.get

def main():
    gameInit()

    image = pygame.image.load('files/intro_ball.gif')
    emojiObject = gameObjectClass(image, 111, 111, 50, 50, True)

    # creating main pane for the screen
    screen = gameCanvasClass('files/background.png')
    screen.drawBackground()
    screen.drawObject(emojiObject)

    running = True

# to detect pressed button hold poll for keyup event in other function
    while running:
        try:
            # handles all events:
            events = getEvents()
            if events != []:
                print(events)
            for event in events:
                # TODO: check the event types in docs:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    innerEvents = getEvents()
                    while innerEvents == [] and pygame.KEYUP not in innerEvents:
                        emojiObject.moveMe(event, screen)
                        screen.drawBackground()
                        screen.drawObject(emojiObject)
                        innerEvents = getEvents()
                else:
                    pass
        except KeyboardInterrupt:
            running = False

if __name__ == "__main__":
    # call the main function:
    main()

