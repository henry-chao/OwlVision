import cv2
import numpy as np
import wx


class WebCam(object):

    def __init__(self):
        self.video_index = -1
        self.webcam = cv2.VideoCapture(self.video_index)

    def scan_for_source(self):
        while self.video_index < 10:
            self.video_index += 1
            print("Scanning for source. Using ID {}".format(self.video_index))
            self.webcam = cv2.VideoCapture(self.video_index)
            if self.has_webcam():
                return False
        self.video_index = 0
        self.webcam = cv2.VideoCapture(self.video_index)
        return False

    def has_webcam(self):
        _, frame = self.webcam.read()
        if(isinstance(frame, np.ndarray)):
            return True
        return False

    def get_image(self, w=None, h=None):
        _, frame = self.webcam.read()
        if w is not None and h is not None:
            frame = cv2.resize(frame, (w, h))
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def size(self):
        _, frame = self.webcam.read()
        return frame.shape[:2]
