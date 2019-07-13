import math as m

class rgbDataGen:
    def __init__(self):
        self.t = []
        self.r = []
        self.g = []
        self.b = []
    
    def reset(self):
        self.t = []
        self.r = []
        self.g = []
        self.b = []

    def genSinData(self, shifts=[0, 1/3, 2/3], ranges = 3):
        self.reset()
        i=0

        shifts = [shift * m.pi for shift in shifts]

        numberOf2PiRanges = ranges
        loopCounts = 300
        step = 2 * m.pi / loopCounts

        while i < loopCounts * numberOf2PiRanges:
            i += 1
            rad = i * step

            self.t.append(rad)
            self.r.append(0.5 * (1 + m.sin(rad + shifts[0])))
            self.g.append(0.5 * (1 + m.sin(rad + shifts[1])))
            self.b.append(0.5 * (1 + m.sin(rad + shifts[2])))
        return [self.t, self.r, self.g, self.b]