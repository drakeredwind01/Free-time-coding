import yaml

def get_dog_details_yaml(breed, filepath="dogs.yaml"):
    """Retrieves details about a dog breed from a YAML file."""
    try:
        with open(filepath, 'r') as file:
            dog_data = yaml.safe_load(file)
            if dog_data and 'breeds' in dog_data and breed in dog_data['breeds']:
                return dog_data['breeds'][breed]
            else:
                return "Breed not found in our database."
    except FileNotFoundError:
        return f"Error: File not found at {filepath}"
    except yaml.YAMLError as e:
        return f"Error parsing YAML: {e}"

def format_dog_details(breed, details):
    """Formats the dog details into the desired output string."""
    if isinstance(details, dict):
        output = f"{breed}: size:{' ':<20}{details['size']},\n"
        output += f"{' ':<{len(breed) + 2}}temperament: {details['temperament']}"
        return output
    else:
        return f"{breed}: {details}"

# Example usage
breed_name = "Belgian Malinois"
details = get_dog_details_yaml(breed_name)
print(format_dog_details(breed_name, details))

breed_name = "Pug"
details = get_dog_details_yaml(breed_name)
print(format_dog_details(breed_name, details))

breed_name = "Corgi"
details = get_dog_details_yaml(breed_name)
print(format_dog_details(breed_name, details))