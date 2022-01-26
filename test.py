from matplotlib import image
import numpy as np


class RubiksCube():
    F = np.ndarray(shape=(3, 3), dtype=tuple)
    B = np.ndarray(shape=(3, 3), dtype=tuple)
    U = np.ndarray(shape=(3, 3), dtype=tuple)
    D = np.ndarray(shape=(3, 3), dtype=tuple)
    R = np.ndarray(shape=(3, 3), dtype=tuple)
    L = np.ndarray(shape=(3, 3), dtype=tuple)


    front = image.imread("front.jpg")  # front with white color in the center
    back = image.imread("back.jpg")    # back with yellow color in the center    Y
    up = image.imread("up.jpg")        # up with orange color in the center      O
    down = image.imread("down.jpg")    # down with red color in the center     G W B
    right = image.imread("right.jpg")  # right with blue color in the center     R
    left = image.imread("left.jpg")    # left with green color in the center

    def RGB_to_color(color):
        return 0

    def identifyColors(img):
        H = img.shape[0]
        W = img.shape[1]
        height = H // 6
        colors = np.ndarray(shape=(3, 3), dtype=tuple)
        for i in range(3):
            width = W // 6
            for j in range(3):
                colors[i][j] = img[height][width]
                width += W // 3
            height += H // 3
        return colors

    def getColors(self):
        self.F = self.identifyColors(self.front)
        self.B = self.identifyColors(self.back)
        self.U = self.identifyColors(self.up)
        self.D = self.identifyColors(self.down)
        self.R = self.identifyColors(self.right)
        self.L = self.identifyColors(self.left)

def main():
    cube = RubiksCube
    cube.getColors(cube)
    for i in range(3):
        for j in range(3):
            print(cube.F[i][j], end='')
        print()

main()
