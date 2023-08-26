#2020.10.19.15.13.33.605


from urllib.request import urlopen
from bs4 import BeautifulSoup, BeautifulSoup

url_to_scrape = ""

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html')



if __name__ == '__main__':


















