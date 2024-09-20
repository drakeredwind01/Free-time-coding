import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote
import re

# List of URLs to scrape
urls = [
    "https://giphy.com/explore/cute-animated",
    "https://giphy.com/reactions",
    "https://www.itsnicethat.com/news/giphy-2021-gifs-and-clips-of-the-year-animation-031221",
    "https://drippingquills.com/t/share-cute-gifs/3511",
]

# Directory to save the GIFs
save_dir = "gifs"
os.makedirs(save_dir, exist_ok=True)


# Function to sanitize file names
def sanitize_filename(filename):
    # Replace characters not allowed in Windows file names with hyphens
    return re.sub(r'[<>:"/\\|?*]', '-', filename)


# Function to download a GIF from a URL
def download_gif(gif_url, save_dir):
    # Unquote to remove URL encoding, then get the file name
    default_name = os.path.basename(unquote(gif_url))
    # Sanitize the default name
    default_name = sanitize_filename(default_name)
    # Create the file name
    file_name = f"gif-{default_name}"
    # Save the GIF
    gif_content = requests.get(gif_url).content
    with open(os.path.join(save_dir, file_name), "wb") as gif_file:
        gif_file.write(gif_content)
    print(f"Saved {file_name}")


# Function to download GIFs from a URL
def download_gifs_from_url(url):
    # Request the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all potential GIF URLs in the page (anything ending with .gif)
    gif_urls = set()

    # Check for .gif in img, video, and source tags
    for tag in soup.find_all(["img", "video", "source"]):
        for attr in ["src", "data-src", "data-gif", "poster"]:
            gif_url = tag.get(attr)
            if gif_url and gif_url.endswith(".gif"):
                gif_urls.add(urljoin(url, gif_url))

    # Check for .gif in links or background images in style attributes
    for tag in soup.find_all(["a", "div", "span"]):
        for attr in ["href", "style"]:
            gif_url = tag.get(attr)
            if gif_url and ".gif" in gif_url:
                # Extract URL from style attribute if necessary
                if "url(" in gif_url:
                    gif_url = gif_url.split("url(")[1].split(")")[0].strip('"\'')
                gif_urls.add(urljoin(url, gif_url))

    # Download each GIF found
    for gif_url in gif_urls:
        download_gif(gif_url, save_dir)


# Iterate over each URL in the list
for url in urls:
    print(f"Downloading GIFs from {url}")
    download_gifs_from_url(url)

print("All downloads complete!")


'''
this only found one more gif total
'''