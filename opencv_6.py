
import cv2 as cv
from opencv_1 import show_image
from opencv_2 import load_image
import numpy as np

def zad_1():
    image = load_image('images/capybara.png')
    
    rims1 = cv.Canny(image, 200, 300)
    rims2 = cv.Canny(image, 150, 250)
    rims3 = cv.Canny(image, 100, 200)
    


    show_image(rims1)
    show_image(rims2)
    show_image(rims3)



def zad_2():
    image = load_image('images/capybara.png')

    rims1 = cv.Laplacian(image, cv.CV_64F, ksize=5)
    rims2 = cv.Laplacian(image, cv.CV_64F, ksize=9)
    rims3 = cv.Laplacian(image, cv.CV_64F, ksize=13)

    show_image(rims1)
    show_image(rims2)
    show_image(rims3)
    
    

def zad_3():
    image = load_image('images/capybara.png')
    
    rims1 = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=5)
    rims2 = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=9)
    rims3 = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=13)

    


    show_image(rims1)
    show_image(rims2)
    show_image(rims3)



def zad_4():
    pass


def zad_5():
    pimage = load_image('images/figury.jpg')

    gray_image = cv.cvtColor(pimage, cv.COLOR_BGR2GRAY)
    

    binary_image = cv.threshold(gray_image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]
    

    contours, _ = cv.findContours(binary_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    

    cv.drawContours(pimage, contours, -1, (0,0, 255), 3)
    
    show_image(pimage)


if __name__ == '__main__':
    zad_5()