import pygame

class gameWindow:
    def __init__(self):
        pass

class gameCanvasClass:
    def __init__(self, backgroundPic, width = 1280, height = 1024):
        self.width = width
        self.height = height
        self.img = pygame.image.load(backgroundPic)
