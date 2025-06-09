# Trash_Detection

Trash Detection Model (YOLOv5 PyTorch)

This repository contains a custom-trained YOLOv5 object detection model built with PyTorch to detect trash and litter in images. The model has been trained on a large dataset of labeled images containing various types of trash (plastic, cans, paper, bottles, etc.) in diverse environments such as streets, parks, beaches, and natural landscapes. The goal of this project is to support automated waste detection for applications such as:

- Autonomous trash-collecting drones

- Smart city monitoring

- Environmental cleanup initiatives

- Educational and research tools

### Features:

- Real-time object detection performance

- Can differentiate between different types of trash

- Supports batch image processing

- Lightweight and deployable to edge devices (Raspberry Pi, NVIDIA Jetson, etc.)

- Compatible with video streams for live detection

- Trained using YOLOv5 architecture and PyTorch framework

## Dataset

https://drive.google.com/drive/folders/1RZOjxU6KcMJte-Xc5aZ8q1uYAKh5kP35?usp=share_link

## Repository:

Best_Weights.pt — The trained YOLOv5 model weights

### Images:

![Mosaic](images/Mosaic_Confidence_1.png)

![Mosaic](images/Mosaic_Confidence_2.png)

![Mosaic](images/Mosaic_Confidence_3.png)

## Confidence Curves:

![Confidence Curve](images/F1_Confidence_Curve.png)

![Confidence Curve](images/Precision_Confidence_Curve.png)

![Confidence Curve](images/Precision_Recall_Curve.png)

![Confidence Curve](images/Recall_Confidence_Curve.png)

### Confusion Matrix:

![Confusion Matrix](images/Confusion_Matrix.png)

### Performance Graphs: 

![Graphs](images/Performance_Graphs.png)

## Label Graphs

![Label Graphs](images/labels_graph_1.png)

![Label Graphs](images/Labels_Graph_2.png)

### Results:

![Val](images/media_images_Validation_36_c257709a16cc6aa5b6a5.jpg)

![Val](images/media_images_Validation_36_d1ba1d852438b09a2f26.jpg)

![Val](images/media_images_Validation_36_9a5c1fc8c0b207f95445.jpg)

