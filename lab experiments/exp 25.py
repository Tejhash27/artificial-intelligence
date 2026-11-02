
# Decision Tree Classification using Python

from sklearn.tree import DecisionTreeClassifier

# Training data
# Features: [Age, Income]
X = [
    [22, 20000],
    [25, 25000],
    [47, 50000],
    [52, 60000],
    [46, 55000],
    [23, 22000]
]

# Class labels
# 0 = No
# 1 = Yes
y = [0, 0, 1, 1, 1, 0]

# Create Decision Tree classifier
model = DecisionTreeClassifier(random_state=0)

# Train the model
model.fit(X, y)

# Test data
test_data = [
    [30, 30000],
    [50, 58000],
    [24, 21000]
]

# Make predictions
predictions = model.predict(test_data)

# Display results
print("Decision Tree Classification Results")

for i in range(len(test_data)):
    result = "Yes" if predictions[i] == 1 else "No"

    print("Age:", test_data[i][0])
    print("Income:", test_data[i][1])
    print("Predicted Class:", result)
    print("----------------------")
