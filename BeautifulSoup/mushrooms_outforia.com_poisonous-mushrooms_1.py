

#!/usr/bin/env python
# coding: utf-8

# In[51]:


from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from io import open
import os


source = requests.get('https://outforia.com/poisonous-mushrooms/')
souped = BeautifulSoup(source.content, 'html.parser')
imgs = souped.find_all('img')

# In[79]:

for img in tqdm(imgs):
    imglink = img.attrs.get('src')

    # If the imglink does not end in .jpg, skip it.
    if not imglink.endswith('.jpg'):
        continue

    image = requests.get(imglink).content
    filename = r'D:\documents\GitHub\Free time coding\_MINDMAP\mushrooms_poisonous'+imglink[imglink.rfind('/'):]
    print(filename)
    '''
    # Create the directory if it does not exist.
    if not os.path.exists('../_MINDMAP/mushrooms'):
        os.mkdir('../_MINDMAP/mushrooms')

    # Write the image to the file.
    with open(filename, "wb") as file:
        file.write(image)
        
1__Death_Cap__Amanita_phalloides_.jpg
2__Funeral_Bell__Galerina_marginata_.jpg
3__Panther_Cap__Amanita_pantherina_.jpg
4__Lilac_Elf_Cup__Sarcosphaera_coronaria_.jpg


name 1
/html/body/div[2]/div[1]/div[2]/main/article/div/div[2]/h2[1]
<h2 id="otoc-1-death-cap-amanita-phalloides" class="wp-block-heading ftwp-heading">1. Death Cap (<em>Amanita phalloides</em>)</h2>
image 1
/html/body/div[2]/div[1]/div[2]/main/article/div/div[2]/figure[2]/picture/img
<img src="https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-2-03152023.jpg" height="664" width="1000" srcset="https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-2-03152023.jpg 1000w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-2-03152023-300x199.jpg 300w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-2-03152023-768x510.jpg 768w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-2-03152023-495x329.jpg 495w" sizes="(max-width: 1000px) 100vw, 1000px" class="wp-image-71437 sp-no-webp" alt="Death Cap (Amanita phalloides) on a soil been dug" decoding="async" loading="lazy">
name 2
/html/body/div[2]/div[1]/div[2]/main/article/div/div[2]/h2[2]
<h2 id="otoc-2-funeral-bell-galerina-marginata" class="wp-block-heading ftwp-heading">2. Funeral Bell (<em>Galerina marginata</em>)</h2>
image 2
/html/body/div[2]/div[1]/div[2]/main/article/div/div[2]/figure[3]/picture/img
<img src="https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-3-03152023.jpg" height="667" width="1000" srcset="https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-3-03152023.jpg 1000w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-3-03152023-300x200.jpg 300w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-3-03152023-768x512.jpg 768w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-3-03152023-600x400.jpg 600w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-3-03152023-493x329.jpg 493w" sizes="(max-width: 1000px) 100vw, 1000px" class="wp-image-71438 sp-no-webp" alt="Funeral Bell (Galerina marginata) growing with clover leaves surround it" decoding="async" loading="lazy">
name 3 
/html/body/div[2]/div[1]/div[2]/main/article/div/div[2]/h2[3]
<h2 id="otoc-3-panther-cap-amanita-pantherina" class="wp-block-heading ftwp-heading">3. Panther Cap (<em>Amanita pantherina)</em></h2>
image 3
/html/body/div[2]/div[1]/div[2]/main/article/div/div[2]/figure[5]/picture/img
<img src="https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-4-03152023.jpg" height="665" width="1000" srcset="https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-4-03152023.jpg 1000w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-4-03152023-300x200.jpg 300w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-4-03152023-768x511.jpg 768w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-4-03152023-600x400.jpg 600w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-4-03152023-495x329.jpg 495w" sizes="(max-width: 1000px) 100vw, 1000px" class="wp-image-71440 sp-no-webp" alt="Panther Cap (Amanita pantherina) growing on a random land" decoding="async" loading="lazy">
name 4 
/html/body/div[2]/div[1]/div[2]/main/article/div/div[2]/h2[4]
<h2 id="otoc-4-lilac-elf-cup-sarcosphaera-coronaria" class="wp-block-heading ftwp-heading">4. Lilac Elf Cup (<em>Sarcosphaera coronaria)</em></h2>
image 4
/html/body/div[2]/div[1]/div[2]/main/article/div/div[2]/figure[7]/picture/img
<img src="https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-5-03152023.jpg" height="664" width="1000" srcset="https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-5-03152023.jpg 1000w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-5-03152023-300x199.jpg 300w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-5-03152023-768x510.jpg 768w, https://outforia.com/wp-content/uploads/2023/04/poisonous-mushrooms-5-03152023-495x329.jpg 495w" sizes="(max-width: 1000px) 100vw, 1000px" class="wp-image-71442 sp-no-webp" alt="Lilac Elf Cup (Sarcosphaera coronaria) in the middle of fallen dry leaves" decoding="async" loading="lazy">


'''









