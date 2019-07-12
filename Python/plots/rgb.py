from matplotlib import pyplot as plt
from rgb_data_generator import rgbDataGen as rgbgen
import math as m

def rgbPlot(rawRGB, title):
    t = rawRGB[0]

    plt.figure(num=None, figsize=(15,6), dpi=80)
    plt.title(title)
    plt.plot(t, rawRGB[1], 'r-')
    plt.plot(t, rawRGB[2], 'g-')
    plt.plot(t, rawRGB[3], 'b-')
    plt.grid(True)

    plt.show()    

rgb = rgbgen()

rgbPlot(rgb.genSinData(), 'sin')
