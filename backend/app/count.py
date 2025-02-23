import cv2
from ultralytics import YOLO
import numpy as np

def detect_person(image):
    """
    Detect persons in the image using YOLO model.

    Args:
        image: numpy array of the image

    Returns:
        list of bounding boxes in format [[x1,y1,x2,y2,confidence], ...]
    """
    # Initialize YOLO model
    model = YOLO('yolov8n.pt')  # using the nano model, you can change to other versions

    # Run inference
    results = model(image)

    # Extract person detections (class 0 in COCO dataset is person)
    boxes = []
    for result in results[0].boxes:
        if result.cls == 0:  # person class
            x1, y1, x2, y2 = result.xyxy[0].cpu().numpy()
            confidence = result.conf[0].cpu().numpy()
            boxes.append([int(x1), int(y1), int(x2), int(y2), float(confidence)])

    return boxes

def draw_bbxes_on_img(image, bbxes):
    """
    Draw bounding boxes on the image.

    Args:
        image: numpy array of the image
        bbxes: list of bounding boxes in format [[x1,y1,x2,y2,confidence], ...]

    Returns:
        image with drawn bounding boxes
    """
    img_with_boxes = image.copy()

    for box in bbxes:
        x1, y1, x2, y2, conf = box

        # Draw rectangle
        cv2.rectangle(img_with_boxes, 
                     (x1, y1), 
                     (x2, y2), 
                     (255, 0, 0),  # Red color
                     5)  # Thickness

        # Add confidence score
        label = f'Person {conf:.2f}'
        cv2.putText(img_with_boxes, 
                   label, 
                   (x1, y1-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 
                   0.5,  # Font scale
                   (0, 255, 0),  # Green color
                   2)  # Thickness

    return img_with_boxes

def count_person_in_img(image):
    """
    Count number of persons in the image and visualize detections.

    Args:
        image: numpy array of the image or path to image file

    Returns:
        tuple (count of persons, image with drawn bounding boxes)
    """
    # If image is a string (file path), load it
    if isinstance(image, str):
        image = cv2.imread(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect persons
    boxes = detect_person(image)

    # Draw boxes
    annotated_image = draw_bbxes_on_img(image, boxes)

    return len(boxes), annotated_image