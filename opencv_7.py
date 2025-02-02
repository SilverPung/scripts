import cv2 as cv2
from opencv_1 import show_image
from opencv_2 import load_image
import numpy as np

class Images:
    def __init__(self):
        self.lower_green = np.array([40, 40, 40])
        self.upper_green = np.array([100, 255, 255])

    def load_video(self, path):
        return cv2.VideoCapture(path)

    def apply_smoothing(self, mask, method="gaussian"):
        if method == "gaussian":
            return cv2.GaussianBlur(mask, (5, 5), 0)
        elif method == "median":
            return cv2.medianBlur(mask, 5)
        elif method == "morphology":
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            return mask
        else:
            raise ValueError("Unknown smoothing method")

    def process_image(self, img_path, bg_path, smoothing_method="gaussian"):
        img = load_image(img_path)
        background = load_image(bg_path)
        background = cv2.resize(background, (img.shape[1], img.shape[0]))

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_green, self.upper_green)
        mask = self.apply_smoothing(mask, smoothing_method)
        mask_inv = cv2.bitwise_not(mask)

        img_fg = cv2.bitwise_and(img, img, mask=mask_inv)
        background_bg = cv2.bitwise_and(background, background, mask=mask)
        return cv2.add(img_fg, background_bg)

    def zad_1(self, smoothing_method="gaussian"):
        result = self.process_image("images/greenscreen.png", "images/image.png", smoothing_method)
        show_image(result)

    def zad_2(self):
        video = self.load_video("images/doggo.mp4")
        background = load_image("images/image.png")

        frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(video.get(cv2.CAP_PROP_FPS))
        background = cv2.resize(background, (frame_width, frame_height))

        out = cv2.VideoWriter('images/result.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.lower_green, self.upper_green)
            mask = self.apply_smoothing(mask, "gaussian")

            if cv2.countNonZero(mask) == 0:
                cv2.putText(frame, 'No green screen found', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            mask_inv = cv2.bitwise_not(mask)
            frame_fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
            background_bg = cv2.bitwise_and(background, background, mask=mask)
            result = cv2.add(frame_fg, background_bg)

            out.write(result)
            cv2.imshow("Result", result)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    images = Images()
    images.zad_1("median")