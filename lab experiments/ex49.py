# Face Detection using Pre-trained Haar Cascade Model

import cv2
import os

# Load pre-trained face detection model
face_model = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Check whether model loaded correctly
if face_model.empty():
    print("Error: Face model not loaded!")
else:
    # Enter image file name
    image_path = input("Enter image file name: ")

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
    else:
        # Convert image to grayscale
        gray = cv2.cvtColor(
            image, cv2.COLOR_BGR2GRAY
        )

        # Detect faces
        faces = face_model.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        print("\nFACE DETECTION RESULTS")
        print("-----------------------------")
        print("Number of faces detected:", len(faces))

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(
                image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        # Save result
        cv2.imwrite("face_result.jpg", image)

        print("Output image saved as face_result.jpg")
        print("Face Detection Completed Successfully!")
