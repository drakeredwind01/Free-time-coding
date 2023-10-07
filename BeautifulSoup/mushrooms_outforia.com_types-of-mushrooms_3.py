'''

IDK why this won't work and it's getting too complicated so instead
I found a way for it to ignore all files save for .jpb in:
    if not imglink.endswith('.jpg'):
        continue
also I used the wrong URL 'https://thegardeningcook.com/herb-identification/'
it should have been       'https://outforia.com/types-of-mushrooms/'

'''


#!/usr/bin/env python
# coding: utf-8

# In[51]:


from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from io import open
import os


source = requests.get('https://outforia.com/types-of-mushrooms/')
souped = BeautifulSoup(source.content, 'html.parser')
imgs = souped.find_all('img')

# In[79]:

for img in tqdm(imgs):
    imglink = img.attrs.get('src')

    # If the imglink does not end in .jpg, skip it.
    if not imglink.endswith('.jpg'):
        continue

    image = requests.get(imglink).content
    filename = r'D:\documents\GitHub\Free time coding\_MINDMAP\mushrooms'+imglink[imglink.rfind('/'):]

    # Create the directory if it does not exist.
    if not os.path.exists('../_MINDMAP/mushrooms'):
        os.mkdir('../_MINDMAP/mushrooms')

    # Write the image to the file.
    with open(filename, "wb") as file:
        file.write(image)
