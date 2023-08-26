import cv2, time, os, tensorflow as tf
import numpy as np

from tensorflow.python.keras.utils.data_utils import get_file

np.random.seed(123)

class Detector:
    def __init__(self):
        pass

    def readClasses(self, classesFilePath):
        with open(classesFilePath, 'r') as f:
            self.classesList = f.read().splitlines()

            #colors list
            slef.colorList = np.random.uniform(low=0, high=225, size=(len(self.classesList),3))

            print(len(self.classesList), len(self.colorList))