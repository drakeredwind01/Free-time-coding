def get_dog_details_if_ladder(breed):
    """Retrieves details about a dog breed using an if/elif/else ladder."""
    if breed == "Labrador Retriever":
        return {"size": "Medium-Large", "temperament": "Friendly, Energetic, Loyal"}
    elif breed == "Golden Retriever":
        return {"size": "Large", "temperament": "Intelligent, Kind, Confident"}
    elif breed == "Pug":
        return {"size": "Small", "temperament": "Charming, Playful, Stubborn"}
    elif breed == "German Shepherd":
        return {"size": "Large", "temperament": "Intelligent, Loyal, Protective"}
    else:
        return "Breed not found in our database."

# Example usage
breed_name = "Golden Retriever"
details = get_dog_details_if_ladder(breed_name)
print(f"Details for {breed_name}: {details}")

breed_name = "Beagle"
details = get_dog_details_if_ladder(breed_name)
print(f"Details for {breed_name}: {details}")