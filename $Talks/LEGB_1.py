# LEGB_1.py
DOG_AGE = 1

def dog_grow():
    global DOG_AGE
    DOG_AGE += 1
    # Use the global variable
    print(f"Dog grew to {DOG_AGE} years old.")
    # Dog grew to 2 years old.
# Call the function to make it print something
dog_grow()