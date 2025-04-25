# LEGB_4.py
import LEGB_3

# DOG_NAME = "ACE"
LEGB_3.DOG_NAME = "ACE" #rename before LEGB_3 prints

LEGB_3.print_dog_data()

print(f"Dog's starting age: {LEGB_3.DOG_AGE}")

LEGB_3.dog_grow()
LEGB_3.dog_grow()

LEGB_3.DOG_AGE = 5

print(f"Dog's current age: {LEGB_3.DOG_AGE}")
LEGB_3.dog_grow()
