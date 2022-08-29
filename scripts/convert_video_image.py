import cv2
import os

file = 'VID_20220727_102635.mp4'
vidcap = cv2.VideoCapture(f'{os.getcwd()}\\resources\\video\\pre_processed\\Temp\\{file}')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(f'{os.getcwd()}\\resources\\video\\pre_processed\\frame{count}.jpg' % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1