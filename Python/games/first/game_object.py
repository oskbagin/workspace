import pygame

# Return true on edge hit, false otherwise
def detectGameObjectHittingCanvasBorder(gameObject, gameEvt, gameScreen):
    borderHit = False
    if gameEvt.key == 273:
        if gameObject.y <= 0:
            borderHit = True
    elif gameEvt.key == 274:
        if gameObject.y >= gameScreen.height - gameObject.size_y:
            borderHit = True

    return borderHit

class gameObjectClass:
    # init method
    def __init__(self, image, size_x, size_y, startx = 0, starty = 0, isMovable = False):
        self.image = image
        # position info
        self.x = startx
        self.y = starty
        # velocity and movement info
        self.step_x = 10
        self.step_y = 10
        self.size_x = size_x
        self.size_y = size_y
        self.movable = isMovable
    
    # drawing methods
    def getImage(self):
        return self.image

    def getXYTuple(self):
        return (self.x, self.y)
    
    # movement methods
    def moveUp(self, gameEvt, gameScreen):
        borderHit = detectGameObjectHittingCanvasBorder(self, gameEvt, gameScreen)
        # TODO bounce of the edge if hit
        if borderHit is False:
            self.y -= self.step_y
        else:
            self.y += self.step_y

    def moveDown(self, gameEvt, gameScreen):
        borderHit = detectGameObjectHittingCanvasBorder(self, gameEvt, gameScreen)
        if borderHit is False:
            self.y += self.step_y
        else:
            self.y -= self.step_y

