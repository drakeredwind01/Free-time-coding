# LEGB_1.py
DOG_AGE = 1

def dog_grow():
    global DOG_AGE
    DOG_AGE += 1
    print(f"Dog grew to {DOG_AGE} years old.")

# Call the function to make it print something
dog_grow()