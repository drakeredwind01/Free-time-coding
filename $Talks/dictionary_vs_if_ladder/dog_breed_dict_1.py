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

# Example usage
breed_name = "Labrador Retriever"
details = get_dog_details_dict(breed_name)
print(f"Details for {breed_name}: {details}")

breed_name = "Poodle"
details = get_dog_details_dict(breed_name)
print(f"Details for {breed_name}: {details}")