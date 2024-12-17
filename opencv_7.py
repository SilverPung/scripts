import cv2 as cv
from opencv_1 import show_image
from opencv_2 import load_image
import numpy as np

def zad_1():
    def rgb_to_bgr(rgb_color):
        return (rgb_color[2], rgb_color[1], rgb_color[0])

    # Convert BGR to HSV
    def bgr_to_hsv(bgr_color):
        color = np.uint8([[bgr_color]])
        hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)
        return hsv_color[0][0]

    # Load the greenscreen image
    greenscreen_image = load_image('images/greenscreen.png')

    # Load the background image
    background_image = load_image('images/image.png')

    # Check if images are loaded correctly
    if greenscreen_image is None or background_image is None:
        raise ValueError("One or both images could not be loaded. Check the file paths.")

    # Resize the background image to match the size of the greenscreen image
    background_image = cv.resize(background_image, (greenscreen_image.shape[1], greenscreen_image.shape[0]))

    # Convert the greenscreen image to HSV
    hsv = cv.cvtColor(greenscreen_image, cv.COLOR_BGR2HSV)

    # Define the exact green color in RGB
    exact_green_rgb = (59, 213, 67)

    # Convert the exact green color to BGR
    exact_green_bgr = rgb_to_bgr(exact_green_rgb)

    # Convert the exact green color to HSV
    exact_green_hsv = bgr_to_hsv(exact_green_bgr)

    # Define the range for the green color
    lower_green = np.array([exact_green_hsv[0] - 10, 100, 100])
    upper_green = np.array([exact_green_hsv[0] + 10, 255, 255])

    # Create a mask for the green color
    mask = cv.inRange(hsv, lower_green, upper_green)

    # Invert the mask to get the non-green parts
    mask_inv = cv.bitwise_not(mask)

    # Extract the non-green parts from the greenscreen image
    fg = cv.bitwise_and(greenscreen_image, greenscreen_image, mask=mask_inv)

    # Extract the green parts from the background image
    bg = cv.bitwise_and(background_image, background_image, mask=mask)

    # Combine the foreground and background
    combined = cv.add(fg, bg)

    # Show the result
    show_image(combined)



if __name__ == "__main__":
    zad_1()