import numpy as np
from PIL import Image
import cv2

SRC = 'images/src/'
TARGET = 'images/target/'

def test_shouldReduceFramesPerSecond():
    cap = cv2.VideoCapture(SRC + 'sample-video-short.mov')
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(TARGET + "output_frame_{}.png".format(count), gray)
            cv2.imshow("output", gray)
            count += 1
            print(count)

        else:
            print("break")
            break

    cv2.destroyAllWindows()
    cap.release()


