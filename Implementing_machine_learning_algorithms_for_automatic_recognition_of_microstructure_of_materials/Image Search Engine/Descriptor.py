# this file is used to create histograms for all the micrographs
import numpy as np
import cv2

class Descriptor:
    print('inside class')
    def __init__(self, bins):
        print('inside init')
        self.bins = bins
        print('bins:')
        print(self.bins)
    def describe(self, image):
  
        print('bins:', self.bins)
        print('inside describe')
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        features = []

        (h, w) = image.shape[:2]
        (cX, cY) = (round(w * 0.5), round(h * 0.5))

        segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),(0, cX, cY, h)]

        (axesX, axesY) = (round(w * 0.75 / 2), round(h * 0.75 / 2))
        ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
        cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)

        for (startX, endX, startY, endY) in segments:
            cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
            cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
            cornerMask = cv2.subtract(cornerMask, ellipMask)
            hist = self.histogram(image, cornerMask)
            features.extend(hist)
        hist = self.histogram(image, ellipMask)
        features.extend(hist)

        
        return features

    def histogram(self, image, mask):
        print('bins')
        print(self.bins)
        hist = cv2.calcHist(images=[image], channels=[0, 1, 2], mask=None,
                            histSize=self.bins, ranges=[0, 256] * 3)
        hist = cv2.normalize(hist, dst=hist.shape)
        return hist.flatten()
        return hist