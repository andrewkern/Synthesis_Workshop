import numpy as np
from matplotlib import pyplot as plt

im = plt.imread("gulf_of_maine_grid_cropped.png")
chan = im[:,:,1]
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        if chan[i,j] > 0:
            print("#", end="")
        else:
            print(" ", end="")
    print("\n")
