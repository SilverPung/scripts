from opencv_1 import show_image
import cv2 as cv
import numpy as np



def load_image(image_path: str) -> np.ndarray:
    # Wczytuje obraz z pliku
    image = cv.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return None

    return image

def zad_1():
    # kustomowa funkcja do wczytywania obrazu
    
    image=load_image("capybara.png")
    

    tx =150
    yx = 50
    # Tworzy macierz translacji o wymiarach 2x3
    translation_matrix = np.float32([[1, 0, tx], [0, 1, yx]])

    # tworzy nowy obraz przesunięty o macierz translacji o wymiarach takich jak obraz
    moved_image = cv.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

    # Wyświetla obraz w oknie
    show_image(moved_image)

def zad_2(dimension: str = 'x'):
    # Wczytuje obraz
    image = load_image("capybara.png")

    # odbijamy w zadanej osi
    if dimension == 'x':
        mirror_image = cv.flip(image, 1)  #W poziomie
    elif dimension == 'y':
        mirror_image = cv.flip(image, 0)  #W pionie
    else:
        print("Error: Invalid dimension. Use 'x' for horizontal or 'y' for vertical.")
        return

    # Wyświetla obraz w oknie
    show_image(mirror_image)

def zad_3(angle:int):
    # Wczytuje obraz
    image = load_image("capybara.png")

    # Tworzy macierz rotacji o wymiarach 2x3
    rotation_matrix = cv.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle,1)

    # Rotuje obraz o 45 stopni w kierunku przeciwnym do ruchu wskazówek zegara
    rotated_image = cv.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

    # Wyświetla obraz w oknie
    show_image(rotated_image)

def zad_4():
    image = load_image("capybara.png")

    # Współrzędne lewego górnego i prawego dolnego rogu prostokąta
    rectagle_start = (0, image.shape[0]//2)
    rectagle_end = (image.shape[1], image.shape[0])

    # Wycinamy fragment z obrazu
    cut_image = image[rectagle_start[1]:rectagle_end[1], rectagle_start[0]:rectagle_end[0]]
   
    show_image(cut_image)



def zad_5(function:str,size:int):
    
    image = load_image("capybara.png")

    if function == "resize":
        #powiększa obraz o x razy z wykorzystaniem funkcji cv.resize
       image = cv.resize(image,(0,0),fx=size,fy=size)
    elif function == "pyrUp":
        #powiększa obraz o x razy z wykorzystaniem funkcji cv.pyrUp , która powiększa obraz tylko o 2 razy
        for i in range(size//2):
            image = cv.pyrUp(image)
    
    show_image(image)
        
    

    

def zad_6(function:str,size:int):
    
    image = load_image("capybara.png")

    if function == "resize":
        #powiększa obraz o x razy z wykorzystaniem funkcji cv.resize
       image = cv.resize(image,(0,0),fx=1/size,fy=1/size)
    elif function == "pyrDown":
        #powiększa obraz o x razy z wykorzystaniem funkcji cv.pyrUp , która powiększa obraz tylko o 2 razy
        for i in range(size//2):
            image = cv.pyrDown(image)
    
    show_image(image)


def zad_7():
    image= load_image("capybara.png")

    zoomed_image = cv.resize(image,(0,0),fx=1.5,fy=1.5)

    show_image(zoomed_image)

if __name__ == "__main__":
    zad_7()