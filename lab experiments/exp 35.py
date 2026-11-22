# Decision Tree Classification Program

from sklearn.tree import DecisionTreeClassifier

# Training data
# Input: Study hours
X = [[1], [2], [3], [4], [5], [6], [7], [8]]

# Output: 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1, 1, 1]

# Create decision tree model
model = DecisionTreeClassifier(random_state=0)

# Train the model
model.fit(X, y)

# Test data
test_data = [[2], [4], [6], [8]]

# Predict results
predictions = model.predict(test_data)

# Display output
print("DECISION TREE CLASSIFICATION")
print("============================")

for i in range(len(test_data)):
    hours = test_data[i][0]

    if predictions[i] == 1:
        result = "PASS"
    else:
        result = "FAIL"

    print("Study Hours:", hours)
    print("Prediction:", result)
    print("----------------------------")

print("Program Executed Successfully!")
