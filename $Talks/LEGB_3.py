# LEGB_3.py
DOG_NAME = "Fido"  # Initialize DOG_NAME without printing yet
DOG_AGE = 1        # Initialize DOG_AGE also changeable

def name_dog():
    global DOG_NAME
    DOG_NAME = "ACE"
    print(f"Dog's name changed to {DOG_NAME}")

def dog_grow():
    global DOG_AGE
    DOG_AGE += 1
    print(f"Dog grew to {DOG_AGE} years old.")

def print_dog_data(): #Added Function
    print(f"all the following data is for {DOG_NAME}")
    dog_grow()
