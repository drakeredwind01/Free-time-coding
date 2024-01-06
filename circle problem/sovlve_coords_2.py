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

# Identify non-overlapping circles
non_overlapping = []
for i, (x1, y1, r1) in enumerate(circles):
    overlaps = False
    for j, (x2, y2, r2) in enumerate(circles):
        if i != j:  # Don't compare with itself
            distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if distance <= r1 + r2:
                overlaps = True
                break  # No need to check further if a collision is found
    if not overlaps:
        non_overlapping.append((x1, y1, r1))

# Print non-overlapping circles
print("Non-overlapping circles:")
for x, y, r in non_overlapping:
    print(f"({x:.2f}, {y:.2f}, {r:.2f})")

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
