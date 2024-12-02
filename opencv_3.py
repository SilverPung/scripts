from opencv_1 import show_image
from opencv_2 import load_image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



def zad_1():
    image = load_image("images/capybara.png")
    # zmieniamy contrast na wartość 3 a jasność na 0
    cv.convertScaleAbs(image, image, 3, 0)
    show_image(image)


def zad_2():
    image = load_image("images/capybara.png")
    # zmieniamy contrast na wartość 1 a jasność na 75
    cv.convertScaleAbs(image, image, 1, 75)
    show_image(image)

def zad_3():

    image1 = load_image("images/capybara.png")
    image2 = load_image("images/logo.png")

    
    image2 = cv.resize(image2, (image1.shape[1], image1.shape[0]))

    
    alpha = 0.8
    beta = 0.2 
    blended = cv.addWeighted(image1, alpha, image2, beta, 0)

    
    show_image(blended)

    
def zad_4():
    # Wczytaj obraz
    image = cv.imread("images/zdjecie.png", cv.IMREAD_GRAYSCALE)
    
    # Sprawdź minimalną i maksymalną wartość piksela przed normalizacją
    min_val, max_val, _, _ = cv.minMaxLoc(image)
    print(f"Przed: min={min_val}, max={max_val}")
    
    # Przeprowadź normalizację obrazu do zakresu <0, 255>
    normalized_image = cv.normalize(image, None, 0, 255, cv.NORM_MINMAX)
    
    # Sprawdź minimalną i maksymalną wartość piksela po normalizacji
    min_val_norm, max_val_norm, _, _ = cv.minMaxLoc(normalized_image)
    print(f"Po: min={min_val_norm}, max={max_val_norm}")
    
    # Sprawdź, czy wartości są zgodne z oczekiwanym zakresem
    assert min_val_norm == 0, "Minimum value after normalization should be 0"
    assert max_val_norm == 255, "Maximum value after normalization should be 255"



def zad_5():
    image = load_image("images/capybara.png")

    b, g, r = cv.split(image)

    zeros = np.zeros_like(b)

    blue_image = cv.merge([b, zeros, zeros])
    green_image = cv.merge([zeros, g, zeros])
    red_image = cv.merge([zeros, zeros, r])

    cv.imwrite("images/blue.png", blue_image)
    cv.imwrite("images/green.png", green_image)
    cv.imwrite("images/red.png", red_image)

    show_image(load_image("images/blue.png"))
    show_image(load_image("images/green.png"))
    show_image(load_image("images/red.png"))


def zad_6():
    image = load_image("images/capybara.png")

    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    show_image(hsv_image)

def zad_7():
    image = load_image("images/capybara.png")
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


    lower_threshold = 150
    upper_threshold = 255

    ret, thresh = cv.threshold(gray_image, lower_threshold, upper_threshold, cv.THRESH_TOZERO)

    show_image(thresh)

def zad_8():
    image_A = load_image("images/capybara.png")
    image_B = load_image("images/logo.png")

    # Resize images to the same size
    height, width = image_A.shape[:2]
    image_B = cv.resize(image_B, (width, height))

    # Perform arithmetic operations
    add_AB = cv.add(image_A, image_B)
    sub_AB = cv.subtract(image_A, image_B)
    sub_BA = cv.subtract(image_B, image_A)
    mul_AB = cv.multiply(image_A, image_B)
    div_AB = cv.divide(image_A, image_B)
    div_BA = cv.divide(image_B, image_A)

    # Save results
    cv.imwrite("images/add_AB.png", add_AB)
    cv.imwrite("images/sub_AB.png", sub_AB)
    cv.imwrite("images/sub_BA.png", sub_BA)
    cv.imwrite("images/mul_AB.png", mul_AB)
    cv.imwrite("images/div_AB.png", div_AB)
    cv.imwrite("images/div_BA.png", div_BA)

    show_image(load_image("images/add_AB.png"))

def zad_9():
    image = load_image("images/capybara.png")

    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.title('Histogram')
    plt.xlabel('Wartość piksela')
    plt.ylabel('Liczba pikseli')
    plt.savefig("images/histogram.png") 
    plt.close() 
    show_image(load_image("images/histogram.png"))

if __name__ == "__main__":
    load_image("images/capybara.png")
    