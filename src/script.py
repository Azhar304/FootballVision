from ultralytics import YOLO
import cv2

# Load the EasyChamp YOLOv8 weights directly from Hugging Face
model = YOLO("https://huggingface.co/aabyzov/easychamp-player-detection-yolov8/resolve/main/player_detection_best.pt")

# we can play with this
model.overrides['conf'] = 0.3

print("Model loaded!")


