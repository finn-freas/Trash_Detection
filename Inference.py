import torch
import cv2

# Load YOLOv5 model from local weights
model = torch.hub.load('ultralytics/yolov5', 'custom', path='Best_Weights.pt', force_reload=True)
model.conf = 0.01  # set confidence threshold (I recommend 0.01)

# Load image
img = 'img.png'  # relative path to your test image

# Run inference
results = model(img)

# Results
results.print()
results.show()  
results.save()  # saves results in runs/detect/exp by default
