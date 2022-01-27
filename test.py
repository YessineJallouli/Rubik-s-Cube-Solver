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
        if (red > 190) and (green > 190) and (blue > 190):
            return 'W'
        if (red > 210) and (green > 80) and (green < 180) and (blue < 110):
            return 'O'
        if (red > 150) and (green > 200) and (blue < 100):
            return 'Y'
        if (red < 110) and (green > 160) and (blue < 110):
            return 'G'
        if (red < 120) and (green < 120) and (blue > 160):
            return 'B'
        if (red > 160) and (green < 110) and (blue < 110):
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

    def rotate_Face(self, face):
        newFace = self.Unknown_Face
        for i in range(3):
            for j in range(3):
                newFace[i][j] = face[2-j][i]
        for i in range(3):
            for j in range(3):
                face[i][j] = newFace[i][j]

    def movR(self):
        self.rotate_Face(self, self.R)
        aux = [self.U[i][2] for i in range(3)]
        for i in range(3):
            self.U[i][2] = self.F[i][2]
        for i in range(3):
            self.F[i][2] = self.D[i][2]
        for i in range(3):
            self.D[i][2] = self.B[2-i][0]
        for i in range(3):
            self.B[2-i][0] = aux[i]

    def movL(self):
        self.rotate_Face(self, self.L)
        aux = [self.D[i][0] for i in range(3)]
        for i in range(3):
            self.D[i][0] = self.F[i][0]
        for i in range(3):
            self.F[i][0] = self.U[i][0]
        for i in range(3):
            self.U[i][0] = self.B[2-i][2]
        for i in range(3):
            self.B[2-i][2] = aux[i]

    def movU(self):
        self.rotate_Face(self, self.U)
        aux = [self.L[0][i] for i in range(3)]
        for i in range(3):
            self.L[0][i] = self.F[0][i]
        for i in range(3):
            self.F[0][i] = self.R[0][i]
        for i in range(3):
            self.R[0][i] = self.B[0][i]
        for i in range(3):
            self.B[0][i] = aux[i]

    def movD(self):
        self.rotate_Face(self, self.D)
        aux = [self.R[2][i] for i in range(3)]
        for i in range(3):
            self.R[2][i] = self.F[2][i]
        for i in range(3):
            self.F[2][i] = self.L[2][i]
        for i in range(3):
            self.L[2][i] = self.B[2][i]
        for i in range(3):
            self.B[2][i] = aux[i]

    def movF(self):
        self.rotate_Face(self, self.F)
        aux = [self.U[2][i] for i in range(3)]
        for i in range(3):
            self.U[2][i] = self.L[2-i][2]
        for i in range(3):
            self.L[i][2] = self.D[0][i]
        for i in range(3):
            self.D[0][i] = self.R[2-i][0]
        for i in range(3):
            self.R[i][0] = aux[i]

def main():
    cube = RubiksCube
    cube.getColors(cube)
    if (cube.validCube == False):
        print("Invalid Rubiks Cube")
        return 0

    cube.display_all_faces(cube)

main()
