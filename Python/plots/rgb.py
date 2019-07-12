from matplotlib import pyplot as plt
import math as m

i=0

r = []
g = []
b = []
t = []

r_shift = 0
g_shift = m.pi/3
b_shift = 2 * m.pi/3

numberOf2PiRanges = 3
loopCounts = 100
step = 2 * m.pi / loopCounts

while i < loopCounts * numberOf2PiRanges:
    i += 1
    rad = i * step

    t.append(rad)
    r.append(m.sin(rad + r_shift))
    g.append(m.sin(rad + g_shift))
    b.append(m.sin(rad + b_shift))

plt.figure(num=None, figsize=(15,6), dpi=80)

plt.plot(t, r)
plt.plot(t, g)
plt.plot(t, b)
plt.grid(True)

plt.show()
