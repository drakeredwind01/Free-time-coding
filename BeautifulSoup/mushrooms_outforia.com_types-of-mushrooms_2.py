#!/usr/bin/env python
# coding: utf-8

# In[51]:


from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from io import open
import os

# Import the DataURIAdapter from the requests-toolbelt package.
from requests_toolbelt.adapters import DataURIAdapter

# Create a new requests session.
session = requests.Session()

# Add the DataURIAdapter to the requests session.
session.mount('data', DataURIAdapter())

# Get the source code of the website.
source = session.get('https://thegardeningcook.com/herb-identification/')

# Parse the HTML content using BeautifulSoup.
souped = BeautifulSoup(source.content, 'html.parser')

# Find all of the img tags on the website.
imgs = souped.find_all('img')

# In[79]:

for img in tqdm(imgs):
    imglink = img.attrs.get('src')

    # If the imglink is a data URI, download the image using the DataURIAdapter.
    if imglink.startswith('data:image/svg+xml,'):
        image = session.get(imglink).content
    else:
        image = requests.get(imglink).content

    filename = r'D:\documents\GitHub\Free time coding\_MINDMAP\mushrooms'+imglink[imglink.rfind('/'):]

    # Create the directory if it does not exist.
    try:
        if not os.path.exists('../_MINDMAP/mushrooms'):
            os.mkdir('../_MINDMAP/mushrooms')
    except FileNotFoundError:
        pass

    # Write the image to the file.
    try:
        with open(filename, "wb") as file:
            file.write(image)
    except FileNotFoundError:
        pass
