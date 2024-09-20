import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt

img1_path = "face-db/20240702_181150 vertical small.jpg"
# img2_path = "face-db/20240702_181150 vertical small.jpg"
    # Facial Distance: -2.220446049250313e-16
img2_path = "face-db/20240702_181150 vertical small clean.jpg"
# img2_path = "face-db/20240702_181150 vertical small dezine 2.png"
# img2_path = "face-db/20240702_181150 vertical small dezine 5.jpg"



img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

# Show the images (optional)
plt.imshow(img1[:, :, ::-1])
plt.show()
plt.imshow(img2[:, :, ::-1])
plt.show()

result = DeepFace.verify(img1_path, img2_path)

# Access the facial distance
facial_distance = result['distance']

# Print the distance
print(f"Facial Distance: {facial_distance}")
