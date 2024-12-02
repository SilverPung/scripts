import cv2 as cv
from opencv_1 import show_image
from opencv_2 import load_image
import numpy as np

def zad_1():
    image = load_image('images/capybara.png')
    
    blurred_image_1 = cv.GaussianBlur(image, (5, 5), 0)
    blurred_image_2 = cv.GaussianBlur(image, (11, 11), 0)
    blurred_image_3 = cv.GaussianBlur(image, (17, 17), 0)
    
    #show_image( image)
    show_image( blurred_image_1)
    show_image( blurred_image_2)
    show_image( blurred_image_3)


def zad_2():
    image = load_image('images/capybara.png')
    
    median_blurred_image_1 = cv.medianBlur(image, 5)
    median_blurred_image_2 = cv.medianBlur(image, 11)
    median_blurred_image_3 = cv.medianBlur(image, 17)
    
    #show_image(image)
    show_image(median_blurred_image_1)
    show_image(median_blurred_image_2)
    show_image(median_blurred_image_3)


def zad_3():
    image = load_image('images/capybara.png')
    
    bilateral_blurred_image_1 = cv.bilateralFilter(image, 5, 75, 75)
    bilateral_blurred_image_2 = cv.bilateralFilter(image, 11, 75, 75)
    bilateral_blurred_image_3 = cv.bilateralFilter(image, 17, 75, 75)
    
    #show_image(image)
    show_image(bilateral_blurred_image_1)
    show_image(bilateral_blurred_image_2)
    show_image(bilateral_blurred_image_3)


def zad_4():
    image = load_image('images/capybara.png')
    # tworzymy filtr uśredniający 50x50
    kernel = np.ones((50, 50), np.float32) / 2500
    

    blurred_image = cv.filter2D(image, -1, kernel)
    

    #show_image(image)
    show_image(blurred_image)



def zad_5():

    image = load_image('images/capybara.png')
    blured_image = cv.GaussianBlur(image, (5, 5), 0)
    
    # tworzymi filtr wyostrzający
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])

    sharpened_image = cv.filter2D(blured_image, -1, kernel)

    #show_image(image)
    show_image(sharpened_image)


def zad_6():
    image = load_image('images/capybara.png')
    
    s_vs_p = 0.5
    amount = 0.04
    noisy_image = np.copy(image)
    
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 1
    
    # Pepper mode
    num_pepper = np.ceil(amount * image.size * (1.0 - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 0

    show_image(noisy_image)

    gauss_image = cv.GaussianBlur(noisy_image, (5, 5), 0)
    median_image = cv.medianBlur(noisy_image, 5)
    bilateral_image = cv.bilateralFilter(noisy_image, 5, 75, 75)

    show_image(gauss_image)
    show_image(median_image)
    show_image(bilateral_image)

def zad_7():
    image = load_image('images/capybara.png')
    
    # Create Gaussian noise
    mean = 0
    sigma = 50
    gaussian_noise = np.random.normal(mean, sigma, image.shape).astype('uint8')
    noisy_image = cv.add(image, gaussian_noise)

    show_image(noisy_image)

    gauss_image = cv.GaussianBlur(noisy_image, (5, 5), 0)
    median_image = cv.medianBlur(noisy_image, 5)
    bilateral_image = cv.bilateralFilter(noisy_image, 5, 75, 75)

    show_image(gauss_image)
    show_image(median_image)
    show_image(bilateral_image)

    


if  __name__ == "__main__":
    zad_7()