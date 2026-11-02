import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

# 1. Load a sample dataset (Iris flower dataset)
iris = load_iris()
X = iris.data  # Features: sepal length/width, petal length/width
y = iris.target  # Target labels: species (Setosa, Versicolor, Virginica)

# 2. Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Initialize and train the Decision Tree Classifier
# max_depth=3 prevents the tree from overfitting
clf = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# 4. Make predictions on the test data
y_pred = clf.predict(X_test)

# 5. Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 6. Print the text-based decision rules
print("--- Text Rules of the Decision Tree ---")
tree_rules = export_text(clf, feature_names=list(iris.feature_names))
print(tree_rules)

# 7. Plot and save the visual tree structure
plt.figure(figsize=(12, 8))
plot_tree(
    clf,
    feature_names=iris.feature_names,
    class_names=list(iris.target_names),
    filled=True,
)
plt.title("Trained Decision Tree Diagram")
plt.show()
