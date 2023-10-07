#!/usr/bin/env python
# coding: utf-8

# In[51]:


from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from io import open
import os
import requests.exceptions as requests_exceptions


source = requests.get('https://outforia.com/poisonous-mushrooms/')
souped = BeautifulSoup(source.content, 'html.parser')

# Get all of the mushroom names
names = souped.select('h2.wp-block-heading.ftwp-heading')

# Get all of the mushroom images
images = souped.select('img.wp-image-71437.sp-no-webp')

# Create a directory to store the mushroom images
if not os.path.exists('mushrooms_poisonous'):
    os.mkdir('mushrooms_poisonous')

# Download the mushroom images and save them with the mushroom names
for i in tqdm(range(len(names))):
    try:
        image = requests.get(images[i]['src'])
    except requests_exceptions.InvalidSchema:
        continue
    except IndexError:
        continue

    with open(os.path.join('mushrooms_poisonous', f'{names[i].text}.jpg'), 'wb') as f:
        f.write(image.content)
