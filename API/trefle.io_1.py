import requests

# Define the API key and base URL
api_key = 'hftxQiZ0wjHo5Gwuyy1wXY6e3pobfnaNT45vcw7wQK0'
base_url = 'https://trefle.io/api/v1/plants/search'

# Define the search query for strawberries
query = 'strawberry'

# Set up the parameters for the request
params = {
    'q': query,
    'token': api_key
}

# Make the request to the Trefle API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the retrieved data
    for plant in data['data']:
        print(f"Common Name: {plant.get('common_name', 'N/A')}")
        print(f"Scientific Name: {plant.get('scientific_name', 'N/A')}")
        print(f"Family: {plant.get('family', 'N/A')}")
        print(f"Genus: {plant.get('genus', 'N/A')}")
        print(f"Plant ID: {plant.get('id', 'N/A')}")
        print(f"Year: {plant.get('year', 'N/A')}")
        print(f"Bibliography: {plant.get('bibliography', 'N/A')}")
        print(f"Author: {plant.get('author', 'N/A')}")
        print(f"Status: {plant.get('status', 'N/A')}")
        print(f"Rank: {plant.get('rank', 'N/A')}")
        print(f"Family Common Name: {plant.get('family_common_name', 'N/A')}")
        print(f"Image URL: {plant.get('image_url', 'N/A')}")
        print(f"Duration: {plant.get('duration', 'N/A')}")
        print(f"Edible Part: {plant.get('edible_part', 'N/A')}")
        print(f"Edible Description: {plant.get('edible', 'N/A')}")
        print(f"Distribution: {plant.get('distribution', 'N/A')}")
        print(f"Foliage: {plant.get('foliage', 'N/A')}")
        print(f"Fruit or Seed: {plant.get('fruit_or_seed', 'N/A')}")
        print(f"Growth: {plant.get('growth', 'N/A')}")
        print(f"Specifications: {plant.get('specifications', 'N/A')}")
        print(f"Synonyms: {plant.get('synonyms', 'N/A')}")
        print('-' * 40)
else:
    print(f"Failed to retrieve data: {response.status_code}")
