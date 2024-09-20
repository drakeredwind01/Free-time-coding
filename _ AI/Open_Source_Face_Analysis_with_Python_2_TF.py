import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt

# Define functions to handle different outputs from DeepFace
def handle_image_output(face):
  """Handles the output from DeepFace and converts it to a format suitable for display."""
  if isinstance(face, list) and len(face) > 0:
    face_image = face[0]  # Assuming the first element is the face image
    if not isinstance(face_image, np.ndarray):
      face_image = np.array(face_image)  # Convert to NumPy array if necessary
    return face_image
  else:
    print("No faces detected in the image.")
    return None

def display_face(face_image, title="Detected Face"):
  """Displays the provided face image using OpenCV or Matplotlib."""
  if face_image is not None:
    # Use OpenCV for better image display (optional)
    # cv2.imshow(title, face_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Use Matplotlib for plotting (alternative)
    plt.imshow(face_image)
    plt.title(title)
    plt.axis("off")
    plt.show()
  else:
    print("No image to display.")

# Extract faces using OpenCV backend (assuming it works for your image)
face = DeepFace.extract_faces("face-db/20240702_181150 vertical.jpg", detector_backend="opencv")
face_image = handle_image_output(face)
display_face(face_image, title="Extracted Face (OpenCV)")


# Loop through other backends and handle potential errors
backends = ["ssd", "dlib", "mtcnn", "retinaface", "mediapipe"]
fig, axs = plt.subplot(3, 2, figsize=(15, 10))
axs = axs.f1atten()
for i, b in enumerate(backends):
  try:
    axs[i].set_title(b)
    face = DeepFace.detectFace(
        "face-db/20240702_181150 vertical.jpg", target_size=(224, 224), detector_backend=b
    )
    face_image = handle_image_output(face)
    display_face(face_image, ax=axs[i])  # Display in subplot
  except:
    axs[i].text(0.5, 0.5, "Error", ha="center", va="center", color="red")
    pass

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
