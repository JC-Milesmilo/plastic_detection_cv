import numpy as np
import cv2
import torch
import numpy as np

#Vamos a capturar el objeto que queremos identificar
model = torch.hub.load('ultralytics/yolov5','custom', 
                    path='C:\\Users\\jca7x\\Desktop\\DMU_FinalPorj\\plastic_detection\\model\\bestExp11_SELECTED_1.pt')

cap = cv2.VideoCapture(0)

while True:
    ret, fram = cap.read()
    #detection
    detect = model(fram)

    info = detect.pandas().xyxy[0]
    print(info)

    #mostrar fps
    cv2.imshow('Plastic detect',np.squeeze(detect.render()))

    #leer teclado
    t = cv2.waitKey(5)

    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()