
# Linear Regression Algorithm

from sklearn.linear_model import LinearRegression

# Training data
# Hours studied (X)
X = [[1], [2], [3], [4], [5]]

# Marks scored (Y)
y = [20, 40, 50, 60, 80]

# Create Linear Regression Model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Display coefficient and intercept
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict marks for new study hours
hours = [[6], [7], [8]]

predictions = model.predict(hours)

print("\nLinear Regression Predictions:")

for h, p in zip(hours, predictions):
    print("Study Hours:", h[0],
          "Predicted Marks:", round(p, 2))

# Predict for a single value
new_hours = [[9]]
result = model.predict(new_hours)

print("\nPredicted marks for 9 hours:",
      round(result[0], 2))
