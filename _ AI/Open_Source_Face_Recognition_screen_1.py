import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt

''' Detecting faces in images and compare'''

# img1_path = "face-db/20240702_181150 vertical small.jpg"
# img2_path = "face-db/20240702_181150 vertical small.jpg"
    # Facial Distance: -2.220446049250313e-16
# img2_path = "face-db/20240702_181150 vertical small clean.jpg"
# img2_path = "face-db/20240702_181150 vertical small dezine 2.png"
# img2_path = "face-db/20240702_181150 vertical small dezine 5.jpg"
img1_path = "face-db/The Tony Stark Fan Theory Giving MCU Fans Hope For His Return.png"
    # tony stark
    # Facial Distance: 0.9671053407167745
img2_path = "face-db/Keanu Reeves.png"
    # Keanu Reeves
    # Facial Distance: 0.9007293238015363
# img2_path = "face-db/pretty 412341cbc077e042472e44321d05b753.jpg"
    # pretty
    # Facial Distance: 0.53100888773325
# img2_path = "face-db/Demon face syndrome What it's like to have the rare disorder.png"
    # Demon face
    # Facial Distance: 0.9392891599859122
# img2_path = "face-db/Alicia Vikander  Lara Croft Wiki  Fandom.png"
    # Alicia Vikander
    # Facial Distance: 0.5954925394679208
# img2_path = "face-db/Chinese Face.png"
    # Chinese Face
    # Facial Distance: 0.9380507332789177
# img2_path = "face-db/Emperor Palpatine without hood.png"
    # Emperor Palpatine
    # Facial Distance: error
# img2_path = "face-db/"



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
