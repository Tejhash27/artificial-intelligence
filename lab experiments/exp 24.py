
# Neural Network for Image Classification using TensorFlow

import tensorflow as tf
from tensorflow.keras import layers, models

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize image data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Create Neural Network model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),

    layers.Dense(128, activation='relu'),

    layers.Dense(64, activation='relu'),

    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
print("Training Neural Network...")
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)

print("\nTest Accuracy:", round(accuracy * 100, 2), "%")

# Predict an image
predictions = model.predict(x_test[:5])

print("\nImage Classification Results:")

for i in range(5):
    predicted_digit = predictions[i].argmax()
    print("Actual Digit:", y_test[i])
    print("Predicted Digit:", predicted_digit)
    print("----------------------")
