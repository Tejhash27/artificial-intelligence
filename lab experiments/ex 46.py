# Object Detection Using Pre-Trained YOLO Model

from ultralytics import YOLO
import os

# Load pre-trained YOLO model
model = YOLO("yolov8n.pt")

# Get image path from the user
image_path = input("Enter image file name: ")

# Check whether image exists
if os.path.exists(image_path):

    # Perform object detection
    results = model.predict(
        source=image_path,
        conf=0.25,
        save=True
    )

    print("\nOBJECT DETECTION RESULTS")
    print("-----------------------------")

    # Display detected objects
    for result in results:

        if result.boxes is not None and len(result.boxes) > 0:

            for box in result.boxes:
                class_id = int(box.cls.item())
                confidence = float(box.conf.item())

                object_name = model.names[class_id]

                print("Object:", object_name)
                print("Confidence:", round(confidence * 100, 2), "%")
                print("-----------------------------")

        else:
            print("No objects detected.")

    print("Object Detection Completed Successfully!")
    print("Detected image saved in the runs/detect folder.")

else:
    print("Error: Image file not found!")
    print("Please enter the correct image file name.")
