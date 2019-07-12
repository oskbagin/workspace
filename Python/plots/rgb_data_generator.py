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

    def genSinData(self, shifts=[0, 1/3, 2/3]):
        self.reset()
        i=0

        #r_shift = 0
        #g_shift = m.pi/3
        #b_shift = 2 * m.pi/3
        shifts = [shift * m.pi for shift in shifts]
        print(shifts)

        numberOf2PiRanges = 3
        loopCounts = 100
        step = 2 * m.pi / loopCounts

        while i < loopCounts * numberOf2PiRanges:
            i += 1
            rad = i * step

            self.t.append(rad)
            self.r.append(m.sin(rad + shifts[0]))
            self.g.append(m.sin(rad + shifts[1]))
            self.b.append(m.sin(rad + shifts[2]))
        return [self.t, self.r, self.g, self.b]