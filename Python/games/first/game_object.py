import pygame

arrows = {
        'up' : 273,
        'down' : 274,
        'right' : 275,
        'left' : 276
}

# Return true on edge hit, false otherwise
def detectGameObjectHittingCanvasBorder(gameObject, gameEvt, gameScreen):
    borderHit = False
    if gameEvt.key == 273:
        if gameObject.y <= 0:
            borderHit = True
    elif gameEvt.key == 274:
        if gameObject.y >= gameScreen.height - gameObject.size_y:
            borderHit = True
    elif gameEvt.key == 275:
        if gameObject.x >= gameScreen.width - gameObject.size_x:
            borderHit = True
    elif gameEvt.key == 276:
        if gameObject.x <= 0:
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
    def moveMe(self, gameEvt, gameScreen):
        borderHit = detectGameObjectHittingCanvasBorder(self, gameEvt, gameScreen)
        # case UP
        if gameEvt.key == arrows['up']:
            self.moveUp(gameEvt, gameScreen, borderHit)
        # case DOWN
        elif gameEvt.key == arrows['down']:
            self.moveDown(gameEvt, gameScreen, borderHit)
        # case RIGHT
        elif gameEvt.key == arrows['right']:
            self.moveRight(gameEvt, gameScreen, borderHit)
        # case LEFT
        elif gameEvt.key == arrows['left']:
            self.moveLeft(gameEvt, gameScreen, borderHit)

    def moveUp(self, gameEvt, gameScreen, borderHit):
        if borderHit is False:
            self.y -= self.step_y
        else:
            self.y += self.step_y

    def moveDown(self, gameEvt, gameScreen, borderHit):
        if borderHit is False:
            self.y += self.step_y
        else:
            self.y -= self.step_y

    def moveLeft(self, gameEvt, gameScreen, borderHit):
        if borderHit is False:
            self.x -= self.step_x
        else:
            self.x += self.step_x

    def moveRight(self, gameEvt, gameScreen, borderHit):
        if borderHit is False:
            self.x += self.step_x
        else:
            self.x -= self.step_x
