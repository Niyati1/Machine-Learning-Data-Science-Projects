# this file is used to create histograms for all the micrographs
#import necessary libraries
import numpy as np
import cv2

class Descriptor:
    print('inside class')
    def __init__(self, bins):
        self.bins = bins        
    def describe(self, image):
  
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []

        (h, w) = image.shape[:2]
        (X, Y) = (round(w * 0.5), round(h * 0.5))

        objects = [(0, X, 0, Y), (X, w, 0, Y), (X, w, Y, h),(0, X, Y, h)]

        (X_n, Y_n) = (round(w * 0.75 / 2), round(h * 0.75 / 2))
        eMask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.ellipse(eMask, (X, Y), (X_n, Y_n), 0, 0, 360, 255, -1)

        for (s_X, e_X, s_Y, e_Y) in objects:
            cMask = np.zeros(image.shape[:2], dtype = "uint8")
            cv2.rectangle(cMask, (s_X, s_Y), (e_X, e_Y), 255, -1)
            cMask = cv2.subtract(cMask, eMask)
            hist = self.histogram(image, cMask)
            features.extend(hist)
        hist = self.histogram(image, eMask)
        features.extend(hist)
        return features

    def histogram(self, image, mask):
        hist = cv2.calcHist(images=[image], channels=[0, 1, 2], mask=None,
                            histSize=self.bins, ranges=[0, 256] * 3)
        hist = cv2.normalize(hist, dst=hist.shape)
        return hist.flatten()
        return hist
