'''
all file names are named as such:
"
latestcb=20160525130525
latestcb=20160910155440
latestcb=20170121230955
latestcb=20191114010533
"

'''
import os
import sys
import requests
from bs4 import BeautifulSoup

def download_image(image_url, download_to_folder):
  """Downloads the image at the given URL to the given folder.

  Args:
    image_url: The URL of the image to download.
    download_to_folder: The folder to download the image to.
  """

  try:
    response = requests.get(image_url)
    response.raise_for_status()
  except Exception as e:
    print(f"Error downloading image '{image_url}': {e}")
    return

  # Remove the question mark (`?`) character from the filename before calling the `open()` function.
  filename = os.path.join(download_to_folder, os.path.basename(image_url).replace("?", ""))

  with open(filename, "wb") as output_file:
    output_file.write(response.content)

def scrape_item_images(download_to_folder):
  """Scrapes all of the item images from the Terraria wiki and downloads them to the given folder.

  Args:
    download_to_folder: The folder to download the item images to.
  """

  # Create the download folder if it doesn't exist.
  if not os.path.exists(download_to_folder):
    os.makedirs(download_to_folder)

  # Get the first page of the Terraria item images category.
  response = requests.get("https://terraria.fandom.com/wiki/Category:Item_images")
  response.raise_for_status()

  # Parse the HTML response using BeautifulSoup.
  soup = BeautifulSoup(response.content, "html.parser")

  # Find all of the image links on the page.
  image_links = []
  for link in soup.find_all("a", class_="image"):
    image_links.append(link["href"])

  # Download all of the image links.
  for image_link in image_links:
    download_image(image_link, download_to_folder)

if __name__ == "__main__":
  # Get the download folder from the command line arguments.
  download_to_folder = sys.argv[1] if len(sys.argv) > 1 else "."

  # Scrape all of the item images from the Terraria wiki and download them to the download folder.
  scrape_item_images(download_to_folder)
