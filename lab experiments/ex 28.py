
# Support Vector Machine for Binary Classification

from sklearn import svm

# Training data
# Features: [Study Hours, Attendance]
X = [
    [2, 40],
    [3, 50],
    [4, 60],
    [7, 80],
    [8, 90],
    [9, 95]
]

# Class labels
# 0 = Fail
# 1 = Pass
y = [0, 0, 0, 1, 1, 1]

# Create SVM classifier
model = svm.SVC(kernel='linear')

# Train the model
model.fit(X, y)

# Test data
test_data = [
    [3, 45],
    [8, 85],
    [5, 65]
]

# Predict the results
predictions = model.predict(test_data)

# Display results
print("SVM Binary Classification Results")

for i in range(len(test_data)):

    if predictions[i] == 1:
        result = "Pass"
    else:
        result = "Fail"

    print("Study Hours:", test_data[i][0])
    print("Attendance:", test_data[i][1])
    print("Predicted Result:", result)
    print("----------------------")
