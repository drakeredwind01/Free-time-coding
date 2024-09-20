import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote
import re

# URL to scrape
url = "https://tenor.com/search/hot-fan-gifs"

# Directory to save the GIFs
save_dir = "gifs"
os.makedirs(save_dir, exist_ok=True)

# Function to sanitize file names
def sanitize_filename(filename):
    # Replace characters not allowed in Windows file names with hyphens
    return re.sub(r'[<>:"/\\|?*]', '-', filename)

# Request the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all GIFs
gif_tags = soup.find_all("img", {"src": lambda x: x and x.endswith(".gif")})

# Download each GIF
for gif_tag in gif_tags:
    gif_url = gif_tag["src"]
    # Unquote to remove URL encoding, then get the file name
    default_name = os.path.basename(unquote(gif_url))

    # Find the title of the gif
    title = gif_tag.get("alt", "untitled").replace(" ", "-")

    # Sanitize the title to remove invalid characters
    title = sanitize_filename(title)

    # Create the file name
    file_name = f"tenor.com-{title}-{default_name}"

    # Save the GIF
    gif_content = requests.get(urljoin(url, gif_url)).content
    with open(os.path.join(save_dir, file_name), "wb") as gif_file:
        gif_file.write(gif_content)

    print(f"Saved {file_name}")

print("Download complete!")


'''
now i want it to work with multiple urls like this
https://tenor.com/search/cute-puppy-gifs
https://tenor.com/search/cute-kitty-gifs
https://tenor.com/search/hot-fan-gifs


'''
