# K-Nearest Neighbors Classification

import math
from collections import Counter

# Training dataset
data = [
    [2, 3, "A"],
    [3, 4, "A"],
    [4, 3, "A"],
    [6, 7, "B"],
    [7, 8, "B"],
    [8, 7, "B"]
]

# New data to classify
new_point = [5, 5]

# Number of nearest neighbors
k = 3

# Calculate Euclidean distance
distances = []

for point in data:
    d = math.sqrt(
        (point[0] - new_point[0]) ** 2 +
        (point[1] - new_point[1]) ** 2
    )

    distances.append((d, point[2]))

# Sort distances
distances.sort()

# Select K nearest neighbors
nearest = distances[:k]

# Find majority class
classes = [item[1] for item in nearest]
prediction = Counter(classes).most_common(1)[0][0]

# Display output
print("K-NEAREST NEIGHBORS CLASSIFICATION")
print("----------------------------------")

print("New Data:", new_point)
print("K Value:", k)

print("\nNearest Neighbors:")
for item in nearest:
    print("Distance:", round(item[0], 2),
          "Class:", item[1])

print("\nPredicted Class:", prediction)
print("Classification Completed Successfully!")
