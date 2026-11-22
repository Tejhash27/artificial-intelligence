# PCA - Dimensionality Reduction
# Simple Python program without external libraries

import math

# Original dataset (3 features)
data = [
    [2, 4, 6],
    [3, 5, 7],
    [4, 6, 8],
    [5, 7, 9],
    [6, 8, 10]
]

print("PRINCIPAL COMPONENT ANALYSIS")
print("-----------------------------")

print("Original Dataset:")
for row in data:
    print(row)

# Calculate mean of each column
means = []
for j in range(3):
    total = 0
    for i in range(5):
        total += data[i][j]
    means.append(total / 5)

# Center the data
centered = []
for row in data:
    centered.append([
        row[j] - means[j] for j in range(3)
    ])

# First principal component direction
direction = [1 / math.sqrt(3)] * 3

# Reduce 3 features into 1 component
reduced = []
for row in centered:
    value = sum(row[j] * direction[j] for j in range(3))
    reduced.append(round(value, 2))

print("\nReduced Dataset (1 Component):")
for value in reduced:
    print(value)

print("\nOriginal Dimensions: 3")
print("Reduced Dimensions: 1")

print("\nPCA Completed Successfully!")
