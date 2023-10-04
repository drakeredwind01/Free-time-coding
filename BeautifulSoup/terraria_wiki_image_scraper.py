import os
import requests
from bs4 import BeautifulSoup

def download_image(image_url, download_to_folder):
  """Downloads the image at the given URL to the given folder.

  Args:
    image_url: The URL of the image to download.
    download_to_folder: The folder to download the image to.
  """

  # Create the download_to_folder folder if it doesn't exist.
  if not os.path.exists(download_to_folder):
    os.makedirs(download_to_folder)

  # Get the filename of the image.
  filename = os.path.basename(image_url)

  # Download the image.
  response = requests.get(image_url)
  with open(os.path.join(download_to_folder, filename), "wb") as output_file:
    output_file.write(response.content)

def scrape_terraria_wiki_images(download_to_folder):
  """Scrapes all of the images from the Terraria wiki and downloads them to the given folder.

  Args:
    download_to_folder: The folder to download the images to.
  """

  # Get the Terraria wiki URL.
  terraria_wiki_url = "https://terraria.fandom.com/wiki/Terraria_Wiki"

  # Make a request to the Terraria wiki URL.
  response = requests.get(terraria_wiki_url)

  # Parse the Terraria wiki HTML response using BeautifulSoup.
  soup = BeautifulSoup(response.content, "html.parser")

  # Find all of the image tags in the Terraria wiki HTML response.
  image_tags = soup.find_all("img")

  # Extract the image URLs from the image tags.
  image_urls = [image_tag["src"] for image_tag in image_tags]

  # Download all of the image URLs to the download_to_folder folder.
  for image_url in image_urls:
    try:
      download_image(image_url, download_to_folder)
    except Exception as e:
      print(f"Error downloading image '{image_url}': {e}")

def main():
  """Downloads all of the images from the Terraria wiki to the current folder.

  Usage:
    python terraria_wiki_image_scraper.py [download_to_folder]

  If no download_to_folder is specified, the images will be downloaded to the current folder.
  """

  # Get the download_to_folder from the command line arguments.
  download_to_folder = sys.argv[1] if len(sys.argv) > 1 else "."

  # Scrape the Terraria wiki images and download them to the download_to_folder folder.
  scrape_terraria_wiki_images(download_to_folder)

if __name__ == "__main__":
  main()
