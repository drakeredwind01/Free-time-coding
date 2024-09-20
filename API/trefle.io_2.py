import requests

# Your Trefle API key
api_key = "hftxQiZ0wjHo5Gwuyy1wXY6e3pobfnaNT45vcw7wQK0"

# Base URL for the Trefle API
base_url = "http://trefle.io/api/v1"

# Endpoint to search for strawberries
search_endpoint = f"{base_url}/plants/search"

# Parameters for the search query
params = {
    "q": "strawberry",
    "token": api_key
}

# Make the API request to search for strawberries
response = requests.get(search_endpoint, params=params)
print(response.status_code)
if response.status_code == 200:
    search_results = response.json()['data']
    if search_results:
        for plant in search_results:
            plant_id = plant['id']
            # Endpoint to get detailed information about the plant
            plant_endpoint = f"{base_url}/plants/{plant_id}"

            # Make the API request to get detailed information about the plant
            plant_response = requests.get(plant_endpoint, params={"token": api_key})

            if plant_response.status_code == 200:
                plant_data = plant_response.json()['data']
                print(f"Name: {plant_data['common_name']} ({plant_data['scientific_name']})")
                print(f"Family: {plant_data['family_common_name']}")

                if plant_data.get('uses'):
                    print(f"Uses: {plant_data['uses']}")
                else:
                    print("Uses: Not available")

                print("-" * 40)
            else:
                print(f"Failed to retrieve details for plant ID: {plant_id}")
    else:
        print("No strawberry plants found.")
else:
    print("Failed to search for plants.")
