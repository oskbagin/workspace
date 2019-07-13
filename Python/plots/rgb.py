from matplotlib import pyplot as plt
from rgb_data_generator import rgbDataGen as rgbgen

def rgbPlot(rawRGB, title):
    t = rawRGB[0]

    plt.figure(num=None, figsize=(15,10), dpi=80)
    plt.title(title)
    
    plt.plot(t, rawRGB[1], 'r-')
    plt.plot(t, rawRGB[2], 'g-')
    plt.plot(t, rawRGB[3], 'b-')
    plt.grid(True)

    #plt.subplot(2,1,1)
    #for i in range(0, len(rawRGB[0])):
    #    plt.bar(rawRGB[0][i], [1], (rawRGB[1][i], rawRGB[2][i], rawRGB[3][i]))

    plt.show()    

rgb = rgbgen()

rgbPlot(rgb.genSinData(shifts=[0, 2/3, 4/3], ranges = 1), 'sin')
#print(rgb.b)
