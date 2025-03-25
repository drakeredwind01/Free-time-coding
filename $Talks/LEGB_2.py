# LEGB_1.py
# LEGB_2.py
import LEGB_1

print(f"Dog's starting age: {LEGB_1.DOG_AGE}")

LEGB_1.dog_grow()
LEGB_1.dog_grow()

LEGB_1.DOG_AGE = 5  # Manually age the dog

print(f"Dog's current age: {LEGB_1.DOG_AGE}")
LEGB_1.dog_grow() # show the new age is used.