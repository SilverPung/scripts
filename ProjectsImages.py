import cv2
import numpy as np
import time

class WebcamBase:
    
    def openWebcam(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Błąd: Nie można otworzyć kamery internetowej.")
            return None
        return cap

    def processFrame(self, cap, process_function):
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Błąd: Nie można odczytać klatki.")
                break

            process_function(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.getWindowProperty("Webcam Video", cv2.WND_PROP_VISIBLE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()

class FaceDetection(WebcamBase):
    
    def __init__(self):
        # Załaduj wstępnie wytrenowany klasyfikator Haar Cascade do wykrywania twarzy
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def faceDetection(self):
        cap = self.openWebcam()
        if cap is None:
            return

        def detect_faces(frame):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow('Webcam Video', frame)

        self.processFrame(cap, detect_faces)

    def blurFaces(self):
        cap = self.openWebcam()
        if cap is None:
            return

        def blur_faces(frame):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            merged_faces = self.mergeOverlappingFaces(faces)
            for (x, y, w, h) in merged_faces:
                face = frame[y:y+h, x:x+w]
                face = cv2.GaussianBlur(face, (99, 99), 30)
                frame[y:y+face.shape[0], x:x+face.shape[1]] = face
            cv2.imshow('Webcam Video', frame)

        self.processFrame(cap, blur_faces)

    def mergeOverlappingFaces(self, faces):
        merged_faces = []
        for (x, y, w, h) in faces:
            merged = False
            for i, (mx, my, mw, mh) in enumerate(merged_faces):
                if (x < mx + mw and x + w > mx and y < my + mh and y + h > my):
                    merged_faces[i] = (min(x, mx), min(y, my), max(x + w, mx + mw) - min(x, mx), max(y + h, my + mh) - min(y, my))
                    merged = True
                    break
            if not merged:
                merged_faces.append((x, y, w, h))
        return merged_faces

class BallDetection(WebcamBase):
    
    def __init__(self):
        # Zdefiniuj listę punktów śledzenia i czasu, w którym zostały one dodane
        self.trail_points = []
        self.trail_duration = 3
        # Zdefiniuj zakres kolorów w formacie HSV
        self.color_lower = (25, 90, 90)  
        self.color_upper = (85, 255, 255)  
        self.ball_size = 200

    def findBall(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])
        mask = cv2.inRange(hsv, self.color_lower, self.color_upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def ballTracking(self):
        cap = self.openWebcam()
        if cap is None:
            return

        def track_ball(frame):
            contours = self.findBall(frame)
            for contour in contours:
                if cv2.contourArea(contour) > self.ball_size:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow('Webcam Video', frame)

        self.processFrame(cap, track_ball)

    def ballTrailing(self):
        cap = self.openWebcam()
        if cap is None:
            return

        def trail_ball(frame):
            contours = self.findBall(frame)
            for contour in contours:
                if cv2.contourArea(contour) > self.ball_size:
                    x, y, w, h = cv2.boundingRect(contour)
                    center = (x + w // 2, y + h // 2)
                    self.trail_points.append((center, time.time()))
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)

            current_time = time.time()
            self.trail_points = [(pt, t) for pt, t in self.trail_points if current_time - t <= self.trail_duration]

            for i in range(1, len(self.trail_points)):
                if self.trail_points[i - 1] is None or self.trail_points[i] is None:
                    continue
                alpha = (current_time - self.trail_points[i][1]) / self.trail_duration
                color = (0, int(255 * (1 - alpha)), int(255 * alpha))
                cv2.line(frame, self.trail_points[i - 1][0], self.trail_points[i][0], color, 2)

            cv2.imshow('Webcam Video', frame)

        self.processFrame(cap, trail_ball)

if __name__ == "__main__":

    bd = BallDetection()
    bd.ballTrailing()
