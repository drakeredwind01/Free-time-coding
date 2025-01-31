import cv2
import numpy as np

def get_color_at_pixel(image, x, y):
    """Gets the color at a specific pixel in an image.

    Args:
        image: The image as a NumPy array.
        x: The x-coordinate of the pixel.
        y: The y-coordinate of the pixel.

    Returns:
        A tuple of (B, G, R) values representing the color at the pixel.
    """

    pixel_color = image[y, x]
    return pixel_color

def main():
    # Load the image
    image = cv2.imread('your_image.png')  # Replace 'your_image.png' with your actual image path

    # Specify the pixel coordinates
    x = 432
    y = 379

    # Get the color at the specified pixel
    color = get_color_at_pixel(image, x, y)

    # Print the color values (B, G, R)
    print("Color at pixel (", x, ",", y, ") is:", color)

if __name__ == "__main__":
    main()