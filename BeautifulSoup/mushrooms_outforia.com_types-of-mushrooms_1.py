#!/usr/bin/env python
# coding: utf-8

# In[51]:

'''
this failes because there is a .svg file

C:\Users\drakeredwind01\miniconda3\envs\tf\python.exe "D:\documents\GitHub\Free time coding\BeautifulSoup\mushrooms_outforia.com_types-of-mushrooms_1.py"
  2%|▏         | 2/81 [00:01<00:57,  1.38it/s]
Traceback (most recent call last):
  File "D:\documents\GitHub\Free time coding\BeautifulSoup\mushrooms_outforia.com_types-of-mushrooms_1.py", line 26, in <module>
    image = requests.get(imglink).content
  File "C:\Users\drakeredwind01\miniconda3\envs\tf\lib\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "C:\Users\drakeredwind01\miniconda3\envs\tf\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\drakeredwind01\miniconda3\envs\tf\lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\drakeredwind01\miniconda3\envs\tf\lib\site-packages\requests\sessions.py", line 697, in send
    adapter = self.get_adapter(url=request.url)
  File "C:\Users\drakeredwind01\miniconda3\envs\tf\lib\site-packages\requests\sessions.py", line 794, in get_adapter
    raise InvalidSchema(f"No connection adapters were found for {url!r}")
requests.exceptions.InvalidSchema: No connection adapters were found for "data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201000%20523'%3E%3Crect%20width='1000'%20height='523'%20style='fill:%23e3e3e3'/%3E%3C/svg%3E"

Process finished with exit code 1
'''
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from io import open
import os


source = requests.get('https://thegardeningcook.com/herb-identification/')
souped = BeautifulSoup(source.content, 'html.parser')
imgs = souped.find_all('img')

# In[79]:

for img in tqdm(imgs):
    imglink = img.attrs.get('src')
    image = requests.get(imglink).content
    filename = r'D:\documents\GitHub\Free time coding\_MINDMAP\mushrooms'+imglink[imglink.rfind('/'):]

    # Create the directory if it does not exist.
    if not os.path.exists('../_MINDMAP/mushrooms'):
        os.mkdir('../_MINDMAP/mushrooms')

    # Write the image to the file.
    with open(filename, "wb") as file:
        file.write(image)
