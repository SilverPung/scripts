import cv2
import numpy as np
import time

class ProjectsImages:
    
    def __init__(self):
        # Load the pre-trained Haar Cascade classifier for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.trail_points = []
        self.trail_duration = 2
        self.color_lower = (0, 80, 0)
        self.color_upper = (120, 255, 80)
        self.ball_size= 250
        


    def faceDetection(self):
        # Open a connection to the webcam (0 is the default camera)
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read frame.")
                break

            # Convert the frame to grayscale (Haar Cascade works better on grayscale images)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


            # Display the resulting frame
            cv2.imshow('Webcam Video', frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.getWindowProperty("Webcam Video", cv2.WND_PROP_VISIBLE) < 1:
                break

        # When everything is done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    def blurFaces(self):
        # Open a connection to the webcam (0 is the default camera)
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read frame.")
                break

            # Convert the frame to grayscale (Haar Cascade works better on grayscale images)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Merge overlapping face detections
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

            # Blur the merged faces
            for (x, y, w, h) in merged_faces:
                face = frame[y:y+h, x:x+w]
                face = cv2.GaussianBlur(face, (99, 99), 30)
                frame[y:y+face.shape[0], x:x+face.shape[1]] = face

            # Display the resulting frame
            cv2.imshow('Webcam Video', frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.getWindowProperty("Webcam Video", cv2.WND_PROP_VISIBLE) < 1:
                break

        # When everything is done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    def ballTracking(self):
        # Open a connection to the webcam (0 is the default camera)
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read frame.")
                break



            mask = cv2.inRange(frame, self.color_lower, self.color_upper)

            # Find contours in the mask
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Draw rectangles around the detected objects
            for contour in contours:
                if cv2.contourArea(contour) > self.ball_size:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Webcam Video', frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.getWindowProperty("Webcam Video", cv2.WND_PROP_VISIBLE) < 1:
                break

        # When everything is done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    def ballTrailing(self):
        # Open a connection to the webcam (0 is the default camera)
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read frame.")
                break

            # Define the color range for the object (e.g., a green ball)
            mask = cv2.inRange(frame, self.color_lower, self.color_upper)

            # Find contours in the mask
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Draw rectangles around the detected objects
            for contour in contours:
                if cv2.contourArea(contour) > self.ball_size:
                    # Get the center of the ball
                    x, y, w, h = cv2.boundingRect(contour)
                    center = (x + w // 2, y + h // 2)
                    self.trail_points.append((center, time.time()))

                    # Draw the ball
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)

            # Remove old trail points
            current_time = time.time()
            self.trail_points = [(pt, t) for pt, t in self.trail_points if current_time - t <= self.trail_duration]

            # Draw the trail with fading effect
            for i in range(1, len(self.trail_points)):
                if self.trail_points[i - 1] is None or self.trail_points[i] is None:
                    continue
                # Calculate the color intensity based on the time elapsed
                alpha = (current_time - self.trail_points[i][1]) / self.trail_duration
                color = (0, int(255 * (1 - alpha)), int(255 * alpha))
                cv2.line(frame, self.trail_points[i - 1][0], self.trail_points[i][0], color, 2)

            # Display the resulting frame
            cv2.imshow('Webcam Video', frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.getWindowProperty("Webcam Video", cv2.WND_PROP_VISIBLE) < 1:
                break

        # When everything is done, release the capture
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    pi = ProjectsImages()
    pi.ballTrailing()
