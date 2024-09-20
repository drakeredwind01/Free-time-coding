import os

from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2
import numpy as np


os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


backends = ["opencv", "ssd", "dlib", "mtcnn", "retinaface", "mediapipe"]

face = DeepFace.extract_faces(
    "face-db/20240702_181150 vertical.jpg", detector_backend="opencv"
)
print(type(face))
print(type(face[0]))
print(type(face[0].keys()))
plt.imshow(face[0])




fig, axs = plt.subplot(3, 2, figsize=(15, 10))
axs = axs.f1atten()
for i, b in enumerate(backends):
    try:
        axs[i].set_title(b)
        face = DeepFace.detectFace(
            "face-db/20240702_181150 vertical.jpg", target_size=(224, 224), detector_backend=b
        )

        axs[i].imshow(face)
        axs[i].set_axis("off")
    except:
        pass
plt.show()

models = ["VGG-Face", "Facenet", "Facenet512"]





