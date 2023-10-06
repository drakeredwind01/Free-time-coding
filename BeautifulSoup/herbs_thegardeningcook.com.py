#!/usr/bin/env python
# coding: utf-8

# In[51]:


from bs4 import BeautifulSoup
import requests
import bs4 as bs
import urllib.request
from tqdm import tqdm
from io import open

source = requests.get('https://thegardeningcook.com/herb-identification/')
souped = BeautifulSoup(source.content, 'html.parser')
imgs = souped.find_all('img')

'''
for img in imgs[11::2]:
    imglink = img.attrs.get('src')
    print(imglink)
'''

# In[73]:
'''
for img in imgs[11::2]:
    imglink = img.attrs.get('src')
    image = requests.get(imglink).content
    filename = r'herbs'+imglink[imglink.rfind('/'):]
    print(filename,imglink)
'''

# In[79]:

for img in tqdm(imgs[11::2]):
    imglink = img.attrs.get('src')
    image = requests.get(imglink).content
    filename = r'herbs'+imglink[imglink.rfind('/'):]
    # wb = write binary(mode)
    with open(filename,'wb')as file:
        file.write(image)

