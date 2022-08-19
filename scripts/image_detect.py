import numpy as np
import cv2
import torch
import numpy as np

# PyTorch Hub
import torch

# Model
model = torch.hub.load('ultralytics/yolov5','custom', 
                    path='C:\\Users\\jca7x\\Desktop\\DMU_FinalPorj\\plastic_detection\\model\\bestExp11_SELECTED_1.pt')

# Images
dir = 'C:\\Users\\jca7x\\Desktop\\DMU_FinalPorj\\plastic_detection\\resources\\img\\lala.jpg'

# Inference
results = model(dir)