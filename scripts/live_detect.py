import numpy as np
import cv2
import torch
import os
import numpy as np


class live_detect():

    def __init__(self,best_pt):
        self.model = torch.hub.load('ultralytics/yolov5','custom', 
                    path= f'{os.getcwd()}\\model\\{best_pt}')
        return

    def live(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, fram = cap.read()
            #detection
            detect = self.model(fram)

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
