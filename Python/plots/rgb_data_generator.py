import math as m

class rgbDataGen:
    def __init__(self, loopCounts = 300):
        self.t = []
        self.r = []
        self.g = []
        self.b = []
        self.step = 2 * m.pi / loopCounts

    def reset(self):
        self.t = []
        self.r = []
        self.g = []
        self.b = []

    def genSinData(self, shifts=[0, 1/3, 2/3], ranges = 3, loopCounts = 300):
        self.reset()
        i=0

        shifts = [shift * m.pi for shift in shifts]

        numberOf2PiRanges = ranges

        while i < loopCounts * numberOf2PiRanges:
            rad = i * self.step

            self.t.append(rad)
            self.r.append(0.5 * (1 + m.sin(rad + shifts[0])))
            self.g.append(0.5 * (1 + m.sin(rad + shifts[1])))
            self.b.append(0.5 * (1 + m.sin(rad + shifts[2])))
            i += 1

        return [self.t, self.r, self.g, self.b]

    def genSinWithPausesData(self, shifts=[0, 2/3, 4/3], ranges = 2, loopCounts = 300):
        self.reset()
        i=0

        shifts = [shift * m.pi for shift in shifts]

        numberOf2PiRanges = ranges
        
        while i < loopCounts * numberOf2PiRanges:
            rad = i * self.step

            # curr_r = 0.5 * (1 + m.sin(rad + shifts[0]))
            # curr_g = 0.5 * (1 + m.sin(rad + shifts[1]))
            # curr_b = 0.5 * (1 + m.sin(rad + shifts[2]))
            curr_r = (m.sin(rad + shifts[0]))
            curr_g = (m.sin(rad + shifts[1]))
            curr_b = (m.sin(rad + shifts[2]))

            self.t.append(rad)
            self.r.append(curr_r)
            self.g.append(curr_g)
            self.b.append(curr_b)
            i += 1

        return [self.t, self.r, self.g, self.b]

    def genTriangle(self, ranges = 2, steps = 360):
        self.reset()

        # can assert params
        i = 0
        tAppend = 0
        cycles = 6
        cycleDur = steps / cycles
        derivative = 1 / cycleDur

        # introduce some halts in the end of cycle so full colours are also present for a moment
        while i < steps:
            currCycle = i // cycleDur

            if currCycle == 0:
                self.r.append(0)
                self.g.append(1)
                self.b.append((i % cycleDur) * derivative)
            elif currCycle == 1:
                self.r.append((i % cycleDur) * derivative)
                self.g.append(1)
                self.b.append(1)
            elif currCycle == 2:
                self.r.append(1)
                self.g.append(1 - (i % cycleDur) * derivative)
                self.b.append(1)
            elif currCycle == 3:
                self.r.append(1)
                self.g.append(0)
                self.b.append(1 - (i % cycleDur) * derivative)
            elif currCycle == 4:
                self.r.append(1 - (i % cycleDur) * derivative)
                self.g.append(0)
                self.b.append(0)
            elif currCycle == 5:
                self.r.append(0)
                self.g.append((i % cycleDur) * derivative)
                self.b.append(0)
            
            self.t.append(i)
            i += 1

        while tAppend > 0:
            self.t.append(i)
            i += 1
            tAppend -= 1

        return [self.t, self.r, self.g, self.b]

    def haldStateForNCycles(self, nSamples):
        cnt = 0
        while cnt < nSamples:
            self.r.append(self.r[-1])
            self.g.append(self.g[-1])
            self.b.append(self.b[-1])

            cnt += 1
        
        # number of samples to append to self.t
        return cnt