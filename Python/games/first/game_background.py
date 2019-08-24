import pygame
from game_object import gameObjectClass

class gameWindow:
    def __init__(self):
        pass

class gameCanvasClass:
    def __init__(self, backgroundPic, width = 1280, height = 640):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.background = pygame.image.load(backgroundPic)

    def drawBackground(self):
        self.screen.blit(self.background, (0, 0))

    def drawObject(self, gameObj):
        self.screen.blit(gameObj.getImage(), gameObj.getXYTuple())
        pygame.display.flip()
