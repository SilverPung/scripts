import numpy as np
import cv2 as cv

def zad_1():
    
    # Twórzy listę 9 wartości od 1 do 8
    values = [1, 2, 3, 3, 5, 6, 6, 7, 8]
    # Tworzy macierz 3x3 z wartości z listy
    matrix = np.array(values, dtype=np.uint8).reshape(3, 3)

    print(matrix)


def zad_2(image_path:str="capybara.png",format:str="png"):
    # Wczytuje obraz z pliku
    image = cv.imread(image_path)
    # Tworzy nazwę pliku wyjściowego
    name = image_path.split(".")[0] + "_copy." + format

    if image is None:
        print("Error: Could not load image.")
        return
    # Zapisuje obraz do pliku z nową nazwą w niezmienionej postaci
    cv.imwrite(name, image)

def zad_3(image_path:str="capybara.png"):
    # Wczytuje obraz z pliku
    image = cv.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return
    # Wyświetla obraz w oknie
    show_image(image)
    
def zad_4(image_path:str="capybara.png"):
    image = cv.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return
    # Konwertuje obraz na odcienie szarości
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # Wyświetla obraz w oknie tak samo jak w zadaniu 3
    show_image(gray_image)


#zad_5
#wszystkie pliki zadziałały oprócz gif, gdyż nie mógł zostać załadowany



def zad_6(image_path:str="capybara.png",text:str="Capybara",
          font_size:int=8,font_color:tuple=(0, 255, 0),
          position:tuple=(100, 250),font=cv.FONT_HERSHEY_SCRIPT_SIMPLEX):
    
    image = cv.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return

    # Dodaje tekst do obrazu poszczególnymi parametrami, w zależności preferencji
    cv.putText(image, text, position, font, font_size, font_color,4)
    show_image(image)


def zad_7(image_path:str="capybara.png"):
    image = cv.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return

    # Tworzy okrąg o podanych parametrach
    circle_center = (image.shape[1]//2, 3*image.shape[0]//4)
    circle_radius = image.shape[0]//4
    circle_color = (0, 0, 0)
    circle_thickness = 3
    cv.circle(image, circle_center, circle_radius, circle_color, circle_thickness)

    # Tworzy linię  o podanych parametrach
    line_start = (0, image.shape[0]//2)
    line_end = (image.shape[1], image.shape[0]//2)
    line_color = (255, 255, 0)
    line_thickness = 5
    cv.line(image,line_start,line_end, line_color, line_thickness)

    # Tworzy prostokąt o podanych parametrach
    rectagle_start = (0, 0)
    rectagle_end = (image.shape[1]//2, image.shape[0]//2)
    rectangle_color = (0, 255, 255)
    rectangle_thickness = 3
    cv.rectangle(image, rectagle_start, rectagle_end, rectangle_color, rectangle_thickness)

    show_image(image)


def show_image(image):
    img_height, img_width = image.shape[:2]

    if img_height > 900 or img_width > 1800:
        show_image_with_scroll(image)
    else:
        show_small_image(image)

def show_small_image(image):
    # Wyświetla obraz w oknie
    cv.imshow("capybara", image)
    
    # Pętla wyświetlająca obraz dopóki nie zostanie zamknięte okno
    while True:
        if cv.waitKey(1) & 0xFF == ord('q'):# Wciśnięcie klawisza 'q' kończy działanie programu
            break
        if cv.getWindowProperty("capybara", cv.WND_PROP_VISIBLE) < 1: # Zamknięcie okna kończy działanie programu
            break
    
    # Zamyka okno
    cv.destroyAllWindows()

def show_image_with_scroll(image):
    # Get image dimensions
    img_height, img_width = image.shape[:2]

    # Define window size
    window_width, window_height = 1920, 1080

    # Create a window
    cv.namedWindow("Scrollable Image", cv.WINDOW_NORMAL)
    cv.resizeWindow("Scrollable Image", window_width, window_height)

    # Create trackbars for scrolling
    def on_trackbar_x(val):
        update_image()

    def on_trackbar_y(val):
        update_image()

    cv.namedWindow("Scrollable Image", cv.WINDOW_NORMAL)
    cv.resizeWindow("Scrollable Image", window_width, window_height)

    # Function to update the displayed portion of the image
    def update_image():
        x = cv.getTrackbarPos("X", "Scrollable Image")
        y = cv.getTrackbarPos("Y", "Scrollable Image")
        cropped_image = image[y:y + window_height, x:x + window_width]
        cv.imshow("Scrollable Image", cropped_image)

    # Create trackbars for scrolling
    cv.createTrackbar("X", "Scrollable Image", 0, max(1, img_width - window_width), lambda val: update_image())
    cv.createTrackbar("Y", "Scrollable Image", 0, max(1, img_height - window_height), lambda val: update_image())

    # Initial display
    update_image()


    # Wait until 'q' is pressed
    while True:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        if cv.getWindowProperty("Scrollable Image", cv.WND_PROP_VISIBLE) < 1:
            break

    # Destroy all windows
    cv.destroyAllWindows()
    
if __name__ == "__main__":
    zad_7()
