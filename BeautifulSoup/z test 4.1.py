import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote
import re
import uuid  # For generating unique filenames

# List of URLs to scrape
urls = [
    "https://giphy.com/explore/cute-animated",
    "https://giphy.com/reactions",
    "https://www.itsnicethat.com/news/giphy-2021-gifs-and-clips-of-the-year-animation-031221",
    "https://www.itsnicethat.com/news/giphy-2021-gifs-and-clips-of-the-year-animation-031221",
    "https://drippingquills.com/t/share-cute-gifs/3511",
]

# Directory to save the images
save_dir = "gifs"
os.makedirs(save_dir, exist_ok=True)

# Function to sanitize file names
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '-', filename)

# Function to check if a URL is valid
def is_valid_url(url):
    return url.startswith('http') or url.startswith('//')

# Function to download an image from a URL
def download_image(img_url, save_dir):
    try:
        response = requests.get(img_url, stream=True)
        content_type = response.headers.get('content-type')

        # Check if the content is an image or gif
        if 'image' in content_type:
            # Generate a unique filename to avoid overwriting
            file_extension = content_type.split('/')[-1]
            file_name = f"image-{uuid.uuid4()}.{file_extension}"
            file_name = sanitize_filename(file_name)

            # Save the image
            with open(os.path.join(save_dir, file_name), "wb") as img_file:
                img_file.write(response.content)
            print(f"Saved {file_name}")
        else:
            print(f"Skipped non-image content: {img_url}")

    except Exception as e:
        print(f"Failed to download {img_url}: {str(e)}")

# Function to download images from a URL
def download_images_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all potential image URLs in the page
        img_urls = set()

        # Check for images in img, video, and source tags
        for tag in soup.find_all(["img", "video", "source"]):
            for attr in ["src", "data-src", "data-gif", "poster"]:
                img_url = tag.get(attr)
                if img_url and is_valid_url(img_url):
                    img_urls.add(urljoin(url, img_url))

        # Check for images in links or background images in style attributes
        for tag in soup.find_all(["a", "div", "span"]):
            for attr in ["href", "style"]:
                img_url = tag.get(attr)
                if img_url and ".gif" in img_url and is_valid_url(img_url):
                    # Extract URL from style attribute if necessary
                    if "url(" in img_url:
                        img_url = img_url.split("url(")[1].split(")")[0].strip('"\'')
                    img_urls.add(urljoin(url, img_url))

        # Download each image found
        for img_url in img_urls:
            download_image(img_url, save_dir)

    except Exception as e:
        print(f"Failed to scrape {url}: {str(e)}")

# Iterate over each URL in the list
for url in urls:
    print(f"Downloading images from {url}")
    download_images_from_url(url)

print("All downloads complete!")
