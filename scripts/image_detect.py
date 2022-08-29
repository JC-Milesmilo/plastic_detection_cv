import os
import torch
import pandas as pd
from datetime import datetime

class model():

    def __init__(self,best_pt):
        # current dateTime
        self.now = datetime.now()
        self.date_time_str = self.now.strftime("%d-%m-%Y")
        # Model

        self.model = torch.hub.load('ultralytics/yolov5','custom', 
                    path= f'{os.getcwd()}\\model\\{best_pt}')

    def result_model(self):
        dir = f'{os.getcwd()}\\resources\\img\\pre_processed\\{self.date_time_str}\\'

        df = pd.DataFrame()
        for filename in os.listdir(dir):
            file_path = os.path.join(dir, filename)
            results = self.model(file_path)
            #results.xyxy[0]  # im predictions (tensor)
            #results.pandas().xyxy[0]  # im predictions (pandas)
            #results.pandas().xyxy[0].value_counts('name')
            object_detected = results.pandas().xyxy[0].value_counts('name')

            #file_split = os.path.splitext("/path/to/some/file.txt")[0]
            file_split = os.path.splitext(filename)[0]
            file_split = file_split.split('_')
            latitude = file_split[0]
            longitude = file_split[1]
            values = {'latitude': float(latitude),'longitude': float(longitude),'count': int(object_detected[0])}
            values = pd.DataFrame([values])
            df = pd.concat((df, values),ignore_index = True)
        return df

#mode = model('Exp11')

#mode.result_model()