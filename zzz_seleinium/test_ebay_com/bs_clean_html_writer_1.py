from bs4 import BeautifulSoup

input_file = "/home/drake/Documents/github/Free-time-coding/zzz_seleinium/test_ebay_com/Graphics Card for sale _ eBay.html"
output_file = "clean_ebay.html"

with open(input_file, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Remove scripts
for script in soup.find_all("script"):
    script.decompose()

# Remove iframes
for iframe in soup.find_all("iframe"):
    iframe.decompose()

# Remove noscript
for noscript in soup.find_all("noscript"):
    noscript.decompose()

with open(output_file, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Wrote clean_ebay.html")
