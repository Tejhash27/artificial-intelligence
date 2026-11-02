
# Dimensionality Reduction using PCA

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample dataset
X = np.array([
    [2, 4, 6],
    [3, 5, 7],
    [4, 6, 8],
    [5, 7, 9],
    [6, 8, 10],
    [7, 9, 11]
])

print("Original Data:")
print(X)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)

X_reduced = pca.fit_transform(X_scaled)

# Display reduced data
print("\nReduced Data after PCA:")
print(X_reduced)

# Display explained variance
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nTotal Variance Retained:")
print(round(sum(pca.explained_variance_ratio_) * 100, 2), "%")

print("\nOriginal Dimensions:", X.shape[1])
print("Reduced Dimensions:", X_reduced.shape[1])
