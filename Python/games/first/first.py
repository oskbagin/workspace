import pygame
import sys
import logging
from game_object import gameObjectClass
from game_background import gameCanvasClass, gameWindow
from game_init import gameInit

getEvents = pygame.event.get
peekEvents = pygame.event.peek

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
                if event.type is pygame.QUIT:
                    running = False
                elif event.type is pygame.KEYDOWN:
                    if event.key is 113:
                        quitEvent = pygame.event.Event(pygame.QUIT)
                        pygame.event.post(quitEvent)
                    else:
                        ''' Pretty naive version
                        innerEvents = []
                        while innerEvents == [] and pygame.KEYUP not in innerEvents:
                            emojiObject.moveMe(event, screen)
                            screen.drawBackground()
                            screen.drawObject(emojiObject)
                            innerEvents = getEvents()'''
                        emojiObject.moveMe(event, screen)
                        screen.drawBackground()
                        screen.drawObject(emojiObject)
                elif event.type == pygame.KEYUP:
                    print('up')
                else:
                    pass
        except KeyboardInterrupt:
            running = False

if __name__ == "__main__":
    # call the main function:
    main()

