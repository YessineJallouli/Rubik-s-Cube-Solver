# Created by Yessine Jallouli

from matplotlib import image

class RubiksCube():
    Unknown_Face = [['U' for x in range(3)] for y in range(3)]
    F = B = U = D = R = L = Unknown_Face

    front = image.imread("front.jpg")  # front should have white color in the center
    back = image.imread("back.jpg")    # back should have yellow color in the center    Y
    up = image.imread("up.jpg")        # up should have orange color in the center      O
    down = image.imread("down.jpg")    # down should have red color in the center     G W B
    right = image.imread("right.jpg")  # right should have blue color in the center     R
    left = image.imread("left.jpg")    # left should have green color in the center

    validCube = True

    def RGB_to_color(color):
        red = color[0]
        green = color[1]
        blue = color[2]
        if (red > 230) and (green > 230) and (blue > 230):
            return 'W'
        if (red > 230) and (green > 100) and (green < 180) and (blue < 110):
            return 'O'
        if (red > 230) and (green > 240) and (blue < 100):
            return 'Y'
        if (red < 110) and (green > 170) and (blue < 110):
            return 'G'
        if (red < 110) and (green < 110) and (blue > 230):
            return 'B'
        if (red > 230) and (green < 110) and (blue < 110):
            return 'R'
        return 'U'

    def identifyColors(img, self):
        H = img.shape[0]
        W = img.shape[1]
        height = H // 6
        colors = [['U' for x in range(3)] for y in range(3)]
        for i in range(3):
            width = W // 6
            for j in range(3):
                colors[i][j] = self.RGB_to_color(img[height][width])
                if (colors[i][j] == 'U'):
                    self.validCube = False
                width += W // 3
            height += H // 3
        return colors

    def getColors(self):
        self.F = self.identifyColors(self.front, self)
        self.B = self.identifyColors(self.back, self)
        self.U = self.identifyColors(self.up, self)
        self.D = self.identifyColors(self.down, self)
        self.R = self.identifyColors(self.right, self)
        self.L = self.identifyColors(self.left, self)

    def display_face(self, name, face):
        print(name, "face :")
        for i in range(3):
            for j in range(3):
                print(face[i][j], end='')
            print()
        print()

    def display_all_faces(self):
        self.display_face(self, "Front", self.F)
        self.display_face(self, "Back", self.B)
        self.display_face(self, "Up", self.U)
        self.display_face(self, "Down", self.D)
        self.display_face(self, "Right", self.R)
        self.display_face(self, "Left", self.L)

    #def movR(self):
        


def main():
    cube = RubiksCube
    cube.getColors(cube)
    if (cube.validCube == False):
        print("Invalid Rubiks Cube")
        return 0

    cube.display_all_faces(cube)

main()
