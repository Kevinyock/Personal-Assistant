import cv2
import numpy

class FacialRecognition():
    def __init__(self):
        print("Facial Recogition Module Online")
        capture = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

        # Check if our camera is connected, if not inform user
        if (capture.isOpened()):
            while True:
                # Captures Each Frame
                ret, frame=capture.read()

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                faces = face_detector.detectMultiScale(
                    gray,
                    scaleFactor = 1.1,
                    minNeighbors = 5
                )

                # Draw a rectangle around the faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                cv2.imshow('Color',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            capture.release()
            cv2.destroyAllWindows()
        else:
            print("Unable to find primary camera")



