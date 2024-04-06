import matplotlib.pyplot as plt
import numpy as np
import os
with open('_ data/names.txt', 'r') as keys:
    names = [line.strip() for line in keys.readlines()]

with open('_ data/numbers.txt', 'r') as values:
    numbers = [line.strip() for line in values.readlines()]

result_dict = dict(zip(names, numbers))  # Use dict(zip(...)) for dictionary creation
print(result_dict)
for name,number in zip(names,numbers):
    print(f"({name}, {number})")
