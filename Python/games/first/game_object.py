import pygame

class gameObject:
    def __init__(self, image, startx = 0, starty = 0, isMovable = False):
        self.image = image
        self.x = startx
        self.y = starty
        self.movable = isMovable

    def getImage(self):
        return self.image

    def getXYTuple(self):
        return (self.x, self.y)


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


