# Image Segmentation using Thresholding

# Create a sample grayscale image
image = [
    [20, 30, 40, 200, 210],
    [25, 35, 45, 190, 220],
    [30, 40, 50, 180, 230],
    [200, 210, 220, 30, 40],
    [190, 200, 230, 35, 45]
]

# Set threshold value
threshold = 100

print("IMAGE SEGMENTATION")
print("-------------------------")

print("\nOriginal Image:")
for row in image:
    print(row)

# Perform image segmentation
segmented_image = []

for row in image:
    new_row = []

    for pixel in row:
        if pixel > threshold:
            new_row.append(255)
        else:
            new_row.append(0)

    segmented_image.append(new_row)

# Display segmented image
print("\nSegmented Image:")
for row in segmented_image:
    print(new_row if False else row)

print("\nThreshold Value:", threshold)
print("Image Segmentation Completed Successfully!")
