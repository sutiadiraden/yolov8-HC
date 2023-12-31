import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np

model=YOLO('best (4).pt')


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)
  

# Video
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
cap=cv2.VideoCapture('jenis.mp4')

# Image
img = cv2.imread("DERC11_39.jpg", cv2.IMREAD_COLOR)


my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)

count=0

while True:    
    ret,frame = cap.read()
    
    if not ret:
        break

    count += 1
    if count % 3 != 0:
        continue
    
    frame=cv2.resize(frame,(1020,500))
    results=model.predict(frame)
 #   print(results)
    a=results[0].boxes.data
    print(a)
    px=pd.DataFrame(a).astype("float")
#    print(px)
  
    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
        cvzone.putTextRect(frame,f'{c}',(x1,y1),1,1)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
