from bs4 import BeautifulSoup
import requests  # Import requests library to fetch the HTML content

def get_html_content(url):
  """Fetches the HTML content from the given URL."""
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception for failed requests
  return response.content

def extract_data(html_content):
  """Extracts the data from the HTML content and generates the table structure."""
  soup = BeautifulSoup(html_content, 'html.parser')

  categories = soup.find_all('div', class_='seriesView')
  data = []

  for category in categories:
    category_name = category.find('div', class_='displayName').text.strip()
    levels = category.find('div', class_='iconHolder').find_all('div', class_='index')
    for level in levels:
      level_number = level.find('div', class_='indexNum').text.strip()
      description_element = level.find_next_sibling('a')  # Find the next sibling 'a' element for description
      if description_element:
        description = description_element.find_next_sibling(text=lambda text: isinstance(text, str) and text.strip())  # Find the next text sibling
      else:
        description = ""
      data.append((category_name, level_number, description))

  # Generate table structure with separator lines
  table_output = ""
  for row in data:
    table_output += f"| {row[0]} | {row[1]} | {row[2]} |\n"
    table_output += "|---|---|---|\n"

  return table_output

if __name__ == "__main__":
  url = "https://learngitbranching.js.org"
  html_content = get_html_content(url)
  table_data = extract_data(html_content)
  print(table_data)
  print(extract_data)