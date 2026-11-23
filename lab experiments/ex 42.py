# K-Means Clustering Algorithm

import math

# Dataset containing data points
data = [
    [1, 2],
    [2, 3],
    [3, 3],
    [8, 8],
    [9, 8],
    [8, 9]
]

# Initial cluster centers
centroids = [
    [1, 2],
    [8, 8]
]

# Function to calculate distance
def distance(point1, point2):
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2
    )

# K-Means algorithm
for iteration in range(5):

    clusters = [[], []]

    # Assign points to nearest centroid
    for point in data:
        d1 = distance(point, centroids[0])
        d2 = distance(point, centroids[1])

        if d1 < d2:
            clusters[0].append(point)
        else:
            clusters[1].append(point)

    # Update centroids
    for i in range(2):
        if len(clusters[i]) > 0:
            x = sum(point[0] for point in clusters[i])
            y = sum(point[1] for point in clusters[i])

            centroids[i] = [
                x / len(clusters[i]),
                y / len(clusters[i])
            ]

# Display results
print("K-MEANS CLUSTERING")
print("-----------------------------")

for i in range(2):
    print("\nCluster", i + 1, ":")
    for point in clusters[i]:
        print(point)

print("\nFinal Centroids:")
for centroid in centroids:
    print([round(value, 2) for value in centroid])

print("\nClustering Completed Successfully!")
