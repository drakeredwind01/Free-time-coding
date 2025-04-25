dog_info = {
    "Labrador Retriever": {"size": "Medium-Large", "temperament": "Friendly, Energetic, Loyal"},
    "Golden Retriever": {"size": "Large", "temperament": "Intelligent, Kind, Confident"},
    "Pug": {"size": "Small", "temperament": "Charming, Playful, Stubborn"},
    "German Shepherd": {"size": "Large", "temperament": "Intelligent, Loyal, Protective"},
}

def get_dog_details_dict(breed):
    """Retrieves details about a dog breed using a dictionary."""
    if breed in dog_info:
        return dog_info[breed]
    else:
        return "Breed not found in our database."

def format_dog_details(breed, details):
    """Formats the dog details into the desired output string."""
    if isinstance(details, dict):
        output = f"{breed}: size:{' ':<20}{details['size']},\n"
        output += f"{' ':<{len(breed) + 2}}temperament: {details['temperament']}"
        return output
    else:
        return f"{breed}: {details}"

# Example usage
breed_name = "Labrador Retriever"
details = get_dog_details_dict(breed_name)
print(format_dog_details(breed_name, details))

breed_name = "Poodle"
details = get_dog_details_dict(breed_name)
print(format_dog_details(breed_name, details))