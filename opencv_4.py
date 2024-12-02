from opencv_1 import show_image
from opencv_2 import load_image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



def zad_1():
        # Load the image in grayscale
    image = load_image('images/capybara.png')
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    # Perform segmentation (binarization)
    _, binary_image = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
    
    # Define different structuring elements
    structuring_elements = [
        cv.getStructuringElement(cv.MORPH_RECT, (3, 3)),
        cv.getStructuringElement(cv.MORPH_RECT, (5, 5)),
        cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3)),
        cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    ]
    elements=["Kw3","Kw5","Ko3","Ko5"]
    
    # Perform erosion and save results
    for i, element in enumerate(structuring_elements):
        eroded_image = cv.erode(binary_image, element)
        cv.imwrite(f'images/eroded_image_{elements[i]}.png', eroded_image)
        

        

def zad_2():
    image = load_image('images/capybara.png')
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, binary_image = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
    structuring_elements = [
        cv.getStructuringElement(cv.MORPH_RECT, (3, 3)),
        cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3)),
    ]
    elements=["Kw3x3","Ko3x3"]

    for i, element in enumerate(structuring_elements):
        for _ in range(3):
            binary_image = cv.erode(binary_image, element)
        cv.imwrite(f'images/eroted_image_{elements[i]}.png', binary_image)



def zad_3():

    image = load_image('images/capybara.png')
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    

    _, binary_image = cv.threshold(image, 100, 255, cv.THRESH_BINARY_INV)
    

    structuring_elements = [
        cv.getStructuringElement(cv.MORPH_RECT, (3, 3)),
        cv.getStructuringElement(cv.MORPH_RECT, (5, 5)),
        cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3)),
        cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    ]
    elements=["Kw3","Kw5","Ko3","Ko5"]

    for i, element in enumerate(structuring_elements):
        dilated_image = cv.dilate(binary_image, element)
        cv.imwrite(f'images/dilated_image_{elements[i]}.png', dilated_image)

def zad_4():
    image = load_image('images/capybara.png')
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, binary_image = cv.threshold(image, 100, 255, cv.THRESH_BINARY_INV)

    structuring_elements = [
        cv.getStructuringElement(cv.MORPH_RECT, (3, 3)),
        cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3)),
    ]
    elements=["Kw3x3","Ko3x3"]

    for i, element in enumerate(structuring_elements):
        for _ in range(3):
            binary_image = cv.dilate(binary_image, element)
        cv.imwrite(f'images/dilated_image_{elements[i]}.png', binary_image)


def zad_5():
    image = load_image('images/capybara.png')
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, binary_image = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)

    eroted_image = cv.erode(binary_image, cv.getStructuringElement(cv.MORPH_RECT, (3, 3)))
    opened_image = cv.dilate(eroted_image, cv.getStructuringElement(cv.MORPH_RECT, (3, 3)))
    cv.imwrite('images/opened_image.png', opened_image)

    dilated_image = cv.dilate(binary_image, cv.getStructuringElement(cv.MORPH_RECT, (3, 3)))
    closed_image = cv.erode(dilated_image, cv.getStructuringElement(cv.MORPH_RECT, (3, 3)))
    cv.imwrite('images/closed_image.png', closed_image)

    


def zad_6():
    image = load_image('images/capybara.png')
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, binary_image = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)

    structuring_element = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

    eroted_image = cv.erode(binary_image, structuring_element)
    dilated_image = cv.dilate(binary_image, structuring_element)

    image1 = cv.subtract(binary_image, eroted_image)
    image2 = cv.subtract(dilated_image, binary_image)
    image3 = cv.subtract(dilated_image, eroted_image)

    cv.imwrite('images/imagekontur1.png', image1)
    cv.imwrite('images/imagekontur2.png', image2)
    cv.imwrite('images/imagekontur3.png', image3)
    

def zad_7():
    image = load_image('images/7.png')
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, binary_image = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)

    skeleton = np.zeros_like(binary_image)
    structuring_element = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    while True:

        opened = cv.morphologyEx(binary_image, cv.MORPH_OPEN,structuring_element )
        temp = cv.subtract(binary_image, opened)
        eroded = cv.erode(binary_image, structuring_element )
        skeleton = cv.bitwise_or(skeleton, temp)
        binary_image = eroded.copy()
        
        if cv.countNonZero(binary_image) == 0:
            break
    
    cv.imwrite('images/skeleton.png', skeleton)





if __name__ == "__main__":
    zad_7()