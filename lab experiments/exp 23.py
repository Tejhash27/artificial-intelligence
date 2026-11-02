
# K-Nearest Neighbors (KNN) Classification

from sklearn.neighbors import KNeighborsClassifier

# Training data
# Features: [Height, Weight]
X = [
    [150, 50],
    [160, 60],
    [170, 65],
    [180, 80],
    [155, 55],
    [175, 75]
]

# Class labels
y = [
    "Short",
    "Short",
    "Medium",
    "Tall",
    "Short",
    "Tall"
]

# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X, y)

# Test data
test_data = [
    [165, 62],
    [185, 85],
    [152, 52]
]

# Predict the classes
predictions = knn.predict(test_data)

# Display results
print("KNN Classification Results")

for i in range(len(test_data)):
    print("Input:", test_data[i])
    print("Predicted Class:", predictions[i])
    print("----------------------")
