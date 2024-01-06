import matplotlib.pyplot as plt
import numpy as np

# Read data from the text file
with open('cords.txt') as file:
    data = file.read()

# Extract data from the file contents
lines = data.strip().split('\n')
circles = []
for line in lines:
    x, y, r = map(float, line.split())
    circles.append((x, y, r))

# Create plot
fig, ax = plt.subplots()

# Draw circles
for x, y, r in circles:
    circle = plt.Circle((x, y), r, color='blue', fill=False)
    ax.add_patch(circle)

# Set limits slightly higher than max radius and offset by center of largest circle
r = max(rs for _, _, rs in circles)
ax.set_xlim(-r - r/5 + min(x for x, _, _ in circles), r + r/5 + max(x for x, _, _ in circles))
ax.set_ylim(-r - r/5 + min(y for _, y, _ in circles), r + r/5 + max(y for _, y, _ in circles))

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Circles')

# Show plot
plt.show()
