from matplotlib import image
import numpy as np

class RubiksCube():
    
    F = np.ndarray(shape=(3,3), dtype= tuple)
    B = np.ndarray(shape=(3,3), dtype= tuple)
    U = np.ndarray(shape=(3,3), dtype= tuple)
    D = np.ndarray(shape=(3,3), dtype= tuple)
    R = np.ndarray(shape=(3,3), dtype= tuple)
    L = np.ndarray(shape=(3,3), dtype= tuple)
    
    front = image.imread("front.jpg")
    back = image.imread("back.jpg")
    up = image.imread("up.jpg")
    down = image.imread("down.jpg")
    right = image.imread("right.jpg")
    left = image.imread("left.jpg")
        
    def identifyColors(img):
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
        return colors
    
    def getColors():
        F = identifyColors(front)
        B = identifyColors(back)
        U = identifyColors(up)
        D = identifyColors(down)
        R = identifyColors(right)
        L = identifyColors(left)
        
    def rgbToColor(color):
        #to be done
        return 0
        
        
    def checkValidity(): 
        #to be done
        
    def rR(): #rotateRight
        
    def rL(): #rotateLeft
    
    def rB(): #rotateBack
        
    def rF(): #rotateFront
    
    def rU(): #rotateUp
        
    def rD(): #rotateDown
    
    #to be Done 
