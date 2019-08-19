import pygame

# Return true on edge hit, false otherwise
def detectGameObjectHittingEdges(gameObject, gameCanvas):
    if gameObject.x < 

class gameObjectClass:
    # init method
    def __init__(self, image, startx = 0, starty = 0, isMovable = False):
        self.image = image
        # position info
        self.x = startx
        self.y = starty
        # velocity and movement info
        self.step_x = 10
        self.step_y = 10
        self.movable = isMovable
    
    # drawing methods
    def getImage(self):
        return self.image

    def getXYTuple(self):
        return (self.x, self.y)
    
    def drawMe(self, screen):
        screen.blit(self.image, self.getXYTuple())

    # movement methods
    def moveUp(self, step):
        detectEdges(self)

# just a dummy function to test
def dummy(facey):
    global step_x
    global step_y
    if facey.x > 1280 - 64 or facey.x < 0:
        step_x *= -1
    if facey.y > 1024 - 64 or facey.y < 0:
        step_y *= -1
    facey.x += step_x
    facey.y += step_y


