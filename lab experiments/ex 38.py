# Support Vector Machine for Binary Classification

from sklearn import svm

# Training dataset
# Input data
X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 7],
    [7, 8],
    [8, 8]
]

# Output labels
# 0 = Class A
# 1 = Class B
y = [0, 0, 0, 1, 1, 1]

# Create SVM model
model = svm.SVC(kernel='linear')

# Train the model
model.fit(X, y)

# Test data
test_data = [
    [2, 2],
    [7, 7],
    [3, 4],
    [8, 9]
]

# Predict the classes
predictions = model.predict(test_data)

# Display results
print("SUPPORT VECTOR MACHINE")
print("-----------------------------")

for i in range(len(test_data)):

    print("Input:", test_data[i])

    if predictions[i] == 0:
        print("Predicted Class: A")
    else:
        print("Predicted Class: B")

    print("-----------------------------")

print("Classification Completed Successfully!")
