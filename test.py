from matplotlib import image
import numpy as np

def rgbToColor(n):
    return n[0]

img = image.imread("face1.jpg")

H = img.shape[0]
W = img.shape[1]

height = H//6
width = W//6

colors = np.ndarray(shape=(3,3), dtype= tuple)

for i in range(3):
    width = W//6
    for j in range(3):
        colors[i][j] = img[height][width]
        width+= W//3 
    height+= H//3
