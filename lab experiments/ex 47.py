# Hyperparameter Tuning using K-Nearest Neighbors (KNN)

# Training dataset
X_train = [
    [1, 2], [2, 3], [3, 3],
    [6, 7], [7, 8], [8, 8],
    [1, 1], [2, 2], [7, 7], [8, 9]
]

y_train = [
    "A", "A", "A",
    "B", "B", "B",
    "A", "A", "B", "B"
]

# Testing dataset
X_test = [
    [2, 2],
    [7, 8],
    [3, 2],
    [8, 8]
]

y_test = ["A", "B", "A", "B"]

# Calculate Euclidean distance
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 +
            (p1[1] - p2[1]) ** 2) ** 0.5

# KNN prediction function
def predict(point, k):
    distances = []

    for i in range(len(X_train)):
        d = distance(point, X_train[i])
        distances.append((d, y_train[i]))

    distances.sort(key=lambda x: x[0])

    votes = {}

    for i in range(k):
        label = distances[i][1]
        votes[label] = votes.get(label, 0) + 1

    return max(votes, key=votes.get)

# Hyperparameter tuning
best_k = 0
best_accuracy = 0

print("HYPERPARAMETER TUNING")
print("-----------------------------")

for k in [1, 3, 5]:

    correct = 0

    for i in range(len(X_test)):
        prediction = predict(X_test[i], k)

        if prediction == y_test[i]:
            correct += 1

    accuracy = (correct / len(y_test)) * 100

    print("K =", k, "Accuracy =", accuracy, "%")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k

# Display best result
print("-----------------------------")
print("Best K Value:", best_k)
print("Best Accuracy:", best_accuracy, "%")
print("Hyperparameter Tuning Completed Successfully!")
