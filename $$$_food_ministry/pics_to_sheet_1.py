from PIL import Image
from pytesseract import image_to_string
import os
import pandas as pd

def extract_data_from_image(image_path):
    """
    Extracts date, time, and lbs from the given image using OCR.

    Args:
        image_path: Path to the image file.

    Returns:
        A tuple containing date, time, and lbs (or None if extraction fails).
    """
    try:
        img = Image.open(image_path)
        text = image_to_string(img)

        # Extract data using regular expressions
        import re
        date_pattern = r"(\d{1,2}/\d{1,2}/\d{2})"
        time_pattern = r"(\d{1,2}:\d{2})"
        lbs_pattern = r"(\d+\.\d{2})"

        date = re.search(date_pattern, text).group(1) if re.search(date_pattern, text) else None
        time = re.search(time_pattern, text).group(1) if re.search(time_pattern, text) else None
        lbs = re.search(lbs_pattern, text).group(1) if re.search(lbs_pattern, text) else None

        return date, time, lbs

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None, None, None

def process_images_in_directory(directory_path):
    """
    Processes all JPG images in the given directory and extracts data.

    Args:
        directory_path: Path to the directory containing images.

    Returns:
        A pandas DataFrame containing the extracted data.
    """
    data = []
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.jpg'):
            image_path = os.path.join(directory_path, filename)
            date, time, lbs = extract_data_from_image(image_path)
            if date and time and lbs:
                data.append({'Date': date, 'Time': time, 'Lbs': lbs})
    return pd.DataFrame(data)

# Example usage
directory_path = "D:\Documents\github\Free-time-coding\$$$_food_ministry\pics"
df = process_images_in_directory(directory_path)

# Save data to an Excel file
df.to_excel("extracted_data.xlsx", index=False)

print("Data extraction complete. Results saved to extracted_data.xlsx")