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

## Repository:

Best_Weights.pt — The trained YOLOv5 model weights

### Images:

Confidence Curves:

![Confidence Curve](images/media_images_Results_36_e4bed294bd7ca59c259a.png)

![Confidence Curve](images/media_images_Results_36_2a5a551479623f33c06a.png)

![Confidence Curve](images/media_images_Results_36_5bd4c40bf45cd7813688.png)

![Confidence Curve](images/media_images_Results_36_988d24134f85eef8bc12.png)


### Confusion Matrix:

![Confusion Matrix](images/Image.jpg)

### Graphs: 

![Graphs](images/media_images_Results_36_f6e0f40945966f09baec.png)

### Results:

![Val](images/media_images_Validation_36_c257709a16cc6aa5b6a5.jpg)

![Val](images/media_images_Validation_36_d1ba1d852438b09a2f26.jpg)

![Val](images/media_images_Validation_36_9a5c1fc8c0b207f95445.jpg)


### Note:

I chose to do 36 epochs, as I found after that performance began to fall off after:

![v1](images/graph_v1.jpeg)

![v1](images/graph_v1_loss.jpeg)

![v1](images/graph_v1_precision.jpeg)

