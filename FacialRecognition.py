import cv2
import numpy

class FacialRecognition():
    def __init__(self):
        print("Module Online")
        capture = cv2.VideoCapture(0)
        # Check if our camera is connected, if not inform user
        while(capture.isOpened()):
            while True:
                ret,frame=capture.read()
                cv2.imshow('Color',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            capture.release()
            cv2.destroyAllWindows()
        else:
            print("Unable to find primary camera")



