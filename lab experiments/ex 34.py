# Neural Network for Flower Classification

from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load flower dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Create Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(10, 10),
    max_iter=2000,
    random_state=1,
    solver='lbfgs'
)

# Train the model
print("Training Neural Network...")
model.fit(X_train, y_train)

# Predict results
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display output
print("\nFLOWER CLASSIFICATION RESULTS")
print("--------------------------------")

print("Total Training Samples:", len(X_train))
print("Total Testing Samples:", len(X_test))
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Predict a new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_flower)

print("\nNew Flower Measurements:", new_flower)
print("Predicted Flower:", iris.target_names[prediction[0]])

print("\nClassification Completed Successfully!")
